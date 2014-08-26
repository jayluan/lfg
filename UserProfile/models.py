from django.db import models
from django.contrib.auth.models import User
from timezone_field import TimeZoneField
from pytz import all_timezones

# Create your models here.
class UserProfile(models.Model):
    picture = models.ImageField("Profile Image", upload_to="profile_picture", blank=True, null=True)
    user = models.OneToOneField(User)
    languages = models.TextField()
    about = models.TextField()
    site = models.TextField()
    timezone = TimeZoneField(default='US/Pacific')
    #lazy evaluation 'LookingForGroupMain.BasicGroup' means look in LookingForGroupMain and find model BasicGroup
    groups = models.ForeignKey('BaseGroup.BaseGroup', blank=True, null=True)

    def __unicode__(self):
        return self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])