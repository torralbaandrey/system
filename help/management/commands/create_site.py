# help/management/commands/create_site.py

from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site

class Command(BaseCommand):
    help = 'Create a new site'

    def handle(self, *args, **kwargs):
        Site.objects.get_or_create(domain='127.0.0.1:8000', name='Localhost')
        self.stdout.write(self.style.SUCCESS('Successfully created site: Localhost'))