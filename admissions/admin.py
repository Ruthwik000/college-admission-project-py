from django.contrib import admin
from .models import Application, AdmissionList, Admission
from django.utils.html import format_html
import csv
from django.http import HttpResponse
from notifications.models import Notification
from django.core.mail import send_mail
from django.conf import settings

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['application_number', 'student', 'stream', 'status_badge', 'priority', 'application_date']
    list_filter = ['status', 'stream__college', 'application_date', 'documents_verified', 'fees_paid']
    search_fields = ['application_number', 'student__username', 'student__email']
    readonly_fields = ['application_number', 'application_date', 'created_at', 'updated_at']
    actions = ['accept_applications', 'reject_applications']
    list_editable = ['priority']
    list_per_page = 25

    def status_badge(self, obj):
        color = {
            'PENDING': 'gray',
            'SELECTED_LIST_1': 'blue',
            'SELECTED_LIST_2': 'blue',
            'SELECTED_LIST_3': 'blue',
            'REJECTED': 'red',
            'ADMITTED': 'green',
            'CANCELLED': 'orange',
        }.get(obj.status, 'gray')
        return format_html('<span style="color:white; background:{}; padding:2px 8px; border-radius:8px;">{}</span>', color, obj.get_status_display())
    status_badge.short_description = 'Status'

    def accept_applications(self, request, queryset):
        for application in queryset:
            application.status = 'ADMITTED'
            application.save()
        self.message_user(request, f"{queryset.count()} applications marked as ADMITTED.")
    accept_applications.short_description = "Accept selected applications"

    def reject_applications(self, request, queryset):
        for application in queryset:
            application.status = 'REJECTED'
            application.save()
        self.message_user(request, f"{queryset.count()} applications marked as REJECTED.")
    reject_applications.short_description = "Reject selected applications"

@admin.register(AdmissionList)
class AdmissionListAdmin(admin.ModelAdmin):
    list_display = ['stream', 'list_type', 'year', 'student_count', 'is_published', 'published_date']
    list_filter = ['list_type', 'year', 'is_published', 'stream__college']
    search_fields = ['stream__name', 'stream__college__name']
    readonly_fields = ['created_at']
    actions = ['publish_lists', 'unpublish_lists']
    list_per_page = 25

    def student_count(self, obj):
        return obj.applications.count()
    student_count.short_description = 'Students'

    def publish_lists(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f"{updated} lists published.")
    publish_lists.short_description = "Publish selected lists"

    def unpublish_lists(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f"{updated} lists unpublished.")
    unpublish_lists.short_description = "Unpublish selected lists"

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['roll_number', 'application', 'section', 'academic_year', 'is_active', 'admission_date', 'print_letter']
    list_filter = ['academic_year', 'is_active', 'admission_date']
    search_fields = ['roll_number', 'application__student__username']
    actions = ['export_as_csv']
    list_editable = ['section', 'is_active']
    list_per_page = 25

    def print_letter(self, obj):
        return format_html('<a class="button" href="/admin/admissions/admission/{}/print/" target="_blank">🖨 Print</a>', obj.id)
    print_letter.short_description = 'Print Letter'

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=admissions.csv'
        writer = csv.writer(response)
        writer.writerow(['Roll Number', 'Student', 'Stream', 'Section', 'Academic Year', 'Admission Date', 'Active'])
        for obj in queryset:
            writer.writerow([
                obj.roll_number,
                obj.application.student.get_full_name(),
                obj.application.stream.name,
                obj.section,
                obj.academic_year,
                obj.admission_date,
                obj.is_active
            ])
        return response
    export_as_csv.short_description = "Export selected as CSV"
