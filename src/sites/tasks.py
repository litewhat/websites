from __future__ import absolute_import, unicode_literals
from celery import shared_task

import csv
import json
import urllib.request
from zipfile import ZipFile


@shared_task
def get_file_from_url(url, filename='tmp.csv.zip'):
    file = urllib.request.URLopener()
    file.retrieve(url, filename)
    return filename


@shared_task
def process_zipped_csv_file(filename):
    # TODO:
    archive = ZipFile(filename)
    datafile = archive.infolist()[0]
    archive.extract(datafile)
    return datafile.filename


@shared_task
def get_data_from_csv_file(filename):
    websites = []
    with open(filename, newline='') as csvfile:
        websites_reader = csv.reader(csvfile, delimiter=',')
        for row in websites_reader:
            alexa_rank, url = row
            websites.append((alexa_rank, url))
    return json.dumps(websites)


