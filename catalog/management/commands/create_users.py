import random

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from faker import Faker


User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number', nargs='+', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        fake = Faker()
        ans = []
        it = int(''.join(map(str, options['number'])))
        while it:
            name = fake.name()
            ans.append(User(username=name, email=name.replace(' ', '')+'@gmail.com',
                            password=make_password(random.choice('123abc'))))
            it -= 1
        User.objects.bulk_create(ans)
