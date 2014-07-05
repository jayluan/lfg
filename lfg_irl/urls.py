from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, auth
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'LookingForGroupMain.views.index'),
    url(r'^user/(?P<user>[a-zA-Z]+)', 'LookingForGroupMain.views.user_detail'),
    url(r'^account/profile', 'LookingForGroupMain.views.account_view'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'LookingForGroupMain.views.logout_view'),
    url(r'^signup', 'LookingForGroupMain.views.signup_view')
)
