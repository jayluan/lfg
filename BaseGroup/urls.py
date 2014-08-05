from django.conf.urls import url, include, patterns


urlpatterns = patterns('',
    url(r'^creating/$', 'UserProfile.views.user_profile'),
    url(r'^new/$', 'BaseGroup.views.new_group')
)