from django.db import models
from django.contrib.auth.models import User

class College(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    established_year = models.IntegerField()
    description = models.TextField()
    logo = models.ImageField(upload_to='college_logos/', blank=True, null=True)
    closing_rank = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
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
