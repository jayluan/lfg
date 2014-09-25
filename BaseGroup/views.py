from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from BaseGroup.forms import BaseGroupForm
from BaseGroup.models import BaseGroup
from BaseGroup.table import  GroupTable
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_tables2   import RequestConfig

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
                groupModel.owner = request.user.userprofile       #owner
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
    admin = False
    is_member = False

    try:
        baseGroup = BaseGroup.objects.get(id=group_id)

        #make sure the group is still active
        if not baseGroup.is_active:
            raise Http404

        if(request.user == baseGroup.owner.user):
            admin = True
        owner = baseGroup.owner

        is_member = request.user.userprofile in baseGroup.users.all()

    #raise 404 if group can't be found
    except BaseGroup.DoesNotExist:
        raise Http404

    return render(request, "basic_group/group_main.html", {'group':baseGroup, 'owner':owner, 'admin':admin, 'is_member':is_member})

#returns a list of groups that are registered
def view_group_list(request):
    group_list = GroupTable(BaseGroup.objects.all())
    RequestConfig(request, paginate={"per_page": 50}).configure(group_list)
    return render(request, "basic_group/group_list.html", {"groups": group_list})

#ajax call for joininig a group
@login_required()
def join(request):
    group = get_object_or_404(BaseGroup, id=request.POST.get('groupId') )
    group.users.add(request.user.userprofile)
    group.save()
    return render(request, "basic_group/group_members.html", {'group':group})

#ajax call for leaving a group
@login_required()
def leave(request):
    group = get_object_or_404(BaseGroup, id=request.POST.get('groupId') )
    if(request.user.userprofile in group.users.all()):
        group.users.remove(request.user.userprofile)
        group.save()

    return render(request, "basic_group/group_members.html", {'group':group})

