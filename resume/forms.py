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

