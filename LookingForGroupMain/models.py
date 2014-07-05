from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    languages = models.TextField()
    about = models.TextField()
    site = models.TextField()

class BasicGroup(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    date_created = models.DateTimeField()
    date_action = models.DateTimeField()
    users = models.OneToOneField(UserProfile)  #list of users
    group_size = models.IntegerField()         #max number of users
