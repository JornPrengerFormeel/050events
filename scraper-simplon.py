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

open('data.txt', 'w').close()

for enkele_div in lijst_van_divs:
	data = open('data.txt','a')

	#location, title, date
	print 'Location: Simplon'
	print 'Title: ' + str(enkele_div.select_one('div.title').text).replace('\t',' ')
	print 'Date: ' + str(enkele_div.select_one('div.date').text.replace('\n', ' '))

	#location, title, date
	data.write( 'Simplon\n' )
	data.write( str(enkele_div.select_one('div.title').text.replace('\t',' ')) + '\n')
	data.write( str(enkele_div.select_one('div.date').text.replace('\n', ' ')) + '\n')

	#define details general
	rough_details = str(enkele_div.select_one('div.details').text) + 'eGenre'
	details = rough_details.replace('\n', ' ')
	print details
	#data.write(details)


	#location
	sLocation = 'Waar: '
	eLocation = 'Open:'
	print 'Sub-location: ' + details[details.find(sLocation)+len(sLocation):details.rfind(eLocation)]
	data.write( details[details.find(sLocation)+len(sLocation):details.rfind(eLocation)] + '\n')


	#time
	sTime = 'Open: '
	eTime = 'VVK:'
	print 'Time: ' + details[details.find(sTime)+len(sTime):details.rfind(eTime)]
	data.write( details[details.find(sTime)+len(sTime):details.rfind(eTime)] + '\n')


	#price
	sPrice = 'VVK: '
	ePrice = 'Aanvang:'
	print 'Price: ' + details[details.find(sPrice)+len(sPrice):details.rfind(ePrice)]
	data.write( details[details.find(sPrice)+len(sPrice):details.rfind(ePrice)] + '\n')


	#genre
	sGenre = 'Genre: '
	eGenre = 'eGenre'
	print 'Genre: ' + details[details.find(sGenre)+len(sGenre):details.rfind(eGenre)]
	data.write( details[details.find(sGenre)+len(sGenre):details.rfind(eGenre)] + '\n')



	print('\n')
	data.write('\n')

data.close()
