from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=75, blank=True, null=True)
    symbol = models.CharField(max_length=10, blank=True, null=True)
    is_index = models.BooleanField(blank=True, default=False)
    
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('symbol',)
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        
    def __unicode__(self):
        return self.symbol if self.symbol is not None else self.name
        
    def __str__(self):
        return self.symbol if self.symbil is not None else self.name
