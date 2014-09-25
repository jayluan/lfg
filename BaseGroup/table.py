import django_tables2 as tables
from BaseGroup.models import BaseGroup
#from LookingForGroupMain.views import user_detail
#from BaseGroup.views import view_group
from django_tables2.utils import A

class GroupTable(tables.Table):
#    name = tables.Column(verbose_name="Group Name")
    owner = tables.LinkColumn('user_detail', args=[A('owner.user.username')])
    name = tables.LinkColumn('view_group', args=[A('pk')])

    class Meta:
        attrs = {"class": "paleblue"}
        model = BaseGroup
        fields = ('name', 'description', 'date_created', 'date_action', 'owner', 'group_size')