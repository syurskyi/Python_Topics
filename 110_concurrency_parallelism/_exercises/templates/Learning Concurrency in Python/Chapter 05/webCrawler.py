____ u__.r.. ______ Request, u.., urljoin, URLError
____ urllib.parse ______ urlparse
______ t___
______ _
______ queue
____ bs4 ______ BeautifulSoup
______ ssl

class Crawler(_.T..):

  ___ __init__(self, baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock):
    _.T...__init__(self);
    print("Web Crawler Worker Started: {}".format(_.current_thread()))
    self.linksToCrawl = linksToCrawl
    self.haveVisited = haveVisited
    self.baseUrl = baseUrl
    self.urlLock = urlLock
    self.errorLinks = errorLinks

  ___ run(self):
    # We create this context so that we can crawl 
    # https sites
    myssl = ssl.create_default_context();
    myssl.check_hostname=False
    myssl.verify_mode=ssl.CERT_NONE
    # process all the links in our queue
    w... T..
      
      self.urlLock.a..
      print("Queue Size: {}".format(self.linksToCrawl.qsize()))
      link = self.linksToCrawl.get()
      self.urlLock.r..
      # have we reached the end of our queue?
      __ link is None:
        _____

      # Have we visited this link already?
      __ (link __ self.haveVisited):
        print("Already Visited: {}".format(link))
        _____
      
      try:
        link = urljoin(self.baseUrl, link)
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        response = u..(req, context=myssl)

        print("Url {} Crawled with Status: {}".format(response.geturl(), response.getcode()))
        
        soup = BeautifulSoup(response.read(), "html.parser")
        
        ___ atag __ soup.find_all('a'):
          __ (atag.get('href') not __ self.haveVisited) and (urlparse(link).netloc == 'tutorialedge.net'):
            self.linksToCrawl.put(atag.get('href'))
          else :
            print("{} already visited or not part of website".format(atag.get('href')))

        print("Adding {} to crawled list".format(link))
        self.haveVisited.append(link)
        
      except URLError as e:
        print("URL {} threw this error when trying to parse: {}".format(link, e.reason))
        self.errorLinks.append(link)
      finally:
        self.linksToCrawl.task_done()
  
    

___ main
  print("Starting our Web Crawler")
  baseUrl = input("Website > ")
  numberOfThreads = input("No Threads > ")

  linksToCrawl = queue.Queue()
  urlLock = _.L...()
  linksToCrawl.put(baseUrl)
  haveVisited = []
  crawlers = []
  errorLinks = []

  ___ i __ r...(int(numberOfThreads)):
    crawler = Crawler(baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock)
    crawler.s..
    crawlers.append(crawler)

  ___ crawler __ crawlers:
    crawler.join()

  print("Total Number of Pages Visited {}".format(len(haveVisited)))
  print("Total Number of Pages with Errors {}".format(len(errorLinks)))


__ _____ __ _____
  main()



