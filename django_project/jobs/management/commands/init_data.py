from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Initialize Data'

    def handle(self, *args, **options):
        call_command('download_quotes')
        call_command('create_companies')
        call_command('create_historical_quotes')
        call_command('create_daily_quotes')
