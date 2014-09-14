from django.conf.urls import patterns, include, url

from rest_framework import routers

from api.views import APIRootView, IndexListView, CompanyListView, QuoteListView, TickerView, \
    QuoteDateListView

urlpatterns = patterns('api.views',
    url(r'^$', APIRootView.as_view(), name='api_root'),
    url(r'^indices/$', IndexListView.as_view(), name='api_indices_list'),
    url(r'^companies/$', CompanyListView.as_view(), name='api_companies_list'),
    url(r'^quotes/$', QuoteListView.as_view(), name='api_quotes_list'),
    url(r'^ticker/$', TickerView.as_view(), name='api_ticker'),

    url(r'^quotes/date/$', QuoteDateListView.as_view(), name='api_quote_date_list'),
)
