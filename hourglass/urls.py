from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.http import HttpResponse

from hourglass_site import views as site_views
from api import urls as api_urls

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^api/', include(api_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tests/$', TemplateView.as_view(template_name='tests.html')),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /")),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^accounts/login', TemplateView.as_view(template_name='login.html')),
    url(r'^oauth/callback', site_views.oauth_callback),
    url(r'^protected/$', site_views.example_protected_view),
)
