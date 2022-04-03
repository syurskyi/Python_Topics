import u__.r..
import time

t0 = time.time()
req = u__.r...urlopen('http://www.example.com')
pageHtml = req.read()
t1 = time.time()
print("Total Time To Fetch Page: {} Seconds".format(t1-t0))