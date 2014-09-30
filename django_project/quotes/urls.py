from django.conf.urls import patterns, url

from quotes.views import DailyQuotesDownloadView

urlpatterns = patterns('',
    url(r'^downloads$', DailyQuotesDownloadView.as_view(), name='quotes_download'),
)
