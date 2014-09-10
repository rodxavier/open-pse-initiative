import csv
import logging

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from companies.models import Company

logger = logging.getLogger('jobs.management.commands')

class Command(BaseCommand):
    help = 'Create companies'

    def handle(self, *args, **options):
        indices = (
            ('PSEi', '^PSEi',),
            ('ALL', '^ALLSHARES'),
            ('FIN', '^FINANCIAL'),
            ('IND', '^INDUSTRIAL'),
            ('HDG', '^HOLDING'),
            ('PRO', '^PROPERTY'),
            ('SVC', '^SERVICE'),
            ('M-O', '^MINING-OIL'),
        )
        
        created_obj = 0
        for index in indices:
            company, created = Company.objects.get_or_create(symbol=index[0], name=index[1], is_index=True)
            if created: created_obj += 1
        logger.info('{0} Company(Index) records created.'.format(created_obj))
        
        with open(settings.COMPANY_NAMES_PATH, 'r') as f:
            reader = csv.reader(f)
            created_obj = 0
            for row in reader:
                symbol, name = row
                if name.endswith('"') and name.startswith('"'):
                    name = name[1:-1]
                name = name.replace('""', '\'')
                company, created = Company.objects.get_or_create(name=name, symbol=symbol)
                if created: created_obj += 1
            
        logger.info('{0} Company records created.'.format(created_obj))
