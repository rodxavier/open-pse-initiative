from rest_framework import serializers

from common.utils import CustomList
from companies.models import Company
from quotes.models import Quote

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('symbol', 'name',)
        
class QuoteSerializer(serializers.ModelSerializer):    
    name = serializers.SerializerMethodField('get_company_name')
    symbol = serializers.SerializerMethodField('get_company_symbol')
    
    class Meta:
        model = Quote
        fields = ('symbol', 'name', 'quote_date', 'price_open', 'price_high', 'price_low',
                    'price_close', 'volume',)
                    
    @property
    def data(self):
        ret_data = super(serializers.ModelSerializer, self).data
        ret_data = CustomList(ret_data)
        header = self.fields.keys()
        ret_data.header = lambda: None
        setattr(ret_data, 'header', header)
        return ret_data
                    
    def get_company_name(self, obj):
        return obj.company.name
        
    def get_company_symbol(self, obj):
        return obj.company.symbol
