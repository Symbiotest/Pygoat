from django import forms
from .models import InsecureUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = InsecureUser
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
