from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.core import serializers

import urllib.request


@shared_task
def get_file_from_url(url):
    file = urllib.request.URLopener()
    file.retrieve(url, 'tmp.csv.zip')