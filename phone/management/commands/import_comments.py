import json

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
            print('Processing %s' % key)
            print(key)
            print(value)
            number, _ = models.Phone.objects.get_or_create(phone=key)

            for comment in value:
                author = None
                if comment.get('email'):
                    author, _ = models.user_model.objects.get_or_create(email=comment.get('email'), first_name=comment.get('name'))

                c = models.Comment(
                    author=author,
                    legacy=False if author else True,
                    phone=number,
                    body=c.get('comment'))
                c.save()
