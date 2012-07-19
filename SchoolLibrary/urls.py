from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^allstudents/$', 'studentinfo.views.listofnames', name = 'All Students'),
    url(r'^studentinfo/(?P<studentinfo_id>\d+)/$', 'studentinfo.views.individual_student' ),
    url(r'^$', 'studentinfo.views.homepage'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    	 url(r'^admin/', include(admin.site.urls)),
)
