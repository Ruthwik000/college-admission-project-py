from django import forms
from .models import UserProfile, StudentProfile
from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'date_of_birth', 'gender', 'address', 'profile_picture']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your address'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['student_id', 'father_name', 'mother_name', 'guardian_phone', 
                 'previous_school', 'board', 'passing_year', 'percentage', 'category']
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your student ID'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter father\'s name'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mother\'s name'}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter guardian\'s phone number'}),
            'previous_school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your previous school name'}),
            'board': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your board name'}),
            'passing_year': forms.NumberInput(attrs={'class': 'form-control', 'min': 2000, 'max': 2030}),
            'percentage': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100, 'step': 0.01}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_guardian_phone(self):
        phone = self.cleaned_data.get('guardian_phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone

    def clean_percentage(self):
        percentage = self.cleaned_data.get('percentage')
        if percentage is not None:
            if percentage < 0 or percentage > 100:
                raise forms.ValidationError('Percentage must be between 0 and 100.')
        return percentage
