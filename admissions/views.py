from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Application, AdmissionList, Admission
from colleges.models import Stream
from notifications.models import Notification
from django.http import HttpResponse
from accounts.decorators import user_type_required

# Create your views here.

@login_required
def apply_for_admission(request, stream_id):
    stream = get_object_or_404(Stream, id=stream_id)
    
    # Check if student has already applied
    if Application.objects.filter(student=request.user, stream=stream).exists():
        messages.warning(request, 'You have already applied for this stream.')
        return redirect('admissions:my_applications')
    
    if request.method == 'POST':
        # Create new application
        application = Application.objects.create(
            student=request.user,
            stream=stream,
            application_number=f"APP{timezone.now().strftime('%Y%m%d%H%M%S')}",
            priority=request.POST.get('priority', 1)
        )
        
        # Create notification
        Notification.objects.create(
            user=request.user,
            title='Application Submitted',
            message=f'Your application for {stream.name} has been submitted successfully.',
            notification_type='APPLICATION'
        )
        
        messages.success(request, 'Application submitted successfully!')
        return redirect('admissions:my_applications')
    
    return render(request, 'admissions/apply.html', {'stream': stream})

@login_required
def my_applications(request):
    applications = Application.objects.filter(student=request.user).order_by('-application_date')
    return render(request, 'admissions/my_applications.html', {'applications': applications})

@login_required
def application_detail(request, application_id):
    application = get_object_or_404(Application, id=application_id, student=request.user)
    return render(request, 'admissions/application_detail.html', {'application': application})

@user_type_required('ADMIN')
def admission_lists(request):
    current_year = timezone.now().year
    admission_lists = AdmissionList.objects.filter(year=current_year).order_by('stream', 'list_type')
    return render(request, 'admissions/admission_lists.html', {'admission_lists': admission_lists})

@user_type_required('ADMIN')
def create_admission_list(request):
    if request.method == 'POST':
        stream_id = request.POST.get('stream')
        list_type = request.POST.get('list_type')
        stream = get_object_or_404(Stream, id=stream_id)
        admission_list = AdmissionList.objects.create(
            stream=stream,
            list_type=list_type,
            year=timezone.now().year
        )
        cutoff = stream.cutoffs.filter(
            cutoff_type=f'CURRENT_{list_type[-1]}',
            year=timezone.now().year
        ).first()
        if cutoff:
            eligible_applications = Application.objects.filter(
                stream=stream,
                status='PENDING'
            ).order_by('-priority')
            admission_list.applications.add(*eligible_applications)
            for application in eligible_applications:
                application.status = f'SELECTED_LIST_{list_type[-1]}'
                application.save()
                Notification.objects.create(
                    user=application.student,
                    title='Selected in Admission List',
                    message=f'You have been selected in {list_type} for {stream.name}.',
                    notification_type='ADMISSION'
                )
        messages.success(request, 'Admission list created successfully!')
        return redirect('admissions:admission_lists')
    streams = Stream.objects.filter(is_active=True)
    return render(request, 'admissions/create_admission_list.html', {'streams': streams})

@user_type_required('ADMIN')
def publish_list(request, list_id):
    admission_list = get_object_or_404(AdmissionList, id=list_id)
    if request.method == 'POST':
        admission_list.is_published = True
        admission_list.published_date = timezone.now()
        admission_list.save()
        for application in admission_list.applications.all():
            Notification.objects.create(
                user=application.student,
                title='Admission List Published',
                message=f'The {admission_list.get_list_type_display()} for {admission_list.stream.name} has been published. Please check your application status.',
                notification_type='ADMISSION'
            )
        messages.success(request, 'Admission list published successfully!')
        return redirect('admissions:admission_lists')
    return redirect('admissions:admission_lists')

@user_type_required('ADMIN')
def register_admission(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if request.method == 'POST':
        admission = Admission.objects.create(
            application=application,
            roll_number=f"ROLL{timezone.now().strftime('%Y%m%d%H%M%S')}",
            section=request.POST.get('section', ''),
            academic_year=f"{timezone.now().year}-{timezone.now().year + 1}"
        )
        application.status = 'ADMITTED'
        application.save()
        Notification.objects.create(
            user=application.student,
            title='Admission Confirmed',
            message=f'Your admission to {application.stream.name} has been confirmed. Your roll number is {admission.roll_number}.',
            notification_type='ADMISSION'
        )
        messages.success(request, 'Admission registered successfully!')
        return redirect('admissions:admission_lists')
    return render(request, 'admissions/register_admission.html', {'application': application})

@user_type_required('ADMIN')
def cancel_admission(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if request.method == 'POST':
        application.status = 'CANCELLED'
        application.save()
        Notification.objects.create(
            user=application.student,
            title='Admission Cancelled',
            message=f'Your admission to {application.stream.name} has been cancelled.',
            notification_type='ADMISSION'
        )
        messages.success(request, 'Admission cancelled successfully!')
        return redirect('admissions:admission_lists')
    return render(request, 'admissions/cancel_admission.html', {'application': application})

# Placeholder views (can be removed if not needed)
# def accept_reject(request):
#     return HttpResponse('This is the Accept/Reject Applications page.')

# def track_status(request):
#     return HttpResponse('This is the Track Status page.')

# def bulk_actions(request):
#     return HttpResponse('This is the Bulk Actions page.')

# def register_students(request):
#     return HttpResponse('This is the Register Students page.')

# def remove_student(request):
#     return HttpResponse('This is the Remove Student page.')

# def final_list(request):
#     return HttpResponse('This is the Final List of Admitted Students page.')
