from django.contrib import admin

from companies.models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'listing_date', 'is_index', 'is_currently_listed', 'is_suspended', 'created_datetime', 'updated_datetime',)

admin.site.register(Company, CompanyAdmin)
