from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from BaseGroup.forms import BaseGroupForm

#create new group view
@login_required()
def new_group(request):
    #if request is a POST, we attempt to save the form
    if request.method == "POST":
        form = BaseGroupForm(request.POST)
        if form.is_valid():
            form.save()

            #get the saved group
    #or else we serve up a blank form
    else:
        form = BaseGroupForm()

    return render(request, "basic_group/group_form.html", {'form':form})