______ t___
____ u__.r.. ______ Request, URLError, urljoin, u..
____ concurrent.futures ______ ThreadPoolExecutor, as_completed

URLS = [
  'http://localhost:1313',
  'http://localhost:1313/about',
  'http://localhost:1313/get-involved/',
  'http://localhost:1313/series/blog/',
]

___ checkStatus(url):
  print("Attempting to crawl URL: {}".format(url))
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  response = u..(req)
  r.. response.getcode(), url

___ printStatus(statusCode):
  print("URL Crawled with status code: {}".format(statusCode))

___ main
  w__ ThreadPoolExecutor(max_workers=3) __ executor:
    
    tasks   # list
    ___ url __ URLS:
      task = executor.submit(checkStatus, (url))
      tasks.a..(task)

    ___ future __ as_completed(tasks):
      printStatus(future.result())

__ _____ __ _____
  main()
