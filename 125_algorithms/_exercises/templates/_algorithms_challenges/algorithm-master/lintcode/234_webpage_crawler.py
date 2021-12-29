____ threading _______ Thread
____ Queue _______ Queue
____ urlparse _______ urlparse

queue = Queue()
results = {}

class CrawlerThread(Thread):
    ___ run(self):
        global queue, results
        w... T...
            url = queue.get()
            __ url n.. __ results \
                a.. urlparse(url).hostname.endswith("wikipedia.org"):
                results[url] = True
                urls = HtmlHelper.parseUrls(url)
                ___ url __ urls:
                    queue.put(url)
            queue.task_done()


#class HtmlHelper:
#    @classmethod
#    def parseUrls(cls, url)
#       # Get all urls from a webpage of given url.
class Solution:
    # @param {string} url a url of root page
    # @return {string[]} all urls
    ___ crawler(self, url):
        # Write your code here
        global queue, results
        thread_pools    # list
        ___ i __ xrange(10):
            thread_pools.a..(CrawlerThread())
            thread_pools[i].setDaemon(True)
            thread_pools[i].start()

        queue.put(url)

        queue.join()
        rt    # list
        ___ key, value __ results.items():
            rt.a..(key)
        r.. rt
