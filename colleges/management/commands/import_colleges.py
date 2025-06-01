from django.core.management.base import BaseCommand
from colleges.models import College, Stream
from decimal import Decimal


class Command(BaseCommand):
    help = 'Import colleges and streams data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting college data import...'))
        
        # Import Osmania University
        self.import_osmania_university()
        
        # Import Arya Group of Colleges
        self.import_arya_college()
        
        self.stdout.write(self.style.SUCCESS('Successfully imported all college data!'))

    def import_osmania_university(self):
        self.stdout.write('Importing Osmania University...')
        
        # Create or update Osmania University
        college, created = College.objects.get_or_create(
            code='OUHYD',
            defaults={
                'name': 'Osmania University',
                'address': 'Administrative Building, Osmania University Campus, Hyderabad - 500007, Telangana, India',
                'phone': '+91-40-2768-2444',
                'email': 'registrar@osmania.ac.in',
                'website': 'https://www.osmania.ac.in',
                'established_year': 1918,
                'description': 'Osmania University is the seventh oldest in India and the first to be established in the erstwhile princely state of Hyderabad. It has a sprawling campus of 500 hectares and offers a wide range of undergraduate and postgraduate programs across various disciplines.'
            }
        )
        
        if created:
            self.stdout.write(f'Created college: {college.name}')
        else:
            self.stdout.write(f'College already exists: {college.name}')
        
        # Import streams for Osmania University
        streams_data = [
            {
                'name': 'Bachelor of Science (B.Sc.)',
                'stream_type': 'SCIENCE',
                'duration_years': 3,
                'total_seats': 500,  # Varies by specialization - using estimate
                'fees_per_year': Decimal('10000'),
                'eligibility_criteria': '10+2 with relevant science subjects',
                'description': 'Undergraduate program in various science disciplines.',
                'is_active': True
            },
            {
                'name': 'Bachelor of Arts (B.A.)',
                'stream_type': 'ARTS',
                'duration_years': 3,
                'total_seats': 600,  # Varies by specialization - using estimate
                'fees_per_year': Decimal('8000'),
                'eligibility_criteria': '10+2 in any stream',
                'description': 'Undergraduate program in various arts disciplines.',
                'is_active': True
            },
            {
                'name': 'Bachelor of Commerce (B.Com.)',
                'stream_type': 'COMMERCE',
                'duration_years': 3,
                'total_seats': 400,  # Varies by specialization - using estimate
                'fees_per_year': Decimal('9000'),
                'eligibility_criteria': '10+2 with commerce subjects',
                'description': 'Undergraduate program focusing on commerce and finance.',
                'is_active': True
            },
            {
                'name': 'Bachelor of Engineering (B.E.)',
                'stream_type': 'ENGINEERING',
                'duration_years': 4,
                'total_seats': 300,  # Varies by department - using estimate
                'fees_per_year': Decimal('25000'),
                'eligibility_criteria': '10+2 with Physics, Chemistry, and Mathematics; entrance exam',
                'description': 'Undergraduate engineering program across various disciplines.',
                'is_active': True
            },
            {
                'name': 'Bachelor of Laws (LL.B.)',
                'stream_type': 'LAW',
                'duration_years': 3,
                'total_seats': 200,  # Varies - using estimate
                'fees_per_year': Decimal('12000'),
                'eligibility_criteria': 'Graduation in any discipline',
                'description': 'Undergraduate program in legal studies.',
                'is_active': True
            }
        ]
        
        for stream_data in streams_data:
            stream, created = Stream.objects.get_or_create(
                college=college,
                name=stream_data['name'],
                defaults=stream_data
            )
            if created:
                self.stdout.write(f'  Created stream: {stream.name}')
            else:
                self.stdout.write(f'  Stream already exists: {stream.name}')

    def import_arya_college(self):
        self.stdout.write('Importing Arya Group of Colleges...')
        
        # Create or update Arya Group of Colleges
        college, created = College.objects.get_or_create(
            code='ARYAJPR',
            defaults={
                'name': 'Arya Group of Colleges, Jaipur',
                'address': 'SP-40, RIICO Industrial Area, Kukas, Delhi Road, Jaipur - 302028, Rajasthan, India',
                'phone': '+91-141-2820700',
                'email': 'admission@aryacollege.org',
                'website': 'https://www.aryacollege.org',
                'established_year': 2000,
                'description': 'Arya Group of Colleges is a group of private engineering colleges in Jaipur, Rajasthan, focusing on higher education and research in engineering and technology. It offers undergraduate and postgraduate programs in various disciplines such as engineering, management, computer applications, and commerce.'
            }
        )
        
        if created:
            self.stdout.write(f'Created college: {college.name}')
        else:
            self.stdout.write(f'College already exists: {college.name}')
        
        # Import streams for Arya Group of Colleges
        streams_data = [
            {
                'name': 'Bachelor of Technology (B.Tech) in Computer Science and Engineering',
                'stream_type': 'ENGINEERING',
                'duration_years': 4,
                'total_seats': 480,
                'fees_per_year': Decimal('85000'),
                'eligibility_criteria': '10+2 with Physics and Mathematics; entrance exam',
                'description': 'Undergraduate program focusing on computer science and engineering principles.',
                'is_active': True
            },
            {
                'name': 'Bachelor of Business Administration (BBA)',
                'stream_type': 'MANAGEMENT',
                'duration_years': 3,
                'total_seats': 120,
                'fees_per_year': Decimal('60000'),
                'eligibility_criteria': '10+2 in any stream',
                'description': 'Undergraduate program in business administration.',
                'is_active': True
            },
            {
                'name': 'Bachelor of Pharmacy (B.Pharm)',
                'stream_type': 'MEDICAL',
                'duration_years': 4,
                'total_seats': 100,
                'fees_per_year': Decimal('90000'),
                'eligibility_criteria': '10+2 with Physics, Chemistry, and Biology/Mathematics',
                'description': 'Undergraduate program in pharmaceutical sciences.',
                'is_active': True
            },
            {
                'name': 'Bachelor of Arts (B.A.)',
                'stream_type': 'ARTS',
                'duration_years': 3,
                'total_seats': 60,
                'fees_per_year': Decimal('30000'),
                'eligibility_criteria': '10+2 in any stream',
                'description': 'Undergraduate program in various arts disciplines.',
                'is_active': True
            },
            {
                'name': 'Master of Business Administration (MBA)',
                'stream_type': 'MANAGEMENT',
                'duration_years': 2,
                'total_seats': 60,
                'fees_per_year': Decimal('70000'),
                'eligibility_criteria': 'Graduation in any discipline; entrance exam',
                'description': 'Postgraduate program in business administration.',
                'is_active': True
            }
        ]
        
        for stream_data in streams_data:
            stream, created = Stream.objects.get_or_create(
                college=college,
                name=stream_data['name'],
                defaults=stream_data
            )
            if created:
                self.stdout.write(f'  Created stream: {stream.name}')
            else:
                self.stdout.write(f'  Stream already exists: {stream.name}')
