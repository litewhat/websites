import csv, json, re

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

url_prefix = 'http://'
data = []

with open('data.csv', newline='') as f:
	reader = csv.DictReader(f, fieldnames=['alexa_rank', 'url'], delimiter=',')
	for row in reader:
		row['url'] = row['url'].lstrip()
		row['url'] = url_prefix + row['url']
		result = re.search(regex, row['url'])
		print(result)
		data.append((row['alexa_rank'], row['url']))

print(data)
print(json.dumps(data))


