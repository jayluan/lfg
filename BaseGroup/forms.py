from django.forms import ModelForm, DateField, TimeField
from BaseGroup.models import BaseGroup
from django.utils import timezone
from datetime import datetime
import pytz



class BaseGroupForm(ModelForm):
    valid_time_formats = ['%H:%M', '%I:%M%p', '%I:%M %p']
    due_date = DateField(label='Event Date', help_text="MM/DD/YYYY")
    due_time = TimeField(label='Event Time', input_formats=valid_time_formats, help_text="ex: 10:30am")

    #define custom label for the "name" field
    def __init__(self, *args, **kwargs):
        super(BaseGroupForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Group Name'

    class Meta:
        model = BaseGroup
        fields = ['name', 'description', 'due_date', 'due_time', 'group_size']

    #custom save routine to automaitcally handle creation date saving and the combining
    #of due_date and due_time into the actual date_action field
    def save(self, commit=True):
        groupModel = super(BaseGroupForm, self).save(commit=False)

        if commit is True:
            groupModel.date_created = timezone.now()
            d = datetime.combine(self.cleaned_data['due_date'],
                                 self.cleaned_data['due_time'])
            user_timezone = groupModel.owner.timezone
            if user_timezone.zone in pytz.all_timezones:
                tz = pytz.timezone(user_timezone.zone)
            else:
                raise Exception("BaseGroup save() error: owner timezone not in list of timezones")

            groupModel.date_action = toUTCc(d, tz)

            groupModel = super(BaseGroupForm, self).save(commit=commit)

        return groupModel


#helper function to convert time to UTC
def toUTCc(d, tz):
    return tz.normalize(tz.localize(d)).astimezone(pytz.utc)