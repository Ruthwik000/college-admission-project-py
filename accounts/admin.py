from django.contrib import admin
from .models import UserProfile, StudentProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'phone_number', 'gender', 'created_at']
    list_filter = ['user_type', 'gender', 'created_at']
    search_fields = ['user__username', 'user__email', 'phone_number']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'user_profile', 'father_name', 'percentage', 'category', 'passing_year']
    list_filter = ['category', 'passing_year', 'board']
    search_fields = ['student_id', 'user_profile__user__username', 'father_name']
