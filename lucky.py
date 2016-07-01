#! python3
# luvky.py -- Open several Google search results from
# command line or Clipboard

import requests, sys, webbrowser, bs4, os, pyperclip, time

print('Googling...') # display text while downloading the Google page

if len(sys.argv) > 1:
	# Get address from command line
	address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard.
	address = pyperclip.paste()

res = requests.get('http://google.com/search?q=' + address)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "lxml")

# Open a browser tab for each result.
linkElems = soup.select('.g .r a')
numOpen = min(5, len(linkElems))

webbrowser.get('google-chrome').open_new('http://google.com' + linkElems[0].get('href'))
for i in range(1, numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))

time.sleep(10)
sys.exit(0)