from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseGroup(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    date_created = models.DateTimeField()
    date_action = models.DateTimeField()
    owner = models.OneToOneField('UserProfile.UserProfile', related_name='creator', null=True)
    users = models.ForeignKey('UserProfile.UserProfile')
    group_size = models.PositiveIntegerField()         #max number of users

    def __unicode__(self):
        return self.name
