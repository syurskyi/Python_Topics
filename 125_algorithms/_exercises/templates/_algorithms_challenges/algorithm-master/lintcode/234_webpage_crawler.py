____ threading _______ Thread
____ Queue _______ Queue
____ urlparse _______ urlparse

queue = Queue()
results    # dict

c_ CrawlerThread(Thread):
    ___ run
        global queue, results
        w... T...
            url = queue.get()
            __ url n.. __ results \
                a.. urlparse(url).hostname.endswith("wikipedia.org"):
                results[url] = T..
                urls = HtmlHelper.parseUrls(url)
                ___ url __ urls:
                    queue.put(url)
            queue.task_done()


#class HtmlHelper:
#    @classmethod
#    def parseUrls(cls, url)
#       # Get all urls from a webpage of given url.
c_ Solution:
    # @param {string} url a url of root page
    # @return {string[]} all urls
    ___ crawler  url):
        # Write your code here
        global queue, results
        thread_pools    # list
        ___ i __ x..(10):
            thread_pools.a..(CrawlerThread())
            thread_pools[i].setDaemon(T..)
            thread_pools[i].start()

        queue.put(url)

        queue.j..()
        rt    # list
        ___ key, value __ results.i..:
            rt.a..(key)
        r.. rt
