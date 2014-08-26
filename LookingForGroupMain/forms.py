from registration.forms import RegistrationForm
from django.forms import ModelForm
from django import forms
import pytz

#custom registration form with required first name and optional last name
class CustomRegistrationForm(RegistrationForm):
    first_name = forms.CharField(max_length=256, label="First Name:", error_messages={'invalid':"Please enter your first name"})
    last_name = forms.CharField(max_length=256, label="Last Name (optional):", required=False)
    timezone = forms.ChoiceField(choices=[(x, x) for x in pytz.common_timezones])

