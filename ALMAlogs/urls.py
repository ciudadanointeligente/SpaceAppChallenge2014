from django.views.generic.base import TemplateView
from .views import HomeTemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SpaceAppChallenge2014.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeTemplateView.as_view(template_name='index.html'), name='home'),
    # url(r'^$', TemplateView.as_view(template_name = 'index.html'), name='home'),
)
