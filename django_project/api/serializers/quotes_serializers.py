from rest_framework import serializers

from common.utils import CustomList
from quotes.models import Quote

class QuoteSerializer(serializers.ModelSerializer):    
    name = serializers.SerializerMethodField('get_company_name')
    symbol = serializers.SerializerMethodField('get_company_symbol')
    
    class Meta:
        model = Quote
        fields = ('symbol', 'name', 'quote_date', 'price_open', 'price_high', 'price_low',
                    'price_close', 'volume',)
                    
    def get_company_name(self, obj):
        return obj.company.name
        
    def get_company_symbol(self, obj):
        return obj.company.symbol
