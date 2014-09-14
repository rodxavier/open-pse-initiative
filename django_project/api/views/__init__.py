from rest_framework import views
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer, XMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.views.companies_views import *
from api.views.quotes_views import *

class APIRootView(views.APIView):
    """
    A Public API that provides end-of-day quotes from the Philippine Stock Exchange(PSE).
    
    ### Supported formats
    - **json**
    - **xml**
    - **csv**
    
    Please send an email to [hello@rodxavier.com](mailto:hello@rodxavier.com) if you find any inaccuracies in the data.
    """
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, XMLRenderer)
    
    def get(self, request):
        return Response({
            'version': 0.1,
            'resources': {
                'indices': reverse('api_indices_list', request=request),
                'companies': reverse('api_companies_list', request=request),
                'quotes': reverse('api_quotes_list', request=request),
                'ticker': reverse('api_ticker', request=request),
            }
        })
