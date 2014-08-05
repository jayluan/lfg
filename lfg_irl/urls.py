from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from registration.backends.default.views import RegistrationView
from LookingForGroupMain.forms import CustomRegistrationForm
from django.conf import settings
from django.conf.urls.static import static

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
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'LookingForGroupMain.views.logout_view'),

    #not sure why this works but if I just pass the URL to a def in views.py, it does not POST to the model
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=CustomRegistrationForm), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('UserProfile.urls')),
#    url(r'^profile/(\w+)/$', 'LookingForGroupMain.views.profile')
    url(r'^groups/', include('BaseGroup.urls'))

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
