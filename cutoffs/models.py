"""
Cutoff Models for the College Admission System.

This module contains models related to cutoff scores and admission criteria
for different colleges and courses.
"""

from django.db import models
from colleges.models import Stream

class CutOff(models.Model):
    """
    Cutoff model to store admission cutoff scores.
    
    This model stores the minimum required scores for admission to different
    courses at various colleges.
    
    Attributes:
        stream (ForeignKey): Reference to the Stream model
        cutoff_type (CharField): Type of cutoff (Previous Year, Current Year - List 1, etc.)
        year (IntegerField): Academic year
        category (CharField): Student category (General, SC, ST, etc.)
        cutoff_percentage (DecimalField): Minimum required score
        available_seats (IntegerField): Total number of seats available
        closing_rank (IntegerField): Minimum required rank
    """
    CUTOFF_TYPES = [
        ('PREVIOUS', 'Previous Year'),
        ('CURRENT_1', 'Current Year - List 1'),
        ('CURRENT_2', 'Current Year - List 2'),
        ('CURRENT_3', 'Current Year - List 3'),
    ]

    CATEGORY_CHOICES = [
        ('GENERAL', 'General'),
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('EWS', 'EWS'),
    ]

    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='cutoffs')
    cutoff_type = models.CharField(max_length=20, choices=CUTOFF_TYPES)
    year = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    cutoff_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    available_seats = models.IntegerField(default=0)
    closing_rank = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the Cutoff model."""
        return f"{self.stream.name} - {self.cutoff_type} - {self.category} - {self.cutoff_percentage}%"

    class Meta:
        """Meta options for the Cutoff model."""
        ordering = ['-year', 'stream', 'category']
        unique_together = ['stream', 'cutoff_type', 'year', 'category']
