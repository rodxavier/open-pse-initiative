from django.views import generic

from rest_framework.reverse import reverse

from quotes.models import Quote

class DailyQuotesDownloadView(generic.ListView):
    model = Quote
    template_name = "quotes/downloads.html"
    paginate_by = 50
    queryset = Quote.objects.order_by('-quote_date').values_list('quote_date', flat=True).distinct()
    
    def get_context_data(self, **kwargs):
        base_url = reverse('api_quotes_list', request=self.request)
        context = super(generic.ListView, self).get_context_data(**kwargs)
        items = []
        for obj in context['object_list']:
            date_string = obj.strftime('%Y-%m-%d')
            item = {
                'quote_date': date_string,
                'csv_url': self.generate_download_url(base_url, date_string, 'csv'),
                'json_url': self.generate_download_url(base_url, date_string, 'json'),
                'xml_url': self.generate_download_url(base_url, date_string, 'xml'),
            }
            items.append(item)
        context['object_list'] = items
        return context
                                       
    def generate_download_url(self, base_url, quote_date, format_type):
        return '{0}?from_date={1}&to_date={1}&format={2}'.format(base_url, quote_date, format_type)
