from django.conf.urls import url, include, patterns

urlpatterns = patterns('',
    url(r'^editprofile/$', 'UserProfile.views.user_profile'),
    url(r'^profile/$', 'UserProfile.views.account_view')
)