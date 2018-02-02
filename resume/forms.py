from django import forms
from django.utils import timezone
from django.forms import ValidationError

from .models import Resume, Career, Education, Award, Link


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'


class CareerForm(forms.ModelForm):
    resume = forms.ModelChoiceField(queryset=Resume.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
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
        widgets = {
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name',
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task/Position',
            }),
            'achivement': forms.Textarea(attrs={
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
    class Meta:
        model = Education
        fields = '__all__'
        widgets = {
            'school_name': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
            'research_content': forms.Textarea(attrs={'class': 'form-control'}),
            'since': forms.TextInput(attrs={'class': 'form-control'}),
            'until': forms.TextInput(attrs={'class': 'form-control'}),
            'currently_employed': forms.CheckboxInput(attrs={'class': 'custom-control-input'}),
        }

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
