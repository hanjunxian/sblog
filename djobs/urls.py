# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(('djobs.views'),
    # Examples:
    # url(r'^$', 'djobs.views.home', name='home'),
    # url(r'^djobs/', include('djobs.foo.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^hello/$', 'hello'),
    url(r'^now/$', 'current_datetime'),
    url(r'^time/plus/(\d+)/$', 'hours_ahead'),
    url(r'^displaymeta/$', 'request_meta'),
)

urlpatterns += patterns(('contact.views'),
    (r'^contact/$', 'contact'),
    (r'^contact_form/$', 'contact_form'),
    (r'^contact/thanks/$', 'thanks'),
)

urlpatterns += patterns((''),
    (r'^smallblog/', include('simpleblog.urls')),
)

urlpatterns += patterns((''),
    #静态文件
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/gs/djobs/static/'}
    ),
)