____ u__.r.. ______ Request, u.., urljoin, URLError
____ urllib.parse ______ urlparse
______ t___
______ _
______ queue
____ bs4 ______ BeautifulSoup
______ ssl

c_ Crawler(_.T..):

  ___  -   baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock):
    _.T... - (self);
    print("Web Crawler Worker Started: {}".format(_.current_thread()))
    linksToCrawl = linksToCrawl
    haveVisited = haveVisited
    baseUrl = baseUrl
    urlLock = urlLock
    errorLinks = errorLinks

  ___ run
    # We create this context so that we can crawl 
    # https sites
    myssl = ssl.create_default_context();
    myssl.check_hostname=False
    myssl.verify_mode=ssl.CERT_NONE
    # process all the links in our queue
    w... T..
      
      urlLock.a..
      print("Queue Size: {}".format(linksToCrawl.qsize()))
      link = linksToCrawl.g..
      urlLock.r..
      # have we reached the end of our queue?
      __ link is None:
        _____

      # Have we visited this link already?
      __ (link __ haveVisited):
        print("Already Visited: {}".format(link))
        _____
      
      try:
        link = urljoin(baseUrl, link)
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        response = u..(req, context=myssl)

        print("Url {} Crawled with Status: {}".format(response.geturl(), response.getcode()))
        
        soup = BeautifulSoup(response.r.. , "html.parser")
        
        ___ atag __ soup.find_all('a'):
          __ (atag.get('href') not __ haveVisited) and (urlparse(link).netloc == 'tutorialedge.net'):
            linksToCrawl.p..(atag.get('href'))
          else :
            print("{} already visited or not part of website".format(atag.get('href')))

        print("Adding {} to crawled list".format(link))
        haveVisited.a..(link)
        
      except URLError as e:
        print("URL {} threw this error when trying to parse: {}".format(link, e.reason))
        errorLinks.a..(link)
      finally:
        linksToCrawl.task_done()
  
    

___ main
  print("Starting our Web Crawler")
  baseUrl = input("Website > ")
  numberOfThreads = input("No Threads > ")

  linksToCrawl = queue.Q..()
  urlLock = _.L...()
  linksToCrawl.p..(baseUrl)
  haveVisited = []
  crawlers = []
  errorLinks = []

  ___ i __ r...(i..(numberOfThreads)):
    crawler = Crawler(baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock)
    crawler.s..
    crawlers.a..(crawler)

  ___ crawler __ crawlers:
    crawler.j..()

  print("Total Number of Pages Visited {}".format(l..(haveVisited)))
  print("Total Number of Pages with Errors {}".format(l..(errorLinks)))


__ _____ __ _____
  main()



