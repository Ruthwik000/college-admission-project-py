"""
College Models for the College Admission System.

This module contains models related to college information management,
including college details, courses, and other college-specific data.
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class College(models.Model):
    """
    College model to store information about educational institutions.
    
    This model stores basic information about colleges including their name,
    location, contact details, and other relevant information.
    
    Attributes:
        name (CharField): Name of the college
        location (CharField): Physical location of the college
        description (TextField): Detailed description of the college
        website (URLField): College's website URL
        contact_email (EmailField): College's contact email
        contact_phone (CharField): College's contact phone number
        established_year (IntegerField): Year the college was established
        accreditation (CharField): College's accreditation status
        facilities (TextField): Available facilities at the college
    """
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    website = models.URLField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    established_year = models.IntegerField()
    accreditation = models.CharField(max_length=100)
    facilities = models.TextField()

    def __str__(self):
        """String representation of the College model."""
        return self.name

    class Meta:
        """Meta options for the College model."""
        ordering = ['name']

class Stream(models.Model):
    STREAM_TYPES = [
        ('SCIENCE', 'Science'),
        ('COMMERCE', 'Commerce'),
        ('ARTS', 'Arts'),
        ('ENGINEERING', 'Engineering'),
        ('MEDICAL', 'Medical'),
        ('LAW', 'Law'),
        ('MANAGEMENT', 'Management'),
    ]

    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='streams')
    name = models.CharField(max_length=100)
    stream_type = models.CharField(max_length=20, choices=STREAM_TYPES)
    duration_years = models.IntegerField()
    total_seats = models.IntegerField()
    fees_per_year = models.DecimalField(max_digits=10, decimal_places=2)
    eligibility_criteria = models.TextField()
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.college.name} - {self.name}"

    class Meta:
        ordering = ['college', 'name']
        unique_together = ['college', 'name']

class Course(models.Model):
    """
    Course model to store information about courses offered by colleges.
    
    This model stores information about different courses offered by colleges,
    including course name, duration, fees, and other details.
    
    Attributes:
        college (ForeignKey): Reference to the College model
        name (CharField): Name of the course
        duration (IntegerField): Duration of the course in years
        fees (DecimalField): Course fees
        seats_available (IntegerField): Number of available seats
        eligibility_criteria (TextField): Course eligibility requirements
    """
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="Duration in years")
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    seats_available = models.IntegerField()
    eligibility_criteria = models.TextField()

    def __str__(self):
        """String representation of the Course model."""
        return f"{self.name} at {self.college.name}"

    class Meta:
        """Meta options for the Course model."""
        ordering = ['college', 'name']
        unique_together = ['college', 'name']
