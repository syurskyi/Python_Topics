import u__.r..
import time
from bs4 import BeautifulSoup

t0 = time.time()
req = u__.r...urlopen('http://www.example.com')
t1 = time.time()
print("Total Time To Fetch Page: {} Seconds".format(t1-t0))
soup = BeautifulSoup(req.read(), "html.parser")

for link in soup.find_all('a'):
  print(link.get('href'))


t2 = time.time()
print("Total Execeution Time: {} Seconds".format)