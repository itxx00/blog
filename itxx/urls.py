#coding:utf-8
from django.conf.urls.defaults import patterns, include, url#, handler500
#from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout
from django.conf import settings

handler500 = 'itxx.blog.views.handler500'
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smd5.views.home', name='home'),
    # url(r'^smd5/', include('smd5.foo.urls')),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
    url(r'media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'sh/(?P<path>.*)$','django.views.static.serve',{'document_root':'s/',}),
    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^2b=yes/', include(admin.site.urls)),
    url(r'^$','itxx.views.index'),
    url(r'^blog/$','itxx.blog.views.index'),
    url(r'^blog/index/(?P<paperid>\d+)','itxx.blog.views.index'),
    
    url(r'^blog/comments/(?P<paperid>\d+)/(?P<showcmt>\d)','itxx.blog.views.papercomment'),##use paper id as url.
    url(r'^blog/comments/(?P<paperid>\d+)','itxx.blog.views.papercomment'),##use paper id as url.
    
    url(r'^blog/list/(?P<ptype>\d+)/(?P<ptid>\d+)','itxx.blog.views.plist'),
    url(r'^blog/list/(?P<ptype>\d+)','itxx.blog.views.plist'),
    #url(r'^blog/link$','itxx.blog.views.link'),
    #url(r'^blog/about$','itxx.blog.views.about'),
    url(r'^robots.txt','itxx.views.robots'),
    url(r'^blog/img=(?P<img_name>\w+\.\w+)','itxx.blog.views.showimg'),
    url(r'^upload_image/','itxx.blog.views.upload_image'),
)
