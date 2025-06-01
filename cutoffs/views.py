from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import CutOff
from colleges.models import Stream, College
from django.http import HttpResponse
from django.db.models import Max, Min
from accounts.decorators import user_type_required
import random

# Create your views here.

@login_required
def cutoff_list(request):
    if not request.user.userprofile.user_type == 'ADMIN':
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('home')
    
    current_year = timezone.now().year
    cutoffs = CutOff.objects.filter(year=current_year).order_by('stream', 'cutoff_type')
    return render(request, 'cutoffs/cutoff_list.html', {'cutoffs': cutoffs})

@login_required
def create_cutoff(request):
    if not request.user.userprofile.user_type == 'ADMIN':
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('home')
    
    if request.method == 'POST':
        stream_id = request.POST.get('stream')
        cutoff_type = request.POST.get('cutoff_type')
        category = request.POST.get('category')
        cutoff_percentage = request.POST.get('cutoff_percentage')
        available_seats = request.POST.get('available_seats')
        
        stream = get_object_or_404(Stream, id=stream_id)
        
        # Create cutoff
        cutoff = CutOff.objects.create(
            stream=stream,
            cutoff_type=cutoff_type,
            category=category,
            cutoff_percentage=cutoff_percentage,
            available_seats=available_seats,
            year=timezone.now().year
        )
        
        messages.success(request, 'Cutoff created successfully!')
        return redirect('cutoffs:cutoff_list')
    
    streams = Stream.objects.filter(is_active=True)
    return render(request, 'cutoffs/create_cutoff.html', {'streams': streams})

@login_required
def edit_cutoff(request, cutoff_id):
    if not request.user.userprofile.user_type == 'ADMIN':
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('home')
    
    cutoff = get_object_or_404(CutOff, id=cutoff_id)
    
    if request.method == 'POST':
        cutoff.cutoff_type = request.POST.get('cutoff_type')
        cutoff.category = request.POST.get('category')
        cutoff.cutoff_percentage = request.POST.get('cutoff_percentage')
        cutoff.available_seats = request.POST.get('available_seats')
        cutoff.save()
        
        messages.success(request, 'Cutoff updated successfully!')
        return redirect('cutoffs:cutoff_list')
    
    return render(request, 'cutoffs/edit_cutoff.html', {'cutoff': cutoff})

@login_required
def delete_cutoff(request, cutoff_id):
    if not request.user.userprofile.user_type == 'ADMIN':
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('home')
    
    cutoff = get_object_or_404(CutOff, id=cutoff_id)
    
    if request.method == 'POST':
        cutoff.delete()
        messages.success(request, 'Cutoff deleted successfully!')
        return redirect('cutoffs:cutoff_list')
    
    return render(request, 'cutoffs/delete_cutoff.html', {'cutoff': cutoff})

@user_type_required('STUDENT')
def compare_cutoffs_view(request):
    # Add print statement here to debug user_type
    if hasattr(request.user, 'userprofile'):
        print(f"Logged in user type: {request.user.userprofile.user_type}")
    else:
        print("Logged in user has no userprofile.")

    # Get all years with CURRENT cutoffs, ordered by year descending
    available_years = CutOff.objects.filter(
        cutoff_type__startswith='CURRENT'
    ).order_by('-year').values_list('year', flat=True).distinct()

    selected_year = request.GET.get('year')

    if not selected_year and available_years:
        # Default to the latest available year if none is selected
        selected_year = available_years.first()
    elif selected_year:
        # Ensure the selected year is an integer and is in the available years
        try:
            selected_year = int(selected_year)
            if selected_year not in available_years:
                # If selected year is not available, default to latest or none
                selected_year = available_years.first() if available_years else None
        except (ValueError, TypeError):
            # Handle invalid year parameter
            selected_year = available_years.first() if available_years else None

    # Get available categories from the CutOff model choices
    available_categories = CutOff.CATEGORY_CHOICES
    selected_category = request.GET.get('category')

    # Default to 'GENERAL' if no category is selected and GENERAL is an option
    if not selected_category:
        default_category = next((cat[0] for cat in available_categories if cat[0] == 'GENERAL'), None)
        selected_category = default_category
    else:
        # Ensure selected category is valid
        if not any(selected_category == cat[0] for cat in available_categories):
            selected_category = None # Or handle as an error

    comparison_data = []
    years_to_display = [] # This will now only contain the selected year for the header
    if selected_year and selected_category:
        years_to_display = [selected_year]
        # Get all streams that belong to a college
        all_streams = Stream.objects.select_related('college').order_by('college__name', 'name')

        for stream in all_streams:
            row_data = {
                'stream': stream,
                'college': stream.college,
                'cutoff': 'N/A' # Default to N/A
            }
            # Fetch cutoff for the selected year and category from database
            cutoff = CutOff.objects.filter(
                stream=stream,
                year=selected_year,
                cutoff_type__startswith='CURRENT', # Ensure we only get 'CURRENT' types
                category=selected_category
            ).order_by('-cutoff_type').first() # Get the latest if multiple CURRENT types exist

            if cutoff:
                row_data['cutoff'] = cutoff.closing_rank # Use closing_rank from database
            else:
                # Generate consistent sample data if no database entry is found
                # Use a combination of stream id, year, and category for a unique but fixed seed
                seed_value = stream.id * 1000000 + selected_year * 100 + hash(selected_category) % 100
                random.seed(seed_value)

                # Generate sample cutoff values based on category with different ranges
                if selected_category == 'GENERAL':
                    row_data['cutoff'] = random.randint(10000, 20000)
                elif selected_category == 'OBC':
                    row_data['cutoff'] = random.randint(20000, 30000)
                elif selected_category == 'SC':
                    row_data['cutoff'] = random.randint(30000, 40000)
                elif selected_category == 'ST':
                    row_data['cutoff'] = random.randint(35000, 45000)
                elif selected_category == 'EWS':
                    row_data['cutoff'] = random.randint(25000, 35000)


            comparison_data.append(row_data)

    context = {
        'comparison_data': comparison_data,
        'available_years': available_years,
        'selected_year': selected_year,
        'years_to_display': years_to_display,
        'available_categories': available_categories,
        'selected_category': selected_category,
    }

    return render(request, 'cutoffs/compare_cutoffs.html', context)
