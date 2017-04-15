from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.core import serializers

import urllib.request


@shared_task
def get_file_from_url(url, filename='tmp.csv.zip'):
    file = urllib.request.URLopener()
    file.retrieve(url, filename)
    return filename


@shared_task
def process_zipped_csv_file(filename):
    print('Processing zipped csv file {}'.format(filename))


