from django.db import models
from django.contrib.auth.models import User
from colleges.models import Stream
from accounts.models import StudentProfile
from django.core.mail import send_mail
from django.conf import settings
from notifications.models import Notification

class Application(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SELECTED_LIST_1', 'Selected in List 1'),
        ('SELECTED_LIST_2', 'Selected in List 2'),
        ('SELECTED_LIST_3', 'Selected in List 3'),
        ('REJECTED', 'Rejected'),
        ('ADMITTED', 'Admitted'),
        ('CANCELLED', 'Cancelled'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='applications')
    application_number = models.CharField(max_length=20, unique=True)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    priority = models.IntegerField(default=1)  # Student's preference order
    documents_verified = models.BooleanField(default=False)
    fees_paid = models.BooleanField(default=False)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.stream.name} - {self.status}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_instance = None
        if not is_new:
            try:
                # Fetch the old instance before saving
                old_instance = Application.objects.get(pk=self.pk)
            except Application.DoesNotExist:
                pass # Should not happen on update

        # Save the application
        super().save(*args, **kwargs)

        # Handle notifications after saving
        if is_new:
             # Create notification for new application after saving
            Notification.objects.create(
                user=self.student,
                title='Application Submitted',
                message=f'Your application for {self.stream.name} has been submitted successfully.',
                notification_type='APPLICATION'
            )
        elif old_instance and old_instance.status != self.status:
            # Create notification for status change after saving
            if self.status == 'ADMITTED':
                title = 'Application Accepted'
                message = f'Your application for {self.stream.name} has been accepted. You are now admitted to the program.'
                email_subject = 'Application Accepted - College Admission System'
                email_message = f"""
Dear {self.student.get_full_name()},

Your application for {self.stream.name} has been accepted. You are now admitted to the program.

Application Details:
- Application Number: {self.application_number}
- Stream: {self.stream.name}
- College: {self.stream.college.name}
- Status: Admitted

Please log in to your account to view more details and complete the admission process.

Best regards,
College Admission System
"""
            elif self.status == 'REJECTED':
                title = 'Application Rejected'
                message = f'Your application for {self.stream.name} has been rejected.'
                email_subject = 'Application Status Update - College Admission System'
                email_message = f"""
Dear {self.student.get_full_name()},

We regret to inform you that your application for {self.stream.name} has been rejected.

Application Details:
- Application Number: {self.application_number}
- Stream: {self.stream.name}
- College: {self.stream.college.name}
- Status: Rejected

You can apply for other streams or colleges through your account.

Best regards,
College Admission System
"""
            elif self.status.startswith('SELECTED_LIST_'):
                list_number = self.status.split('_')[-1]
                title = f'Selected in List {list_number}'
                message = f'Your application for {self.stream.name} has been selected in List {list_number}.'
                email_subject = f'Selected in List {list_number} - College Admission System'
                email_message = f"""
Dear {self.student.get_full_name()},

Your application for {self.stream.name} has been selected in List {list_number}.

Application Details:
- Application Number: {self.application_number}
- Stream: {self.stream.name}
- College: {self.stream.college.name}
- Status: Selected in List {list_number}

Please check your account for further instructions and next steps.

Best regards,
College Admission System
"""
            else:
                title = 'Application Status Updated'
                message = f'Your application status for {self.stream.name} has been updated to {self.get_status_display()}.'
                email_subject = 'Application Status Update - College Admission System'
                email_message = f"""
Dear {self.student.get_full_name()},

Your application status has been updated.

Application Details:
- Application Number: {self.application_number}
- Stream: {self.stream.name}
- College: {self.stream.college.name}
- Status: {self.get_status_display()}

Please log in to your account to view more details.

Best regards,
College Admission System
"""

            Notification.objects.create(
                user=self.student,
                title=title,
                message=message,
                notification_type='ADMISSION'
            )

    class Meta:
        ordering = ['-application_date']
        unique_together = ['student', 'stream']

class AdmissionList(models.Model):
    LIST_TYPES = [
        ('LIST_1', 'Merit List 1'),
        ('LIST_2', 'Merit List 2'),
        ('LIST_3', 'Merit List 3'),
        ('FINAL', 'Final Admission List'),
    ]

    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='admission_lists')
    list_type = models.CharField(max_length=10, choices=LIST_TYPES)
    year = models.IntegerField()
    applications = models.ManyToManyField(Application, related_name='admission_lists')
    published_date = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stream.name} - {self.list_type} - {self.year}"

    class Meta:
        ordering = ['-year', 'stream', 'list_type']
        unique_together = ['stream', 'list_type', 'year']

class Admission(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    admission_date = models.DateTimeField(auto_now_add=True)
    roll_number = models.CharField(max_length=20, unique=True)
    section = models.CharField(max_length=10, blank=True)
    academic_year = models.CharField(max_length=9)  # e.g., "2024-2025"
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.application.student.get_full_name()} - {self.roll_number}"

    class Meta:
        ordering = ['roll_number']
