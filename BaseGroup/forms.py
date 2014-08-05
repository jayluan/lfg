from django.forms import ModelForm
from django import forms
from BaseGroup.models import BaseGroup

class BaseGroupForm(ModelForm):
    class Meta:
        model = BaseGroup
        fields = ['name', 'description', 'date_action', 'group_size']

