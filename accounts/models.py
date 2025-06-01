from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserProfile(models.Model):
    USER_TYPES = [
        ('STUDENT', 'Student'),
        ('ADMIN', 'Admin'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='STUDENT')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"

    class Meta:
        ordering = ['user__username']

class StudentProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=17)
    previous_school = models.CharField(max_length=200)
    board = models.CharField(max_length=50)
    passing_year = models.IntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=20, choices=[
        ('GENERAL', 'General'),
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('EWS', 'EWS'),
    ])

    def __str__(self):
        return f"{self.user_profile.user.get_full_name()} - {self.student_id}"

    class Meta:
        ordering = ['student_id']
