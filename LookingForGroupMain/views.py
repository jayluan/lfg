from django.contrib.auth.models import User
from BaseGroup.models import BaseGroup
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from LookingForGroupMain.forms import CustomRegistrationForm


# Create your views here.
def index(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return login(request, template_name='main.html', extra_context=context)

def user_detail(request, user):
    user = User.objects.get(username=user)
    context = {'user':user}
    return render(request, 'user/details.html', context)

def registration_view(request):
    user_signup_form = CustomRegistrationForm()
    context = {'form':user_signup_form}
    return render(request, 'registration/registration_form.html', context)

def logout_view(request):
    logout(request)
    return index(request)
    #Redirect to success page


def CreateGroup(request):
    if(request.user.is_authenticated()):
        userProfile = request.user.UserProfile
        context = {'user':userProfile}
        return render(request, 'group/create.html', context)
    else:
        return login(request)