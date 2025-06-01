from django.contrib import admin
from .models import CutOff

@admin.register(CutOff)
class CutOffAdmin(admin.ModelAdmin):
    list_display = ['stream', 'cutoff_type', 'year', 'category', 'cutoff_percentage', 'available_seats', 'closing_rank']
    list_filter = ['cutoff_type', 'year', 'category', 'stream__college']
    search_fields = ['stream__name', 'stream__college__name']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['cutoff_percentage', 'available_seats', 'closing_rank']
