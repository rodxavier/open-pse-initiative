import logging

from django.core.management import call_command
from django.core.management.base import BaseCommand

logger = logging.getLogger('jobs.management.commands')

class Command(BaseCommand):
    help = 'Create data for the day'

    def handle(self, *args, **options):
        logger.info('Starting daily_job')
        call_command('download_quotes')
        call_command('create_daily_quotes')
        logger.info('Finished daily_job')
