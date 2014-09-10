from django.contrib import admin

from companies.models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'is_index', 'created_datetime', 'updated_datetime',)

admin.site.register(Company, CompanyAdmin)
