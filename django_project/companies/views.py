from django.views import generic

from companies.models import Company

class CompanyListView(generic.ListView):
    model = Company
    template_name = "companies/company_list.html"
    paginate_by = 50
    queryset = Company.objects.filter(is_index=False, is_currently_listed=True)
