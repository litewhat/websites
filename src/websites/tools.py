from bs4 import BeautifulSoup
import re
import urllib.request

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def get_file_from_url(url):
    file = urllib.request.URLopener()
    file.retrieve(url, 'tmp.csv.zip')


def check_file_format(filepath):
    pass


def add_prefix(url):
    if not url.startswith('http://') or not url.startswith('https://'):
        url = 'http://' + url
    return url


def check_url(url):
    is_valid = re.match(regex, url)
    if is_valid is None:
        return None
    return url


def cut_get(url):
    return url.split('?')[0]


def get_website_data(html, *args):
    data = {}
    soup = BeautifulSoup(html, 'lxml')
    for arg in args:
        data[arg] = soup.find(arg)
    return data


def get_tag_from_html(html, tag):
    soup = BeautifulSoup(html, 'lxml')
    return soup.find(tag).string


def get_links_from_html(html):
    links = {}
    soup = BeautifulSoup(html, 'lxml')
    tagged_links = soup.find_all('a')
    _ = { link.get('href') for link in tagged_links }
    for link in _:
        link = cut_get(link)
        link = add_prefix(link)
        links.add(link)
    return links