from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from BaseGroup.forms import BaseGroupForm
from BaseGroup.models import BaseGroup
from django.http import HttpResponseRedirect
from django.http import Http404

#create new group view
@login_required()
def new_group(request):
    #if request is a POST, we attempt to save the form
    if request.method == "POST":
        form = BaseGroupForm(request.POST)
        if form.is_valid():
            groupModel = form.save(commit=False) #get the group model under the form

            #lookup user to make sure he/she exists
            try:
                groupModel.owner = request.user       #owner
                groupModel = form.save()
                redirectUrl = '/groups/view/'+str(groupModel.id)
                return HttpResponseRedirect(redirectUrl)
            except Exception, e:
                print str(e)
                form= BaseGroupForm()   #something went wrong, so give them the default form

    #or else we serve up a blank form
    else:
        form = BaseGroupForm()

    return render(request, "basic_group/group_form.html", {'form':form})


#view for an arbitrary group
@login_required()
def view_group(request, group_id):
    owner = None
    try:
        baseGroup = BaseGroup.objects.get(id=group_id)
        if(request.user == baseGroup.owner):
            owner = baseGroup.owner

    #raise 404 if group can't be found
    except BaseGroup.DoesNotExist:
        raise Http404

    return render(request, "basic_group/group_main.html", {'group':baseGroup, 'owner':owner})