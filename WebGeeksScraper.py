import requests
from bs4 import BeautifulSoup
from pprint import pprint
url = 'https://webgeeks-2.herokuapp.com/web5.html'
resp = requests.get(url=url)
class_list = set()
soup = BeautifulSoup(resp.content,"html.parser")
foundu = soup.findAll("a", href=True)
found = [url + i['href'] for i in soup.findAll("a")]
#print(found)
tags = {tag.name for tag in soup.find_all()}
for tag in tags:
  
    # find all element of tag
    for i in soup.find_all( tag ):
        #print("running for loop")
        # if tag has attribute of class
        if i.has_attr( "class" ):
            
            
            if len( i['class'] ) != 0:
                #print(i['class'])
                class_list.add(" ".join( i['class']))
  
print( class_list )