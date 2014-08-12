from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from BaseGroup.forms import BaseGroupForm
from UserProfile.models import UserProfile
from datetime import datetime
from django.http import HttpResponseRedirect

#create new group view
@login_required()
def new_group(request):
    #if request is a POST, we attempt to save the form
    if request.method == "POST":
        form = BaseGroupForm(request.POST)
        if form.is_valid():
            groupModel = form.save(commit=False) #get the group model under the form

            #lookup user
            try:
                currentUserProfile = UserProfile.objects.get(user=request.user)
                groupModel.date_created = datetime.now()    #creation time
                groupModel.owner = currentUserProfile       #owner

                #combine date and time fields
                groupModel.date_action = datetime.combine(form.date, form.time)
                form.save()
                return HttpResponseRedirect('/')
            except:
                form= BaseGroupForm()   #something went wrong, so give them the default form

    #or else we serve up a blank form
    else:
        form = BaseGroupForm()

    return render(request, "basic_group/group_form.html", {'form':form})