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

site = open('site.html', 'w')

body = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="theme.css">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css">
</head>
<body>
    <div id="column">
        <div id="home">
            <div id="agenda">
                <div class="agenda-header">
                    <div class="titel">programma</div>
                </div>
                <div class="agenda-content">
"""

site.write(body)

for enkele_div in lijst_van_divs:
    data = open('site.html','a')
    #item-detatils
    data.write( '                   <div class = "item-block">\n')
    data.write( '                       <div class = "item-details">\n')
    #location, title, date
    data.write( '                           <div class="title">' + str(enkele_div.select_one('div.title').text.replace('\t',' ')) + '</div>' + '\n')
    data.write( '                           <div class="venue">' + 'Simplon' + '</div>' + '\n')
    data.write( '                           <div class="date">' + str(enkele_div.select_one('div.date').text.replace('\n', ' ')) + '</div>' + '\n')

    #define details general
    rough_details = str(enkele_div.select_one('div.details').text) + 'eGenre'
    details = rough_details.replace('\n', ' ')
    #data.write(details)

    data.write( '                           <div class = "details">' + '\n')

    #location
    sLocation = 'Waar: '
    eLocation = 'Open:'
    data.write( '                               <div class="location">' + details[details.find(sLocation)+len(sLocation):details.rfind(eLocation)] + '</div>' + '\n')

    #time
    sTime = 'Open: '
    eTime = 'VVK:'
    data.write( '                               <div class="open">' + details[details.find(sTime)+len(sTime):details.rfind(eTime)] + '</div>' + '\n')

    #price
    sPrice = 'VVK: '
    ePrice = 'Aanvang:'
    data.write( '                               <div class="price">' + details[details.find(sPrice)+len(sPrice):details.rfind(ePrice)] + '</div>' + '\n')

    #genre
    sGenre = 'Genre: '
    eGenre = 'eGenre'
    data.write( '                               <div class="genre">' + details[details.find(sGenre)+len(sGenre):details.rfind(eGenre)] + '</div>' + '\n')

    data.write( '                           </div>\n' )
    data.write( '                       </div>\n' )
    data.write( '                   </div>\n' )

end = """
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""
data.write(end)

data.close()
site.close()
