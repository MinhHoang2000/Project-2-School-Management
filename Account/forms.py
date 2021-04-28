from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password_1 = forms.CharField(widget=forms.PasswordInput())
    new_password_2 = forms.CharField(widget=forms.PasswordInput())