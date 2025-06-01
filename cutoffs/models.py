from django.db import models
from colleges.models import Stream

class CutOff(models.Model):
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
        return f"{self.stream.name} - {self.cutoff_type} - {self.category} - {self.cutoff_percentage}%"

    class Meta:
        ordering = ['-year', 'stream', 'category']
        unique_together = ['stream', 'cutoff_type', 'year', 'category']
