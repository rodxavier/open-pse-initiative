from django.core.management call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create data for the day'

    def handle(self, *args, **options):
        call_command('download_quotes')
        call_command('create_daily_quotes')
