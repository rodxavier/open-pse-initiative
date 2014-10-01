from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^terms$', TemplateView.as_view(template_name='terms.html'), name='terms'),
    
    url(r'^api/', include('api.urls')),
    url(r'^quotes/', include('quotes.urls')),
    url(r'^companies/', include('companies.urls')),
    
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^secret/', include(admin.site.urls)),
    
    url(r'^robots\.txt$', include('robots.urls')),
    url(r'^humans\.txt$', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
