#from django.conf.urls import include
from django.conf.urls import patterns, url

from futurestop import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'futurestop.views.home', name='home'),
    #url(r'^index/', views.index, name='index'),
    url(r'^api/(?P<udid>\d+)/', views.udid, name='udid'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
