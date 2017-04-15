import urllib.request


def get_file_from_url(url):
    print('Getting file from url: {}'.format(url))
    file = urllib.request.URLopener()
    file.retrieve(url, 'tmp.csv.zip')
    # debug
    print('Done.')


def check_file_format(filepath):
    pass


