from datetime import datetime

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import views

from companies.models import Company
from quotes.models import Quote
from serializers import CompanySerializer, QuoteSerializer
    
class APIRootView(views.APIView):
    def get(self, request):
        return Response({
            'version': 0.1,
            'resources': {
                'companies': reverse('api_companies_list', request=request),
                'quotes': reverse('api_quotes_list', request=request),
            }
        })

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class QuoteListView(generics.ListAPIView):
    serializer_class = QuoteSerializer
    
    def get_queryset(self):
        items = Quote.objects.all()
        stocks = self.request.QUERY_PARAMS.get('stocks')
        from_date = self.request.QUERY_PARAMS.get('from_date')
        to_date = self.request.QUERY_PARAMS.get('to_date')
        if stocks is not None:
            stocks = stocks.split(',')
            items = items.filter(company__symbol__in=stocks)        
        if from_date is None and to_date is None:
            latest_quote_date = Quote.objects.latest('quote_date').quote_date
            items = items.filter(quote_date=latest_quote_date)
        if from_date is not None:
            from_date = datetime.strptime(from_date, '%Y-%m-%d')
            items = items.filter(quote_date__gte=from_date)
        if to_date is not None:
            to_date = datetime.strptime(to_date, '%Y-%m-%d')
            items = items.filter(quote_date__lte=to_date)
        return items.order_by('quote_date', '-company__is_index', 'company__symbol')
