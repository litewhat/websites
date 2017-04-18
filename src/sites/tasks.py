from __future__ import absolute_import, unicode_literals
from celery import shared_task
from websites.tools import add_prefix, check_url, get_from_url, get_links_from_html

import csv
import json
import urllib.request
from zipfile import ZipFile


@shared_task
def get_file_from_url(url, filename='tmp.csv.zip'):
    file = urllib.request.URLopener()
    file.retrieve(url, filename
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
    '''
    Takes csv file as parameter and returns json file with websites.
    '''
    websites = []
    with open(filename, newline='') as csvfile:
        websites_reader = csv.DictReader(csvfile, fieldnames=['alexa_rank', 'url'], delimiter=',')
        for row in websites_reader:
            row['url'] = row['url'].lstrip()
            row['url'] = add_prefix(row['url'])
            row['url'] = check_url(row['url'])
            if row['url'] is None:
                continue
            websites.append({
                'alexa_rank': row['alexa_rank'],
                'url':        row['url']
            })
    return json.dumps(websites)


@shared_task
def scan_website(url):
    html_cont = None
    with urllib.request.urlopen(url) as f:
        html_cont = f.read()
    return html_cont


@shared_task
def scan_websites(websites):
    # TODO: description is 'default'. Have to change it.
    rows = json.loads(websites)
    for row in rows:
        html = scan_website(row['url'])
        row['title'] = get_from_url(html, 'title')
        row['description'] = 'default'
        hyperlinks = get_links_from_html(html)

