"""
User Profile Models for the College Admission System.

This module contains the UserProfile model which extends Django's built-in User model
to store additional information about users in the system.
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """
    UserProfile model extends the default User model with additional fields.
    
    This model is used to store additional information about users that is not
    included in Django's default User model, such as phone number and address.
    
    Attributes:
        user (OneToOneField): One-to-one relationship with Django's User model
        phone_number (CharField): User's contact phone number
        address (TextField): User's physical address
    """
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
        """String representation of the UserProfile model."""
        return f"{self.user.username} - {self.user_type}"

    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to automatically create a UserProfile when a new User is created.
    
    Args:
        sender: The model class (User)
        instance: The actual instance being saved
        created: Boolean; True if a new record was created
        **kwargs: Additional keyword arguments
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal handler to automatically save the UserProfile when the User is saved.
    
    Args:
        sender: The model class (User)
        instance: The actual instance being saved
        **kwargs: Additional keyword arguments
    """
    instance.userprofile.save()

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
