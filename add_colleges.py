import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_admission_system.settings')
django.setup()

from colleges.models import College, Stream
from cutoffs.models import CutOff

def add_college_data():
    # College 1: Zenith Institute of Technology
    college1, _ = College.objects.get_or_create(
        code="ZIT101",
        defaults={
            "name": "Zenith Institute of Technology",
            "address": "123 Tech Park Road, Bengaluru, Karnataka, 560001",
            "phone": "+91-9876543210",
            "email": "contact@zenithtech.edu.in",
            "website": "https://www.zenithtech.edu.in",
            "established_year": 1998,
            "description": "A premier institute offering advanced engineering programs with global exposure."
        }
    )

    # Stream 1.1: B.Tech in Computer Science for Zenith
    stream1_1, _ = Stream.objects.get_or_create(
        college=college1,
        name="B.Tech in Computer Science",
        defaults={
            "stream_type": "ENGINEERING",
            "duration_years": 4,
            "total_seats": 180,
            "fees_per_year": 125000.00,
            "eligibility_criteria": "10+2 with PCM, 75% marks, JEE Main rank required",
            "description": "Focus on AI, ML, software dev, cloud computing.",
            "is_active": True
        }
    )

    # CutOffs for Stream 1.1 (Zenith B.Tech CS)
    cutoffs_stream1_1 = [
        {"year": 2024, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 91.00, "available_seats": 8, "closing_rank": 12000},
        {"year": 2024, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 85.00, "available_seats": 15, "closing_rank": 18000},
        {"year": 2024, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 75.00, "available_seats": 12, "closing_rank": 25000},
        {"year": 2024, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 70.00, "available_seats": 10, "closing_rank": 30000},
        {"year": 2024, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 80.00, "available_seats": 8, "closing_rank": 20000},
        {"year": 2023, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 89.50, "available_seats": 10, "closing_rank": 14500},
        {"year": 2023, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 83.00, "available_seats": 18, "closing_rank": 20000},
        {"year": 2023, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 73.00, "available_seats": 15, "closing_rank": 28000},
        {"year": 2023, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 68.00, "available_seats": 12, "closing_rank": 32000},
        {"year": 2023, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 78.00, "available_seats": 10, "closing_rank": 22000},
        {"year": 2022, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 88.00, "available_seats": 12, "closing_rank": 16000},
        {"year": 2022, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 81.00, "available_seats": 20, "closing_rank": 22000},
        {"year": 2022, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 70.00, "available_seats": 18, "closing_rank": 30000},
        {"year": 2022, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 15, "closing_rank": 35000},
        {"year": 2022, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 75.00, "available_seats": 10, "closing_rank": 25000},
    ]
    for cutoff_data in cutoffs_stream1_1:
        CutOff.objects.update_or_create(stream=stream1_1, year=cutoff_data["year"], category=cutoff_data["category"], cutoff_type=cutoff_data["cutoff_type"], defaults=cutoff_data)

    # College 2: Crestview College of Management
    college2, _ = College.objects.get_or_create(
        code="CCM201",
        defaults={
            "name": "Crestview College of Management",
            "address": "45 Business Bay, Pune, Maharashtra, 411001",
            "phone": "+91-9023456789",
            "email": "info@crestview.ac.in",
            "website": "https://www.crestview.ac.in",
            "established_year": 2005,
            "description": "A business school fostering future leaders and entrepreneurs."
        }
    )

    # Stream 2.1: BBA for Crestview
    stream2_1, _ = Stream.objects.get_or_create(
        college=college2,
        name="BBA (Bachelor of Business Administration)",
        defaults={
            "stream_type": "MANAGEMENT",
            "duration_years": 3,
            "total_seats": 150,
            "fees_per_year": 90000.00,
            "eligibility_criteria": "10+2 with minimum 50%",
            "description": "Comprehensive business education with industry exposure.",
            "is_active": True
        }
    )

    # CutOffs for Stream 2.1 (Crestview BBA)
    cutoffs_stream2_1 = [
        {"year": 2024, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 78.00, "available_seats": 10, "closing_rank": 22000},
        {"year": 2024, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 72.00, "available_seats": 15, "closing_rank": 28000},
        {"year": 2024, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 12, "closing_rank": 35000},
        {"year": 2024, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 10, "closing_rank": 40000},
        {"year": 2024, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 70.00, "available_seats": 8, "closing_rank": 30000},
        {"year": 2023, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 76.00, "available_seats": 12, "closing_rank": 25000},
        {"year": 2023, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 70.00, "available_seats": 18, "closing_rank": 30000},
        {"year": 2023, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 63.00, "available_seats": 15, "closing_rank": 38000},
        {"year": 2023, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 58.00, "available_seats": 12, "closing_rank": 42000},
        {"year": 2023, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 68.00, "available_seats": 10, "closing_rank": 32000},
        {"year": 2022, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 74.00, "available_seats": 15, "closing_rank": 28000},
        {"year": 2022, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 68.00, "available_seats": 20, "closing_rank": 33000},
        {"year": 2022, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 18, "closing_rank": 40000},
        {"year": 2022, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 15, "closing_rank": 45000},
        {"year": 2022, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 12, "closing_rank": 35000},
    ]
    for cutoff_data in cutoffs_stream2_1:
        CutOff.objects.update_or_create(stream=stream2_1, year=cutoff_data["year"], category=cutoff_data["category"], cutoff_type=cutoff_data["cutoff_type"], defaults=cutoff_data)

    # College 3: Avalon School of Arts
    college3, _ = College.objects.get_or_create(
        code="ASA301",
        defaults={
            "name": "Avalon School of Arts",
            "address": "77 Culture Road, Jaipur, Rajasthan, 302001",
            "phone": "+91-9988776655",
            "email": "admissions@avalonarts.edu",
            "website": "https://www.avalonarts.edu",
            "established_year": 1985,
            "description": "One of India's oldest institutions for fine arts and liberal education."
        }
    )

    # Stream 3.1: BA in History for Avalon
    stream3_1, _ = Stream.objects.get_or_create(
        college=college3,
        name="BA in History",
        defaults={
            "stream_type": "ARTS",
            "duration_years": 3,
            "total_seats": 80,
            "fees_per_year": 60000.00,
            "eligibility_criteria": "10+2 with 50% marks",
            "description": "Study of world history with focus on Indian history and culture.",
            "is_active": True
        }
    )

    # CutOffs for Stream 3.1 (Avalon BA History)
    cutoffs_stream3_1 = [
        {"year": 2024, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 68.00, "available_seats": 5, "closing_rank": 28000},
        {"year": 2024, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 62.00, "available_seats": 8, "closing_rank": 35000},
        {"year": 2024, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 6, "closing_rank": 42000},
        {"year": 2024, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 50.00, "available_seats": 5, "closing_rank": 45000},
        {"year": 2024, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 4, "closing_rank": 38000},
        {"year": 2023, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 66.00, "available_seats": 6, "closing_rank": 30000},
        {"year": 2023, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 10, "closing_rank": 38000},
        {"year": 2023, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 53.00, "available_seats": 8, "closing_rank": 45000},
        {"year": 2023, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 48.00, "available_seats": 7, "closing_rank": 48000},
        {"year": 2023, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 58.00, "available_seats": 5, "closing_rank": 40000},
        {"year": 2022, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 64.00, "available_seats": 8, "closing_rank": 32000},
        {"year": 2022, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 58.00, "available_seats": 12, "closing_rank": 40000},
        {"year": 2022, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 50.00, "available_seats": 10, "closing_rank": 48000},
        {"year": 2022, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 45.00, "available_seats": 8, "closing_rank": 50000},
        {"year": 2022, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 7, "closing_rank": 42000},
    ]
    for cutoff_data in cutoffs_stream3_1:
        CutOff.objects.update_or_create(stream=stream3_1, year=cutoff_data["year"], category=cutoff_data["category"], cutoff_type=cutoff_data["cutoff_type"], defaults=cutoff_data)

    # College 4: Horizon Law Academy
    college4, _ = College.objects.get_or_create(
        code="HLA401",
        defaults={
            "name": "Horizon Law Academy",
            "address": "Sector 22, Dwarka, New Delhi, 110075",
            "phone": "+91-7890654321",
            "email": "office@horizonlaw.edu.in",
            "website": "https://www.horizonlaw.edu.in",
            "established_year": 2010,
            "description": "An upcoming law school focused on practical litigation and constitutional studies."
        }
    )

    # Stream 4.1: BA LLB (Integrated) for Horizon
    stream4_1, _ = Stream.objects.get_or_create(
        college=college4,
        name="BA LLB (Integrated)",
        defaults={
            "stream_type": "LAW",
            "duration_years": 5,
            "total_seats": 120,
            "fees_per_year": 140000.00,
            "eligibility_criteria": "10+2 with CLAT score",
            "is_active": True,
            "description": "Integrated law program focusing on foundational legal studies."
        }
    )

    # CutOffs for Stream 4.1 (Horizon BA LLB)
    cutoffs_stream4_1 = [
        {"year": 2024, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 88.00, "available_seats": 10, "closing_rank": 4200},
        {"year": 2024, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 82.00, "available_seats": 15, "closing_rank": 5500},
        {"year": 2024, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 75.00, "available_seats": 12, "closing_rank": 7000},
        {"year": 2024, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 70.00, "available_seats": 10, "closing_rank": 8000},
        {"year": 2024, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 80.00, "available_seats": 8, "closing_rank": 6000},
        {"year": 2023, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 86.00, "available_seats": 12, "closing_rank": 4800},
        {"year": 2023, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 80.00, "available_seats": 18, "closing_rank": 6000},
        {"year": 2023, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 73.00, "available_seats": 15, "closing_rank": 7500},
        {"year": 2023, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 68.00, "available_seats": 12, "closing_rank": 8500},
        {"year": 2023, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 78.00, "available_seats": 10, "closing_rank": 6500},
        {"year": 2022, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 84.00, "available_seats": 15, "closing_rank": 5500},
        {"year": 2022, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 78.00, "available_seats": 20, "closing_rank": 6800},
        {"year": 2022, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 70.00, "available_seats": 18, "closing_rank": 8000},
        {"year": 2022, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 15, "closing_rank": 9000},
        {"year": 2022, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 75.00, "available_seats": 12, "closing_rank": 7500},
    ]
    for cutoff_data in cutoffs_stream4_1:
        CutOff.objects.update_or_create(stream=stream4_1, year=cutoff_data["year"], category=cutoff_data["category"], cutoff_type=cutoff_data["cutoff_type"], defaults=cutoff_data)

    # College 5: Stellar School of Science
    college5, _ = College.objects.get_or_create(
        code="SSS501",
        defaults={
            "name": "Stellar School of Science",
            "address": "Sector 10, Chandigarh, 160010",
            "phone": "+91-8765432109",
            "email": "admissions@stellarscience.edu.in",
            "website": "https://www.stellarscience.edu.in",
            "established_year": 2015,
            "description": "Leading research institution in basic sciences."
        }
    )

    # Stream 5.1: B.Sc. Physics for Stellar
    stream5_1, _ = Stream.objects.get_or_create(
        college=college5,
        name="B.Sc. Physics",
        defaults={
            "stream_type": "SCIENCE",
            "duration_years": 3,
            "total_seats": 60,
            "fees_per_year": 70000.00,
            "eligibility_criteria": "10+2 with PCM",
            "is_active": True,
            "description": "Comprehensive physics curriculum with research opportunities."
        }
    )

    # CutOffs for Stream 5.1 (Stellar B.Sc Physics)
    cutoffs_stream5_1 = [
        {"year": 2024, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 80.00, "available_seats": 7, "closing_rank": 10000},
        {"year": 2024, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 75.00, "available_seats": 10, "closing_rank": 15000},
        {"year": 2024, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 8, "closing_rank": 20000},
        {"year": 2024, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 6, "closing_rank": 25000},
        {"year": 2024, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 70.00, "available_seats": 5, "closing_rank": 18000},
        {"year": 2023, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 78.00, "available_seats": 8, "closing_rank": 12000},
        {"year": 2023, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 73.00, "available_seats": 12, "closing_rank": 18000},
        {"year": 2023, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 63.00, "available_seats": 10, "closing_rank": 22000},
        {"year": 2023, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 58.00, "available_seats": 8, "closing_rank": 28000},
        {"year": 2023, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 68.00, "available_seats": 6, "closing_rank": 20000},
        {"year": 2022, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 75.00, "available_seats": 10, "closing_rank": 15000},
        {"year": 2022, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 70.00, "available_seats": 15, "closing_rank": 20000},
        {"year": 2022, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 12, "closing_rank": 25000},
        {"year": 2022, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 10, "closing_rank": 30000},
        {"year": 2022, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 8, "closing_rank": 22000},
    ]
    for cutoff_data in cutoffs_stream5_1:
        CutOff.objects.update_or_create(stream=stream5_1, year=cutoff_data["year"], category=cutoff_data["category"], cutoff_type=cutoff_data["cutoff_type"], defaults=cutoff_data)

    # College 6: Delta Institute of Technology
    college6, _ = College.objects.get_or_create(
        code="DIT601",
        defaults={
            "name": "Delta Institute of Technology",
            "address": "Innovation Valley, Hyderabad, Telangana, 500081",
            "phone": "+91-9876123450",
            "email": "info@deltaitech.edu.in",
            "website": "https://www.deltaitech.edu.in",
            "established_year": 2008,
            "description": "Focus on emerging technologies and software development."
        }
    )

    # Stream 6.1: B.Tech in Information Technology for Delta
    stream6_1, _ = Stream.objects.get_or_create(
        college=college6,
        name="B.Tech in Information Technology",
        defaults={
            "stream_type": "ENGINEERING",
            "duration_years": 4,
            "total_seats": 150,
            "fees_per_year": 130000.00,
            "eligibility_criteria": "10+2 with PCM, JEE Main score",
            "is_active": True,
            "description": "Specialization in network security and data management."
        }
    )

    # CutOffs for Stream 6.1 (Delta B.Tech IT)
    cutoffs_stream6_1 = [
        {"year": 2024, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 72.00, "available_seats": 18, "closing_rank": 28000},
        {"year": 2024, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 25, "closing_rank": 35000},
        {"year": 2024, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 20, "closing_rank": 45000},
        {"year": 2024, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 50.00, "available_seats": 15, "closing_rank": 50000},
        {"year": 2024, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 12, "closing_rank": 40000},
        {"year": 2023, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 70.00, "available_seats": 20, "closing_rank": 30000},
        {"year": 2023, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 63.00, "available_seats": 28, "closing_rank": 38000},
        {"year": 2023, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 53.00, "available_seats": 22, "closing_rank": 48000},
        {"year": 2023, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 48.00, "available_seats": 18, "closing_rank": 53000},
        {"year": 2023, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 58.00, "available_seats": 15, "closing_rank": 43000},
        {"year": 2022, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 68.00, "available_seats": 22, "closing_rank": 32000},
        {"year": 2022, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 30, "closing_rank": 40000},
        {"year": 2022, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 50.00, "available_seats": 25, "closing_rank": 50000},
        {"year": 2022, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 45.00, "available_seats": 20, "closing_rank": 55000},
        {"year": 2022, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 18, "closing_rank": 45000},
    ]
    for cutoff_data in cutoffs_stream6_1:
        CutOff.objects.update_or_create(stream=stream6_1, year=cutoff_data["year"], category=cutoff_data["category"], cutoff_type=cutoff_data["cutoff_type"], defaults=cutoff_data)

    # College 7: Gamma College of Commerce
    college7, _ = College.objects.get_or_create(
        code="GCC701",
        defaults={
            "name": "Gamma College of Commerce",
            "address": "Financial District, Chennai, Tamil Nadu, 600001",
            "phone": "+91-9123456780",
            "email": "admissions@gammacommerce.edu",
            "website": "https://www.gammacommerce.edu",
            "established_year": 1995,
            "description": "Renowned for its strong commerce and accounting programs."
        }
    )

    # Stream 7.1: B.Com in Accounting and Finance for Gamma
    stream7_1, _ = Stream.objects.get_or_create(
        college=college7,
        name="B.Com in Accounting and Finance",
        defaults={
            "stream_type": "COMMERCE",
            "duration_years": 3,
            "total_seats": 100,
            "fees_per_year": 80000.00,
            "eligibility_criteria": "10+2 in Commerce stream",
            "is_active": True,
            "description": "Specialization in corporate finance and taxation."
        }
    )

    # CutOffs for Stream 7.1 (Gamma B.Com)
    cutoffs_stream7_1 = [
        {"year": 2024, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 62.00, "available_seats": 12, "closing_rank": 38000},
        {"year": 2024, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 18, "closing_rank": 45000},
        {"year": 2024, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 45.00, "available_seats": 15, "closing_rank": 55000},
        {"year": 2024, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 40.00, "available_seats": 12, "closing_rank": 60000},
        {"year": 2024, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 50.00, "available_seats": 10, "closing_rank": 50000},
        {"year": 2023, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 15, "closing_rank": 40000},
        {"year": 2023, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 53.00, "available_seats": 20, "closing_rank": 48000},
        {"year": 2023, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 43.00, "available_seats": 18, "closing_rank": 58000},
        {"year": 2023, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 38.00, "available_seats": 15, "closing_rank": 63000},
        {"year": 2023, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 48.00, "available_seats": 12, "closing_rank": 53000},
        {"year": 2022, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 58.00, "available_seats": 18, "closing_rank": 42000},
        {"year": 2022, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 50.00, "available_seats": 22, "closing_rank": 50000},
        {"year": 2022, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 40.00, "available_seats": 20, "closing_rank": 60000},
        {"year": 2022, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 35.00, "available_seats": 18, "closing_rank": 65000},
        {"year": 2022, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 45.00, "available_seats": 15, "closing_rank": 55000},
    ]
    for cutoff_data in cutoffs_stream7_1:
        CutOff.objects.update_or_create(stream=stream7_1, year=cutoff_data["year"], category=cutoff_data["category"], cutoff_type=cutoff_data["cutoff_type"], defaults=cutoff_data)

    # College 8: Epsilon School of Humanities
    college8, _ = College.objects.get_or_create(
        code="ESH801",
        defaults={
            "name": "Epsilon School of Humanities",
            "address": "University Road, Kolkata, West Bengal, 700073",
            "phone": "+91-9345678901",
            "email": "admissions@epsilonhumanities.edu",
            "website": "https://www.epsilonhumanities.edu",
            "established_year": 2000,
            "description": "Offering diverse programs in social sciences and literature."
        }
    )

    # Stream 8.1: MA in Sociology for Epsilon
    stream8_1, _ = Stream.objects.get_or_create(
        college=college8,
        name="MA in Sociology",
        defaults={
            "stream_type": "ARTS",
            "duration_years": 2,
            "total_seats": 50,
            "fees_per_year": 50000.00,
            "eligibility_criteria": "Bachelor's degree in any discipline",
            "is_active": True,
            "description": "Advanced study of societal structures and human behavior."
        }
    )

    # CutOffs for Stream 8.1 (Epsilon MA Sociology)
    cutoffs_stream8_1 = [
        {"year": 2024, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 75.00, "available_seats": 6, "closing_rank": 20000},
        {"year": 2024, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 68.00, "available_seats": 10, "closing_rank": 28000},
        {"year": 2024, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 8, "closing_rank": 35000},
        {"year": 2024, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 6, "closing_rank": 40000},
        {"year": 2024, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 5, "closing_rank": 30000},
        {"year": 2023, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 73.00, "available_seats": 8, "closing_rank": 22000},
        {"year": 2023, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 12, "closing_rank": 30000},
        {"year": 2023, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 58.00, "available_seats": 10, "closing_rank": 38000},
        {"year": 2023, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 53.00, "available_seats": 8, "closing_rank": 42000},
        {"year": 2023, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 63.00, "available_seats": 7, "closing_rank": 32000},
        {"year": 2022, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 70.00, "available_seats": 10, "closing_rank": 25000},
        {"year": 2022, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 62.00, "available_seats": 15, "closing_rank": 33000},
        {"year": 2022, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 12, "closing_rank": 40000},
        {"year": 2022, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 50.00, "available_seats": 10, "closing_rank": 45000},
        {"year": 2022, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 8, "closing_rank": 35000},
    ]
    for cutoff_data in cutoffs_stream8_1:
        CutOff.objects.update_or_create(stream=stream8_1, year=cutoff_data["year"], category=cutoff_data["category"], cutoff_type=cutoff_data["cutoff_type"], defaults=cutoff_data)

    # Add data for Arya Group of Colleges, Jaipur
    college9, _ = College.objects.get_or_create(
        code="AGC901",
        defaults={
            "name": "Arya Group of Colleges, Jaipur",
            "address": "SP-42, Riico Industrial Area, Kukas, Jaipur, Rajasthan 302028",
            "phone": "+91-141-2622515",
            "email": "info@aryacollege.in",
            "website": "https://www.aryacollege.in",
            "established_year": 1999,
            "description": "A group of technical and management colleges in Jaipur."
        }
    )

    # Stream for Arya Group of Colleges, Jaipur: Bachelor of Arts (B.A.)
    stream9_1, _ = Stream.objects.get_or_create(
        college=college9,
        name="Bachelor of Arts (B.A.)",
        defaults={
            "stream_type": "ARTS",
            "duration_years": 3,
            "total_seats": 100,
            "fees_per_year": 50000.00,
            "eligibility_criteria": "10+2 in any stream",
            "is_active": True,
            "description": "General Bachelor of Arts program."
        }
    )

    # CutOffs for Stream 9.1 (Arya BA)
    cutoffs_stream9_1 = [
        {"year": 2024, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 10, "closing_rank": 30000},
        {"year": 2024, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 58.00, "available_seats": 15, "closing_rank": 38000},
        {"year": 2024, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 50.00, "available_seats": 12, "closing_rank": 45000},
        {"year": 2024, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 45.00, "available_seats": 10, "closing_rank": 50000},
        {"year": 2024, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 8, "closing_rank": 40000},
        {"year": 2023, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 63.00, "available_seats": 12, "closing_rank": 32000},
        {"year": 2023, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 56.00, "available_seats": 18, "closing_rank": 40000},
        {"year": 2023, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 48.00, "available_seats": 15, "closing_rank": 48000},
        {"year": 2023, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 43.00, "available_seats": 12, "closing_rank": 53000},
        {"year": 2023, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 53.00, "available_seats": 10, "closing_rank": 42000},
        {"year": 2022, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 15, "closing_rank": 35000},
        {"year": 2022, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 53.00, "available_seats": 20, "closing_rank": 43000},
        {"year": 2022, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 45.00, "available_seats": 18, "closing_rank": 50000},
        {"year": 2022, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 40.00, "available_seats": 15, "closing_rank": 55000},
        {"year": 2022, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 50.00, "available_seats": 12, "closing_rank": 45000},
    ]
    for cutoff_data in cutoffs_stream9_1:
        CutOff.objects.update_or_create(stream=stream9_1, year=cutoff_data["year"], category=cutoff_data["category"], cutoff_type=cutoff_data["cutoff_type"], defaults=cutoff_data)

    # Add data for Osmania University
    college10, _ = College.objects.get_or_create(
        code="OU1001",
        defaults={
            "name": "Osmania University",
            "address": "Osmania University Main Rd, Hyderabad, Telangana 500007",
            "phone": "+91-40-27682363",
            "email": "info@osmania.ac.in",
            "website": "https://www.osmania.ac.in",
            "established_year": 1918,
            "description": "A public state university in Hyderabad."
        }
    )

    # Stream for Osmania University: Bachelor of Science (B.Sc.)
    stream10_1, _ = Stream.objects.get_or_create(
        college=college10,
        name="Bachelor of Science (B.Sc.)",
        defaults={
            "stream_type": "SCIENCE",
            "duration_years": 3,
            "total_seats": 120,
            "fees_per_year": 60000.00,
            "eligibility_criteria": "10+2 in Science stream",
            "is_active": True,
            "description": "General Bachelor of Science program."
        }
    )

    # CutOffs for Stream 10.1 (Osmania B.Sc)
    cutoffs_stream10_1 = [
        {"year": 2024, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 78.00, "available_seats": 15, "closing_rank": 10000},
        {"year": 2024, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 70.00, "available_seats": 20, "closing_rank": 15000},
        {"year": 2024, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 18, "closing_rank": 20000},
        {"year": 2024, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 15, "closing_rank": 25000},
        {"year": 2024, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 12, "closing_rank": 18000},
        {"year": 2023, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 76.00, "available_seats": 18, "closing_rank": 12000},
        {"year": 2023, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 68.00, "available_seats": 22, "closing_rank": 17000},
        {"year": 2023, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 58.00, "available_seats": 20, "closing_rank": 22000},
        {"year": 2023, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 53.00, "available_seats": 18, "closing_rank": 27000},
        {"year": 2023, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 63.00, "available_seats": 15, "closing_rank": 20000},
        {"year": 2022, "category": "GENERAL", "cutoff_type": "CURRENT_1", "cutoff_percentage": 74.00, "available_seats": 20, "closing_rank": 15000},
        {"year": 2022, "category": "OBC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 65.00, "available_seats": 25, "closing_rank": 20000},
        {"year": 2022, "category": "SC", "cutoff_type": "CURRENT_1", "cutoff_percentage": 55.00, "available_seats": 22, "closing_rank": 25000},
        {"year": 2022, "category": "ST", "cutoff_type": "CURRENT_1", "cutoff_percentage": 50.00, "available_seats": 20, "closing_rank": 30000},
        {"year": 2022, "category": "EWS", "cutoff_type": "CURRENT_1", "cutoff_percentage": 60.00, "available_seats": 18, "closing_rank": 22000},
    ]
    for cutoff_data in cutoffs_stream10_1:
        CutOff.objects.update_or_create(stream=stream10_1, year=cutoff_data["year"], category=cutoff_data["category"], cutoff_type=cutoff_data["cutoff_type"], defaults=cutoff_data)

    print("\nFinished adding/updating data.")

if __name__ == "__main__":
    add_college_data() 