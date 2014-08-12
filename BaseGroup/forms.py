from django.forms import ModelForm
from BaseGroup.models import BaseGroup
from django.db import models

class BaseGroupForm(ModelForm):
    dueDate = models.DateField()
    dueTime = models.TimeField()

    class Meta:
        model = BaseGroup
        fields = ['dueDate', 'dueTime', 'name', 'description', 'date_action', 'group_size']