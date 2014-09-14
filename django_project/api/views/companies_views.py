from rest_framework import generics

from api.serializers import CompanySerializer
from companies.models import Company

class IndexListView(generics.ListAPIView):
    """
    Returns a list of all indices and industries
    """
    queryset = Company.objects.filter(is_index=True)
    serializer_class = CompanySerializer

class CompanyListView(generics.ListAPIView):
    """
    Returns a list of all companies
    
    ### Parameters
    - **include_indices** - Takes 1(true)/0(false) as values to include indices. **Default: 0**
    
    ### Examples

    Get the all companies including indices and industries

        GET     /api/companies/?include_indices=1
    """
    serializer_class = CompanySerializer
    
    def get_queryset(self):
        items = Company.objects.all()
        include_indices = self.request.QUERY_PARAMS.get('include_indices', 0)
        if include_indices in [0, '0']:
            items = items.filter(is_index=False)
        return items
