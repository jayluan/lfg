from django.conf.urls import url, include, patterns


urlpatterns = patterns('',
    url(r'^creating/$', 'UserProfile.views.user_profile'),
    url(r'^new/$', 'BaseGroup.views.new_group'),
    url(r'^view/(?P<group_id>\d+)', 'BaseGroup.views.view_group', name='view_group'),
    url(r'^join/$', 'BaseGroup.views.join'),
    url(r'^leave/$', 'BaseGroup.views.leave'),
    url(r'^all/$', 'BaseGroup.views.view_group_list')
)