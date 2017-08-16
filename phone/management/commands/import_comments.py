import json
import datetime

from django.core.management.base import BaseCommand

from phone import models


class Command(BaseCommand):
    help = 'import links from json file'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('file_location', nargs='+', type=str)

    def handle(self, *args, **options):
        file_name = options.get('file_location')[0]
        f = open(file_name, 'r')
        data = json.loads(f.read())
        for key, value in data.items():
            number, _ = models.Phone.objects.get_or_create(phone=key)

            for comment in value:
                if comment.get('email'):
                    author, _ = models.user_model.objects.get_or_create(
                        username=comment.get('email'))
                    author.email = comment.get('email')

                else:
                    author, _ = models.user_model.objects.get_or_create(
                        username=comment.get('name'))

                author.first_name = comment.get('name') or ''
                author.save()

                c = models.Comment(
                    author=author,
                    legacy=False if author else True,
                    phone=number,
                    insert_date=datetime.datetime.strptime(comment.get('insert_date'), "%Y-%m-%dT%H:%M:%S.%f"),
                    body=comment.get('comment'))
                c.save()
