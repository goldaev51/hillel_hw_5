from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('cnt', nargs=1, type=int,
                            help='input count of new users to be created',
                            choices=range(1, 11))

    def handle(self, *args, **options):
        cnt = options['cnt'][0]

        User = get_user_model()
        fake = Faker()

        users = list()
        for i in range(cnt):
            username = (fake.first_name() + fake.last_name()).lower()
            user_email = (username + '@' + fake.free_email_domain())
            password = make_password(fake.password())

            user = User(username=username, email=user_email, password=password)
            users.append(user)

            self.stdout.write(self.style.SUCCESS(f'Created user: {str(username)}'))

        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('All users created!'))
