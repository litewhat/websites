from bs4 import BeautifulSoup
import urllib.request

def scan_website():
	html_cont = None
	with urllib.request.urlopen('http://wp.pl') as f:
		html_cont = f.read()
	return html_cont

html = scan_website()

def get_website_data(html, *args):
    data = {}
    soup = BeautifulSoup(html, 'html.parser')
    for arg in args:
        data[arg] = soup.find_all(arg)
    return data
