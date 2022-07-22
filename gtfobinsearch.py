import argparse
from bs4 import BeautifulSoup
import requests

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Input file of binaries")
args = parser.parse_args()


url = 'https://gtfobins.github.io'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 

urls = []
for link in soup.find_all('a'):
    urls.append(url+link.get('href'))

#get rid of extra hrefs
for _ in range(23): 
	urls.pop(0); 
	#urls.pop()



binlist=[]
def readfile(sf):
	with open(sf, "r") as sf:
		for line in sf:
			line = line.split("/")
			binlist.append(line[len(line)-1])

def gtfocheck():
	for binary in binlist:
		for url in urls:
			urlsp = url.split("/")
			if binary == urlsp[4]:
				print(url)

readfile(args.file)
gtfocheck()

