import csv
import logging
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from companies.models import Company
from quotes.models import Quote

logger = logging.getLogger('jobs.management.commands')

class Command(BaseCommand):
    help = 'Create historical quotes'

    def handle(self, *args, **options):
        with open(settings.HISTORICAL_QUOTES_PATH, 'r') as f:
            reader = csv.reader(f)
            indices = {
                'FINANCIAL': '^FINANCIAL',
                'INDUSTRIAL': '^INDUSTRIAL',
                'HOLDINGS': '^HOLDING',
                'PROPERTY': '^PROPERTY',
                'SERVICES': '^SERVICE',
                'MINING&O': '^MINING-OIL',
                'COMPOSITE': '^PSEi',
                'ALL SHARES INDE': '^ALLSHARES',
            }
            processed = {}
            records = []
            for row in reader:
                try:
                    symbol, quote_date, price_open, price_high, price_low, price_close, volume, last = row
                
                    if quote_date == '<DATE>':
                        continue
                    quote_date = datetime.strptime(quote_date, '%Y%m%d')
                    
                    if symbol in indices.keys():
                        name = indices[symbol]
                        company, created = Company.objects.get_or_create(name=name)
                    else:    
                        company, created = Company.objects.get_or_create(symbol=symbol)
                    
                    if not quote_date in processed.keys():
                        processed[quote_date] = []
                    if not company.id in processed[quote_date]:
                        processed[quote_date].append(company.id)
                        records.append(
                            Quote(
                                company=company,
                                quote_date=quote_date,
                                price_open=price_open,
                                price_high=price_high,
                                price_low=price_low,
                                price_close=price_close,
                                volume=volume
                            )
                        )
                    if len(records) >= 50000:
                         Quote.objects.bulk_create(records)
                         logger.info('{0} Quote records created'.format(len(records)))
                         records = []
                         
                except Exception, e:
                    logger.error(row)
                    logger.error(e)
                    continue
                    
            Quote.objects.bulk_create(records)
            logger.info('{0} Quote records created'.format(len(records)))
