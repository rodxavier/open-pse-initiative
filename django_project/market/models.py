from django.db import models

class NonTradingDay(models.Model):
    non_trading_date = models.DateField()
    
    class Meta:
        ordering = ('non_trading_date',)
        verbose_name = 'Non Trading Day'
        verbose_name_plural = 'Non Trading Days'
        
    def __unicode__(self):
        return self.non_trading_date.strftime('%B %d, %Y')
        
    def __str__(self):
        return self.non_trading_date.strftime('%B %d, %Y')
