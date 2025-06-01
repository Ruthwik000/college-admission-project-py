from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, StudentProfile
from .forms import UserProfileForm, StudentProfileForm
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, user_type='STUDENT')
            messages.success(request, 'Registration successful! Please complete your profile.')
            login(request, user)
            return redirect('accounts:edit_profile')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    try:
        user_profile = request.user.userprofile
        student_profile = getattr(user_profile, 'studentprofile', None)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
        student_profile = None

    context = {
        'user_profile': user_profile,
        'student_profile': student_profile,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    try:
        student_profile = user_profile.studentprofile
    except StudentProfile.DoesNotExist:
        student_profile = None

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        student_form = StudentProfileForm(request.POST, instance=student_profile) if student_profile else StudentProfileForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            if student_profile:
                student_form.save()
            else:
                student_profile = student_form.save(commit=False)
                student_profile.user_profile = user_profile
                student_profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        user_form = UserProfileForm(instance=user_profile)
        student_form = StudentProfileForm(instance=student_profile) if student_profile else StudentProfileForm()

    context = {
        'user_form': user_form,
        'student_form': student_form,
    }
    return render(request, 'accounts/edit_profile.html', context)

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type', 'STUDENT')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            try:
                user_profile = user.userprofile
                if user_profile.user_type == user_type:
                    login(request, user)
                    if user_type == 'ADMIN':
                        return redirect('accounts:admin_dashboard')
                    else:
                        return redirect('accounts:profile')
                else:
                    messages.error(request, f'Invalid login type. Please login as {user_profile.user_type}.')
            except UserProfile.DoesNotExist:
                messages.error(request, 'User profile not found.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')

@login_required
def admin_dashboard(request):
    if not request.user.userprofile.user_type == 'ADMIN':
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('accounts:profile')
    return render(request, 'accounts/admin_dashboard.html')

# Placeholder views (can be removed if not needed)
# def statistics_dashboard(request):
#     return HttpResponse('This is the Statistics Dashboard page.')

# def send_notifications(request):
#     return HttpResponse('This is the Send Notifications page.')

# def change_password(request):
#     return HttpResponse('This is the Change Password page.')

# def audit_logs(request):
#     return HttpResponse('This is the Audit Logs page.')
