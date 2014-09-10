from django.db import models

class Quote(models.Model):
    company = models.ForeignKey('companies.Company')
    quote_date = models.DateField()
    price_open = models.DecimalField(max_digits=20, decimal_places=10)
    price_high = models.DecimalField(max_digits=20, decimal_places=10)
    price_low = models.DecimalField(max_digits=20, decimal_places=10)
    price_close = models.DecimalField(max_digits=20, decimal_places=10)
    volume = models.BigIntegerField(blank=True, null=True)
    
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-quote_date', 'company',)
        unique_together = (('company', 'quote_date'),)
        
    def __unicode__(self):
        return '{0} {1}'.format(self.quote_date, self.company.symbol)
        
    def __str__(self):
        return '{0} {1}'.format(self.quote_date, self.company.symbol)
