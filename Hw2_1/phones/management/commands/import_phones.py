import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            is_first=True
            for row in spamreader:
                if is_first:
                    is_first=False
                    continue
                phone = Phone()
                phone.name = row[1]
                phone.image = row[2]
                phone.price = row[3]
                phone.release_date = row[4]
                phone.lte_exists = row[5]
                # ... остальные поля модели Phone
                phone.save()