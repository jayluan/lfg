from django.db import models
from registration.signals import user_registered
from UserProfile.models import UserProfile


#callback and connection for creating a new user profile after someone registers
def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user=user)
    user.first_name = request.POST["first_name"]
    user.last_name = request.POST["last_name"]
    user.save()
    profile.save()

#connect all signals
user_registered.connect(user_registered_callback)