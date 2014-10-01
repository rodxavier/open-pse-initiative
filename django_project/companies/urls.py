from django.conf.urls import patterns, url

from companies.views import CompanyListView

urlpatterns = patterns('',
    url(r'^$', CompanyListView.as_view(), name='companies_list'),
)
