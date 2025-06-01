from django.contrib import admin
from .models import College, Stream

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'phone', 'email', 'established_year', 'closing_rank', 'created_at']
    list_filter = ['established_year', 'created_at']
    search_fields = ['name', 'code', 'email']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['closing_rank']

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ['name', 'college', 'stream_type', 'total_seats', 'fees_per_year', 'is_active']
    list_filter = ['stream_type', 'is_active', 'college']
    search_fields = ['name', 'college__name']
    readonly_fields = ['created_at']
