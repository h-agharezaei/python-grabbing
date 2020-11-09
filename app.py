import bs4
import re
import time
from urllib.request import urlopen

class sects:  
    def __init__(self,id, rank, type,body):  
        self.id = id  
        self.rank = rank  
        self.type = type  
        self.body = body
   
# creating list        
list = []

counter = 1
url = 'http://classic.austlii.edu.au/au/legis/cth/consol_act/ma1958118'

html = urlopen(url).read()
soup = bs4.BeautifulSoup(html ,"lxml")
for link in soup.find_all('a', href=True ):
    #link.text
    counter += 10
    href = link['href']
    if(re.match(r'^s\d*\w+(.html)$',href, re.M|re.I)):
        #print(href)
        html1 = urlopen(url+'/'+href).read()
        soup1 = bs4.BeautifulSoup(html1 ,"lxml")
        title = '<h2>' + soup1.find('b' ).text +'</h2>';
        list.append( sects(href,counter,'title', title) ) 
        counter += 1
        #print(title)
        h3 =  '<span><strong>' + soup1.find('h3' ).text +'</strong><span>';
        list.append( sects(href,counter,'b', h3) ) 
        counter += 1
        #print(h3)
        body = ''
        for p in soup1.find_all('p'):
            body1 = p.text
            for link1 in p.find_all('a', href=True):
                body1 = body1.replace(link1.text, '<a href="'+link1['href']+'">'+ link1.text + '</a>')
            body += body1
        list.append( sects(href,counter,'body', body) ) 
        counter += 1
        #print('\n---------------------------------\n')
        #time.sleep(1 )
        
for obj in list: 
    print( obj.id, obj.rank,obj.type, obj.body, sep ='      \n' )
