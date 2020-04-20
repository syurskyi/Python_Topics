______ urllib2
______ time
from BeautifulSoup ______ BeautifulSoup

linkArray = []

def getLinks():
  req = urllib2.urlopen('http://www.example.com')
  soup = BeautifulSoup(req.read())
  for link in soup.findAll('a'):
    linkArray.append(link.get('href'))
    print(len(linkArray))

getLinks()
