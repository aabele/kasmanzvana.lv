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
        author = models.user_model.objects.get(pk=1)
        for item in data:
            number, _ = models.Phone.objects.get_or_create(phone=item.get("number"))
            comment = models.Comment(
                author=author,
                phone=number,
                body='Atradām ka šis numurs ir norādīts pie <a href="{1}">{0}</a>'.format(item.get("title"), item.get('url')))
            comment.save()
