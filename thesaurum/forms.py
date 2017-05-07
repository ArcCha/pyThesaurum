from registration.forms import RegistrationForm
from django import forms


class ExtendedRegistrationForm(RegistrationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'label': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'label': 'last_name'}))