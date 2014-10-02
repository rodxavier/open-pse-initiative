from datetime import datetime, timedelta

from django.db import models
from django.db.models import Max, Min

class Company(models.Model):
    name = models.CharField(max_length=75, blank=True, null=True)
    symbol = models.CharField(max_length=10, blank=True, null=True)
    listing_date = models.DateField(blank=True, null=True)
    order = models.IntegerField(blank=True, default=0)
    is_index = models.BooleanField(blank=True, default=False)
    is_currently_listed = models.BooleanField(blank=True, default=True)
    is_suspended = models.BooleanField(blank=True, default=False)
    
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('symbol',)
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        
    def __unicode__(self):
        return self.symbol if self.symbol is not None else self.name
        
    def __str__(self):
        return self.symbol if self.symbol is not None else self.name
        
    @property
    def readable_name(self):
        if self.is_index:
            return self.name[1:]
        else:
            return self.name
    
    @property    
    def year_high(self):
        today = datetime.now()
        one_year = timedelta(days=52*7)
        if today.isoweekday() == 6:
            today = today - timedelta(days=1)
        elif today.isoweekday() == 7:
            today = today - timedelta(days=2)
        last_year = today - one_year
        quotes = self.quote_set.filter(quote_date__gt=last_year)
        if quotes.count() == 0:
            return 0.0
        year_high = quotes.aggregate(Max('price_high'))
        return ('%f' % year_high['price_high__max']).rstrip('0').rstrip('.')
        
    @property    
    def year_low(self):
        today = datetime.now()
        one_year = timedelta(days=52*7)
        if today.isoweekday() == 6:
            today = today - timedelta(days=1)
        elif today.isoweekday() == 7:
            today = today - timedelta(days=2)
        last_year = today - one_year
        quotes = self.quote_set.filter(quote_date__gt=last_year)
        if quotes.count() == 0:
            return 0.0
        year_low = quotes.aggregate(Min('price_low'))
        return ('%f' % year_low['price_low__min']).rstrip('0').rstrip('.')
        
    @property
    def last_thirty_quotes(self):
        quotes = self.quote_set.order_by('-quote_date')[:30]
        return quotes
