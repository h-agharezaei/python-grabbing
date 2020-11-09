import bs4
import re
import time
from urllib.request import urlopen

url = 'http://classic.austlii.edu.au/au/legis/cth/consol_act/ma1958118'

html = urlopen(url).read()
soup = bs4.BeautifulSoup(html ,"lxml")
for link in soup.find_all('a', href=True ):
    #link.text
    href = link['href']
    if(re.match(r'^s\d*\w+(.html)$',href, re.M|re.I)):
        #print(href)
        html1 = urlopen(url+'/'+href).read()
        soup1 = bs4.BeautifulSoup(html1 ,"lxml")
        title = soup1.find('b' ).text;
        print(title)
        h3 = soup1.find('h3' ).text;
        print(h3)
        for p in soup1.find_all('p'):
            print(p.text)
       
        print('\n---------------------------------\n')
        time.sleep(3 )
