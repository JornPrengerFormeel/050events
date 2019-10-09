#problemen met ascii characters verholpen
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#bro
import textwrap
import requests
import csv
from bs4 import BeautifulSoup

#de pagina laden
url = "https://www.simplon.nl"
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

lijst_van_divs = soup.select('a.item')

for enkele_div in lijst_van_divs:
	#location, title, date
	print 'Location: Simplon'
	print 'Title: ' + str(enkele_div.select_one('div.title').text).replace('\t',' ')
	print 'Date: ' + str(enkele_div.select_one('div.date').text.replace('\n', ' '))
	
	#define details general
	rough_details = str(enkele_div.select_one('div.details').text) + 'eGenre'
	details = rough_details.replace('\n', ' ')
	#print details
	
	#location
	sLocation = 'Waar: '
	eLocation = 'Open:'
	print 'Sub-location: ' + details[details.find(sLocation)+len(sLocation):details.rfind(eLocation)]
	
	#time
	sTime = 'Open: '
	eTime = 'VVK:'
	print 'Time: ' + details[details.find(sTime)+len(sTime):details.rfind(eTime)]
	
	#price
	sPrice = 'DVK: '
	ePrice = 'Aanvang:'
	print 'Price: ' + details[details.find(sPrice)+len(sPrice):details.rfind(ePrice)]
	
	#genre
	sGenre = 'Genre: '
	eGenre = 'eGenre'
	print 'Genre: ' + details[details.find(sGenre)+len(sGenre):details.rfind(eGenre)]
	
	#print('Details: ' + textwrap.dedent(details).replace('    ', '').replace('\n', ''))

	print('\n')
