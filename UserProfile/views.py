from UserProfile.models import UserProfile
from UserProfile.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.shortcuts import HttpResponseRedirect
from lfg_irl.settings import MEDIA_ROOT

from os.path import join
from PIL import Image as PImage

from django.core.context_processors import csrf
def add_csrf(request, **kwargs):
    d=dict(user=request.user, **kwargs)
    d.update(csrf(request))
    return d


@login_required
def account_view(request):
    return render(request, 'userAdmin/account_home.html')

#Edit user profile
@login_required
def profile(request, pk):
    #edit user profile
    profile = UserProfile.objects.get(user__username=pk)
    img = None

    if request.method == "POST":
        pf = UserProfileForm(request.POST, request.FILES, instance=profile)
        if pf.is_valid():
            pf.save()
            #resize img and save
            imfn = join(MEDIA_ROOT, profile.user.username)
            im = PImage.open(imfn)
            im.thumbnail((160,160), PImage.ANTIALIAS)
            im.save(imfn, "JPEG")

    else:
        pf = UserProfileForm(instance=profile)

    if profile.picture:
        img = "/media/"+profile.user.username

    return render_to_response("user/profile.html", add_csrf(request, pf=pf, img=img))

@login_required
def user_profile(request):
    #edit user profile
    img = None

    if request.method == "POST":

        # imfn = join(MEDIA_ROOT, request.user.username + ".png")
        # #im = pf.cleaned_data['picture'].open()
        # im = PImage.open(request.FILES['picture'])
        # im.thumbnail((160,160), PImage.ANTIALIAS)
        #
        # try:
        #     im.save(imfn)
        #     request.FILES['picture'] = imfn
        # except Exception as e:
        #     print '%s (%s)' % (e.message, type(e))

        pf = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if pf.is_valid():
            #resize img and save
#            imfn = join(MEDIA_ROOT, request.user.username + ".png")
            #im = pf.cleaned_data['picture'].open()
#            im = PImage.open(request.FILES['picture'])
#            im.thumbnail((160,160), PImage.ANTIALIAS)

#            try:
#                im.save(imfn)
#            except Exception as e:
#                print '%s (%s)' % (e.message, type(e))
#            pf.cleaned_data['picture'].path = imfn

            try:
                pf.save()
                return HttpResponseRedirect('/accounts/profile/')
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
                return render_to_response("user/profile.html", add_csrf(request, pf=pf))



    else:
        pf = UserProfileForm(instance=request.user.profile)
        return render_to_response("user/profile.html", add_csrf(request, pf=pf, user_profile=request.user.profile))
    # if request.user.profile.picture:
    #     img = join(MEDIA_ROOT,request.user.username+".png")

