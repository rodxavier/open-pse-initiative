from rest_framework_csv.renderers import CSVRenderer

from api.serializers import QuoteSerializer

class QuoteCSVRenderer(CSVRenderer):
	headers = QuoteSerializer().get_fields()