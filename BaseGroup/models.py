from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseGroup(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    date_created = models.DateTimeField()
    date_action = models.DateTimeField()
    users = models.ForeignKey('UserProfile.UserProfile')
    group_size = models.IntegerField()         #max number of users

    def __unicode__(self):
        return self.name
