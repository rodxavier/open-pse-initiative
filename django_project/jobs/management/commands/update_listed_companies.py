import logging
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

import requests

from companies.models import Company

logger = logging.getLogger('jobs.management.commands')

class Command(BaseCommand):
    help = 'Update currently listed companies'

    def handle(self, *args, **options):
        logger.info('Started updating currently listed companies')
        companies = Company.objects.filter(is_index=False)
        r = requests.get(settings.COMPANY_LIST_URL)
        records = r.json()['records']
        for record in records:
            symbol = record['securitySymbol']
            name = record['securityName']
            listing_date = record['listingDate'].split()[0]
            status = record['securityStatus']
            try:
                company = companies.get(symbol=symbol)
                companies = companies.exclude(id=company.id)
            except Company.DoesNotExist:
                company = Company(symbol=symbol)
            company.name = name
            company.is_currently_listed = True
            company.is_suspended = True if status == 'S' else False
            company.listing_date = datetime.strptime(listing_date, '%Y-%m-%d').date()
            company.save()
        companies.update(is_currently_listed=False, is_suspended=False)
        logger.info('Finished updating currently listed companies')
