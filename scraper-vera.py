#problemen met ascii characters verholpen
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#hoe noem je mensen die vanuit het westen naar het noorden komen?
import requests
import csv
from bs4 import BeautifulSoup

#de pagina laden
url = "https://www.vera-groningen.nl/programma/"
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

lijst_van_divs = soup.select('a.vert-aligneable-container')

for enkele_div in lijst_van_divs:
    print('Title: ' + str(enkele_div.select_one('h3.artist').text).replace('\t',' '))
    print('Date: ' + str(enkele_div.select_one('div.date').text.replace('\n', ' ')))
    print('Location: Vera, ' + str(enkele_div.select_one('div.schedule').text.replace(' | ','\n')))
    print('\n')
