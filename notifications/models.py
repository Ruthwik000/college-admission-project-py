"""
Notification Models for the College Admission System.

This module contains models related to the notification system,
including user notifications and system announcements.
"""

from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    """
    Notification model to store user notifications.
    
    This model manages notifications sent to users about various events
    in the admission process.
    
    Attributes:
        user (ForeignKey): Reference to the User model
        title (CharField): Notification title
        message (TextField): Notification message
        notification_type (CharField): Type of notification
        is_read (BooleanField): Whether the notification has been read
        created_at (DateTimeField): When the notification was created
        link (URLField): Optional link related to the notification
    """
    NOTIFICATION_TYPES = [
        ('APPLICATION', 'Application Update'),
        ('DOCUMENT', 'Document Verification'),
        ('PAYMENT', 'Payment Status'),
        ('ADMISSION', 'Admission Status'),
        ('SYSTEM', 'System Announcement'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        """String representation of the Notification model."""
        return f"{self.title} - {self.user.username}"

    class Meta:
        """Meta options for the Notification model."""
        ordering = ['-created_at']

class Announcement(models.Model):
    """
    Announcement model to store system-wide announcements.
    
    This model manages important announcements that need to be displayed
    to all users or specific user groups.
    
    Attributes:
        title (CharField): Announcement title
        content (TextField): Announcement content
        start_date (DateField): When the announcement becomes active
        end_date (DateField): When the announcement expires
        is_active (BooleanField): Whether the announcement is currently active
        target_audience (CharField): Who should see this announcement
    """
    TARGET_AUDIENCE_CHOICES = [
        ('ALL', 'All Users'),
        ('STUDENTS', 'Students Only'),
        ('ADMIN', 'Administrators Only'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    target_audience = models.CharField(max_length=20, choices=TARGET_AUDIENCE_CHOICES, default='ALL')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the Announcement model."""
        return self.title

    class Meta:
        """Meta options for the Announcement model."""
        ordering = ['-created_at']
