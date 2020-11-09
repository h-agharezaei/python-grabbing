import bs4
import re
import time
from urllib.request import urlopen

class sects:  
    def __init__(self,id, rank, title, h3,body):  
        self.id = id  
        self.rank = rank  
        self.title = title  
        self.h3 = h3 
        self.body = body
   
# creating list        
list = []

counter = 10
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
        #print(title)
        h3 = soup1.find('h3' ).text;
        #print(h3)
        body = ''
        for p in soup1.find_all('p'):
            body1 = p.text
            for link1 in p.find_all('a', href=True):
                body1 = body1.replace(link1.text, '<a href="'+link1['href']+'">'+ link1.text + '</a>')
            body += body1
        list.append( sects(href,counter,title,h3, body) ) 
        counter += 1
        #print('\n---------------------------------\n')
        time.sleep(1 )
        
for obj in list: 
    print( obj.id, obj.rank,obj.title,obj.h3,obj.body, sep =' ' )
