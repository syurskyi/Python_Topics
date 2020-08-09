from threading ______ Thread
from Queue ______ Queue
from urlparse ______ urlparse

queue = Queue()
results = {}

class CrawlerThread(Thread
    ___ run(self
        global queue, results
        w___ True:
            url = queue.get()
            __ url not in results \
                and urlparse(url).hostname.endswith("wikipedia.org"
                results[url] = True
                urls = HtmlHelper.parseUrls(url)
                ___ url in urls:
                    queue.put(url)
            queue.task_done()


#class HtmlHelper:
#    @classmethod
#    ___ parseUrls(cls, url)
#       # Get all urls from a webpage of given url.
class Solution:
    # @param {string} url a url of root page
    # @return {string[]} all urls
    ___ crawler(self, url
        # Write your code here
        global queue, results
        thread_pools = []
        ___ i in xrange(10
            thread_pools.append(CrawlerThread())
            thread_pools[i].setDaemon(True)
            thread_pools[i].start()

        queue.put(url)

        queue.join()
        rt = []
        ___ key, value in results.items(
            rt.append(key)
        r_ rt
