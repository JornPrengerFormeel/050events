#problemen met ascii characters verholpen
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#hoe noem je mensen die vanuit het westen naar het noorden komen?
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
    print('Title: ' + str(enkele_div.select_one('div.title').text).replace('\t',' '))
    print('Date: ' + str(enkele_div.select_one('div.date').text.replace('\n', ' ')))
    print('Location: ' + str(enkele_div.select_one('div.details').text))
    print('\n')
