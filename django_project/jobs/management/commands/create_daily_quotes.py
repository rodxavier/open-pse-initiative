import csv
import glob
import logging
import os
from datetime import datetime
from filecmp import dircmp

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from companies.models import Company
from quotes.models import Quote

logger = logging.getLogger('jobs.management.commands')

class Command(BaseCommand):
    help = 'Create daily quotes'

    def handle(self, *args, **options):
        files = []
        if os.path.isdir(settings.PREV_QUOTES_DIR):
            dcmp = dircmp(settings.PREV_QUOTES_DIR, settings.NEW_QUOTES_DIR)
            # Process subdirs common to both dir
            for subdir, sub_dcmp in dcmp.subdirs.items():
                temp = sub_dcmp.right_only
                temp = [os.path.join(subdir, x) for x in temp]
                files.extend(temp)
            files = [os.path.join(settings.NEW_QUOTES_DIR, x) for x in files]
            # Process subdirs not present in PREV_QUOTES_DIR
            for subdir in dcmp.right_only:
                path = os.path.join(settings.NEW_QUOTES_DIR, subdir)
                if os.path.isdir(path):
                    files.extend(glob.glob(os.path.join(path, '*.csv')))
        else:
            files = glob.glob(os.path.join(settings.NEW_QUOTES_DIR, '*', '*.csv'))
        for afile in files:
            with open(afile, 'r') as f:
                created_obj = updated_obj = 0
                logger.info('Processing {0}'.format(afile))
                reader = csv.reader(f)
                for row in reader:
                    try:
                        symbol, quote_date, price_open, price_high, price_low, price_close, volume, value = row
                        quote_date = datetime.strptime(quote_date, '%m/%d/%Y')
                        
                        if symbol.startswith('^'):
                            name = symbol
                            company, created = Company.objects.get_or_create(name=name)
                        else:    
                            company, created = Company.objects.get_or_create(symbol=symbol)
                        
                        created = False
                        try:
                            quote = Quote.objects.get(
                                company=company,
                                quote_date=quote_date,
                            )
                        except Quote.DoesNotExist:
                            quote = Quote(
                                company=company,
                                quote_date=quote_date,
                            )
                            created = True
                        quote.price_open = price_open
                        quote.price_high = price_high
                        quote.price_low = price_low
                        quote.price_close = price_close
                        quote.volume = volume
                        quote.save()
                        
                        if created:
                            created_obj += 1
                        else:
                            updated_obj += 1
                    except Exception, e:
                        logger.error(row)
                        logger.error(e)
                        continue
                logger.info('{0} created records. {1} updated records.'.format(created_obj, updated_obj))
