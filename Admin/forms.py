from django import forms
from django.forms.fields import BooleanField, CharField
from django.forms.widgets import CheckboxInput, PasswordInput

class RegisterForm(forms.Form):
    username = CharField()
    password = CharField(widget=forms.PasswordInput())
    is_admin = BooleanField(widget=forms.CheckboxInput(), required=False)