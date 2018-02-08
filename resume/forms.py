from django import forms
from django.utils import timezone
from django.forms import ValidationError

from .models import Resume, Career, Education, Award, Link


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone number ex) 010-0000-0000' 
            }),
            'about_me': forms.Textarea(attrs={
                'rows': 5,    
                'placeholder': 'Make your resume stand out with a simple self introduction. (3-5 lines recommended)',
            }),
        }


class CareerForm(forms.ModelForm):
    since = forms.DateField(input_formats=['%Y.%m'], widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '0000.0',
    }))
    until = forms.DateField(input_formats=['%Y.%m'], required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '0000.0',
    }))

    class Meta:
        model = Career
        fields = '__all__'
        exclude = ('resume',)
        widgets = {
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name',
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task/Position',
            }),
            'achievement': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Major Achievement',
            }),
            'currently_employed': forms.CheckboxInput(attrs={
                'class': 'custom-control-input form-control',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['currently_employed'] == True:
            cleaned_data['until'] = timezone.now().date()
        # Check since < until
        if cleaned_data['since'] >= cleaned_data['until']:
            raise ValidationError('"Until" should be later than "Since"')


class EducationForm(forms.ModelForm):
    since = forms.DateField(input_formats=['%Y.%m'], widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '0000.0',
    }))
    until = forms.DateField(input_formats=['%Y.%m'], required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '0000.0',
    }))
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ('resume',)
        widgets = {
            'school_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'School Name',
            }),
            'major': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Major',
            }),
            'research_content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Compeletion Courses or Research Content'
            }),
            'currently_attending': forms.CheckboxInput(attrs={
                'class': 'custom-control-input form-control',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['currently_attending'] == True:
            cleaned_data['until'] = timezone.now().date()
        # Check since < until
        if cleaned_data['since'] >= cleaned_data['until']:
            raise ValidationError('"Until" should be later than "Since"')

class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'
        widgets = {
            'activity_name': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
            'at': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'github': forms.TextInput(attrs={'class': 'form-control'}),
            'stackoverflow': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'}),
            'google_plus': forms.TextInput(attrs={'class': 'form-control'}),
            'blog': forms.URLInput(attrs={'class': 'form-control'}),
                
        }
