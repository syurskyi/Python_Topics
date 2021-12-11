____ u__.r.. ______ Request, u.., urljoin, URLError
____ urllib.parse ______ urlparse
______ t___
______ _
______ queue
____ bs4 ______ BeautifulSoup
______ ssl

c_ Crawler(_.T..):

  ___  -   baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock):
    _.T... - ;
    print("Web Crawler Worker Started: {}".f..(_.current_thread()))
    linksToCrawl = linksToCrawl
    haveVisited = haveVisited
    baseUrl = baseUrl
    urlLock = urlLock
    errorLinks = errorLinks

  ___ run
    # We create this context so that we can crawl 
    # https sites
    myssl = ssl.create_default_context();
    myssl.check_hostname=F..
    myssl.verify_mode=ssl.CERT_NONE
    # process all the links __ our queue
    w... T..
      
      urlLock.a..
      print("Queue Size: {}".f..(linksToCrawl.qsize()))
      link = linksToCrawl.g..
      urlLock.r..
      # have we reached the end of our queue?
      __ link __ N..:
        _____

      # Have we visited this link already?
      __ (link __ haveVisited):
        print("Already Visited: {}".f..(link))
        _____
      
      ___
        link = urljoin(baseUrl, link)
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        response = u..(req, context=myssl)

        print("Url {} Crawled with Status: {}".f..(response.geturl(), response.getcode()))
        
        soup = BeautifulSoup(response.r.. , "html.parser")
        
        ___ atag __ soup.find_all('a'):
          __ (atag.get('href') n.. __ haveVisited) a.. (urlparse(link).netloc == 'tutorialedge.net'):
            linksToCrawl.p..(atag.get('href'))
          else :
            print("{} already visited or not part of website".f..(atag.get('href')))

        print("Adding {} to crawled list".f..(link))
        haveVisited.a..(link)
        
      _____ URLError __ e:
        print("URL {} threw this error when trying to parse: {}".f..(link, e.reason))
        errorLinks.a..(link)
      ______
        linksToCrawl.task_done()
  
    

___ main
  print("Starting our Web Crawler")
  baseUrl = i..("Website > ")
  numberOfThreads = i..("No Threads > ")

  linksToCrawl = queue.Q..()
  urlLock = _.L...()
  linksToCrawl.p..(baseUrl)
  haveVisited   # list
  crawlers   # list
  errorLinks   # list

  ___ i __ r...(i..(numberOfThreads)):
    crawler = Crawler(baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock)
    crawler.s..
    crawlers.a..(crawler)

  ___ crawler __ crawlers:
    crawler.j..()

  print("Total Number of Pages Visited {}".f..(l..(haveVisited)))
  print("Total Number of Pages with Errors {}".f..(l..(errorLinks)))


__ _____ __ _____
  main()



