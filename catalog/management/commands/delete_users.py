import argparse

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


def check_positive(value):
    if not str(value).isdigit():
        raise argparse.ArgumentTypeError(f'{value} is an invalid int value, enter positive int values')
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f'{value} is an invalid positive int value')
    return ivalue


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('user_ids', nargs='+', type=check_positive,
                            help='input user ids to delete')

    def handle(self, *args, **options):
        User = get_user_model()
        user_ids = options['user_ids']

        needed_users = User.objects.filter(id__in=user_ids)

        if not needed_users.exists():
            self.stdout.write(self.style.WARNING(f'Users not exists: {str(user_ids)}'))
            return
        elif not needed_users.filter(is_superuser=1).exists():
            deleted = needed_users.delete()
            self.stdout.write(self.style.SUCCESS(f'Deleted users: {str(deleted)}'))
        else:
            super_user = needed_users.filter(is_superuser=1)
            self.stdout.write(self.style.WARNING(f'User ids contains superuser: {str(super_user)}'))
