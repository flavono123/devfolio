from django import forms

from .models import Resume, Career, Education, Award, Link


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'


class CareerForm(forms.ModelForm):
    resume = forms.ModelChoiceField(queryset=Resume.objects.all(), widget=forms.Select(attrs={
        'class': 'form-class',
    }))
    since = forms.DateField(input_formats=['%Y.%m'], widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '0000.0',
    }))
    until = forms.DateField(input_formats=['%Y.%m'], widget=forms.TextInput(attrs={
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
