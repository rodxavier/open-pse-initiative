from django.contrib import admin

from quotes.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('get_symbol', 'quote_date', 'price_open', 'price_high', 'price_low', 'price_close', 'volume',)

    def get_symbol(self, obj):
        return obj.company.symbol if obj.company.symbol is not None else obj.company.name
    get_symbol.admin_order_field  = 'company__symbol'

admin.site.register(Quote, QuoteAdmin)
