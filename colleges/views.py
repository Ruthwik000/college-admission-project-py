from django.shortcuts import render, get_object_or_404
from .models import College, Stream
from cutoffs.models import CutOff
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Min

def college_list(request):
    colleges = College.objects.all()
    return render(request, 'colleges/college_list.html', {'colleges': colleges})

def college_detail(request, college_id):
    college = get_object_or_404(College, id=college_id)
    streams = college.streams.filter(is_active=True)

    # Find the latest year with CURRENT cutoffs for streams in this college
    latest_year = CutOff.objects.filter(
        stream__in=streams,
        cutoff_type__startswith='CURRENT'
    ).aggregate(Min('year'))['year__min'] # Using min just to get any year, could be max or distinct

    # Attach the lowest closing rank from the latest current year cutoff to each stream
    for stream in streams:
        lowest_closing_rank = None
        if latest_year:
            current_cutoffs = CutOff.objects.filter(
                stream=stream,
                year=latest_year,
                cutoff_type__startswith='CURRENT'
            ).exclude(closing_rank__isnull=True) # Exclude cutoffs with no closing rank

            if current_cutoffs.exists():
                # Find the minimum closing rank among relevant cutoffs
                lowest_closing_rank = current_cutoffs.aggregate(Min('closing_rank'))['closing_rank__min']

        stream.lowest_closing_rank = lowest_closing_rank

    return render(request, 'colleges/college_detail.html', {
        'college': college,
        'streams': streams
    })

def stream_list(request, college_id):
    college = get_object_or_404(College, id=college_id)
    streams = college.streams.filter(is_active=True)
    return render(request, 'colleges/stream_list.html', {
        'college': college,
        'streams': streams
    })

def stream_detail(request, stream_id):
    stream = get_object_or_404(Stream, id=stream_id)
    previous_cutoffs = CutOff.objects.filter(
        stream=stream,
        cutoff_type='PREVIOUS'
    ).order_by('-year', 'category')
    current_cutoffs = CutOff.objects.filter(
        stream=stream,
        cutoff_type__startswith='CURRENT'
    ).order_by('cutoff_type', 'category')

    return render(request, 'colleges/stream_detail.html', {
        'stream': stream,
        'previous_cutoffs': previous_cutoffs,
        'current_cutoffs': current_cutoffs
    })

# Placeholder views (can be removed if not needed)
# def add_college(request):
#     return HttpResponse('This is the Add College page.')

# def manage_streams(request):
#     return HttpResponse('This is the Manage Streams page.')

# def set_seat_limits(request):
#     return HttpResponse('This is the Set Seat Limits page.')
