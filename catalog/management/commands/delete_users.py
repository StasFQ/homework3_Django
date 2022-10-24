from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.core.management.base import BaseCommand
User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number', nargs='+', type=int)

    def handle(self, *args, **options):
        superusers = User.objects.filter(is_superuser=True, id__in=options['number'])
        if superusers.exists():
            raise PermissionDenied
        else:
            User.objects.filter(id__in=options['number']).delete()
