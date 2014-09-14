import json
from datetime import datetime

from django.conf import settings
from django.core.paginator import Paginator

import requests
from rest_framework import generics
from rest_framework import views
from rest_framework.pagination import PaginationSerializer
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer, XMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse

from quotes.models import Quote
from api.serializers import QuoteSerializer

class QuoteListView(generics.ListAPIView):
    """
    Returns a list of end-of-day quotes from the PSE

    ### Parameters
    - **stocks** - A comma separated list of stock symbols
    - **from_date** - Start date of end-of-day quotes. This is inclusive. **Format: YYYY-MM-DD**
    - **to_date** - End date of end-of-day quotes. This is exclusive. **Format: YYYY-MM-DD**

    *NOTE: All the parameters are not required. When neither `from_date` and `to_date` are provided, 
    the API returns the quotes from the latest available date.*

    ### Examples

    Get the latest available end-of-day quote for a company

        GET     /api/quotes/?stocks=BDO

    Get the latest available end-of-day quote for multiple companies

        GET     /api/quotes/?stocks=BDO,BPI,MBT

    Get all available end-of-day quotes for all companies starting from the `from_date`

        GET     /api/quotes/?from_date=2014-04-07

    Get all available end-of-day quotes for all companies starting until the `end_date`
        
        GET     /api/quotes/?to_date=2014-04-07
        
    Get all available end-of-day quotes for all companies between from the `from_date`, until the `end_date`

        GET     /api/quotes/?from_date=2014-04-07&to_date=2014-11-11
    """
    serializer_class = QuoteSerializer
    
    def get_queryset(self):
        items = Quote.objects.all()
        stocks = self.request.QUERY_PARAMS.get('stocks')
        from_date = self.request.QUERY_PARAMS.get('from_date')
        to_date = self.request.QUERY_PARAMS.get('to_date')
        if stocks is not None:
            stocks = stocks.split(',')
            stocks = [x.upper() for x in stocks]
            items = items.filter(company__symbol__in=stocks)        
        if from_date is None and to_date is None:
            latest_quote_date = Quote.objects.latest('quote_date').quote_date
            items = items.filter(quote_date=latest_quote_date)
        if from_date is not None and to_date is not None and from_date == to_date:
            quote_date = datetime.strptime(from_date, '%Y-%m-%d')
            items = items.filter(quote_date=quote_date)
        else:
            if from_date is not None:
                from_date = datetime.strptime(from_date, '%Y-%m-%d')
                items = items.filter(quote_date__gte=from_date)
            if to_date is not None:
                to_date = datetime.strptime(to_date, '%Y-%m-%d')
                items = items.filter(quote_date__lt=to_date)
        return items.order_by('quote_date', '-company__is_index', 'company__symbol')
        
class TickerView(views.APIView):
    """
    Provides a near-realtime endpoint for quotes
    
    ### Parameters
    - **stocks** - A comma separated list of stock symbols
    
    ### Examples

    Get the latest available end-of-day quote for a company

        GET     /api/quotes/?stocks=BPI
    """
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, XMLRenderer)
    
    def get(self, request):
        r = requests.get(settings.TICKER_URL)
        response = json.loads(r.content)
        data = {}
        items = []
        stocks = self.request.QUERY_PARAMS.get('stocks')
        if stocks is not None:
            stocks = stocks.split(',')
            stocks = [x.upper() for x in stocks]
        for item in response:
            if item['securitySymbol'] == 'Stock Update As of':
                as_of = item['securityAlias']
                as_of = datetime.strptime(as_of, '%m/%d/%Y %I:%M %p')
                data['as_of'] = as_of.strftime('%Y-%m-%d %I:%M%p')
            else:
                quote = {}
                quote['symbol'] = item['securitySymbol'].upper()
                if Company.objects.filter(symbol=quote['symbol']).count() != 0:
                    quote['name'] = Company.objects.get(symbol=quote['symbol']).name
                else:
                    quote['name'] = item['securityAlias'].title()
                quote['percent_change'] = item['percChangeClose']
                quote['price'] = item['lastTradedPrice']
                quote['volume'] = item['totalVolume']
                quote['indicator'] = item['indicator']
                if stocks is not None:
                    if quote['symbol'] in stocks:
                        items.append(quote)
                else:
                    items.append(quote)
        data['quotes'] = items
        return Response(data)
        
class DailyQuotesDownloadView(views.APIView):
    paginate_by = 100
    
    def get(self, request):
        base_url = reverse('api_quotes_list', request=request)
        page_num = self.request.QUERY_PARAMS.get('page', 1)
        quote_dates = Quote.objects.order_by('-quote_date').values_list('quote_date', flat=True).distinct()
        paginator = Paginator(quote_dates, self.paginate_by)
        page = paginator.page(page_num)
        items = []
        for obj in page.object_list:
            date_string = obj.strftime('%Y-%m-%d')
            item = {
                'quote_date': date_string,
                'csv_url': self.generate_download_url(base_url, date_string, 'csv'),
                'json_url': self.generate_download_url(base_url, date_string, 'json'),
                'xml_url': self.generate_download_url(base_url, date_string, 'xml'),
            }
            items.append(item)
        page.object_list = items
        serializer = PaginationSerializer(instance=page, context={'request': request})
        data = serializer.data
        return Response(data)
        
    def generate_download_url(self, base_url, quote_date, format_type):
        return '{0}?from_date={1}&to_date={1}&format={2}'.format(base_url, quote_date, format_type)
