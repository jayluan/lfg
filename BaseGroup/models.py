from django.db import models
from django.contrib.auth.models import User
from UserProfile.models import UserProfile

# Create your models here.
class BaseGroup(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    date_created = models.DateTimeField()
    date_action = models.DateTimeField()

    '''query through UserProfile using the following:
        p = UserProfile.objects.get(user__username='jay')
        g = p.groups.get(name='test8')
    '''
    owner = models.ForeignKey(UserProfile, related_name='groups', null=True)
    users = models.ManyToManyField(UserProfile, related_name='member_of', null=True)
    group_size = models.PositiveIntegerField()         #max number of users
    is_active = models.BooleanField(default=True)


    def __unicode__(self):
        return self.name
