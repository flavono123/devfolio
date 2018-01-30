from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={
        'id': 'inputEmail',
        'class': 'form-control',
        'placeholder': 'Email',
        'autofocus': True,
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'inputPassword',
        'class': 'form-control',
        'placeholder': 'Password',
    }))

    
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #TODO: make the first and the last name to essential fields / blank=False
        fields =('email', 'first_name', 'last_name') + UserCreationForm.Meta.fields 
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
            }),
            'username': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
            # TODO: placeholders for password and confirm
            'email': forms.HiddenInput,     
        }

    def save(self, commit=True):
        user = super().save(False)
        user.email = user.username
        user = super().save()

        return user

