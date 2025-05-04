# usermodule/forms.py

from django import forms
from .models import Account

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput()}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
