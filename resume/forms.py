from django import forms

from .models import Resume, Career


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = '__all__'
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'since': forms.TextInput(attrs={'class': 'form-control'}),
            'until': forms.TextInput(attrs={'class': 'form-control'}),
            'currently_employed': forms.CheckboxInput(attrs={'class': 'custom-control-input'}),
        }
