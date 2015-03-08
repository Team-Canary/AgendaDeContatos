from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'agenda.views.index'),
    url(r'adiciona/$', 'agenda.views.adiciona'),
    url(r'item/(?P<id_item>\d+)/$', 'agenda.views.item'),
    url(r'remove/(?P<id_item>\d+)/$', 'agenda.views.remove'),

    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',{'login_url': '/login/'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
