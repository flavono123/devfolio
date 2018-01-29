from django import forms
from django.contrib.auth.forms import UserCreationForm, get_user_model


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
        widgets = {
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

