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
    print('Getting file from url: {}'.format(url))
    file = urllib.request.URLopener()
    file.retrieve(url, 'tmp.csv.zip')
    # debug
    print('Done.')


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


