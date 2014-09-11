import logging
import os
import shutil
from StringIO import StringIO
from zipfile import ZipFile

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

import requests

logger = logging.getLogger('jobs.management.commands')

class Command(BaseCommand):
    help = 'Download the quotations zip file from Dropbox'

    def handle(self, *args, **options):
        r = requests.get(settings.QUOTES_DROPBOX_DL_URL)
        z = ZipFile(StringIO(r.content))
        if os.path.isdir(settings.NEW_QUOTES_DIR):
            if os.path.isdir(settings.PREV_QUOTES_DIR):
                shutil.rmtree(settings.PREV_QUOTES_DIR)
            shutil.move(settings.NEW_QUOTES_DIR, settings.PREV_QUOTES_DIR)
        z.extractall(settings.NEW_QUOTES_DIR)
        logger.info('Downloaded quotes')
        
