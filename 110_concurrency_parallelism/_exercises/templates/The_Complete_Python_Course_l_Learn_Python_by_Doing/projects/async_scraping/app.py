"""
You can see when running this file, that the amount of time it takes for the requests is actually quite long—
and they don't seem to all happen at the same time.

That's because the toscrape websites actually limit us to a single connection at a time,
so making multiple requests using aiohttp and waiting for them to come back is completely useless.

Indeed, if we use a different site (e.g. you can try with http://google.com), you'll see the requests
all seem to happen at once.

The speed at which we can request pages is not only a product of the speed of our Python program, but
also the speed of the server giving us the responses back (and, in this case, any artificial limitations that
have been put in place to prevent us from making too many requests at once!).

Servers sometimes do this so that you can't make 1000 simultaneous requests and crash the server.
"""

______ _
______ aiohttp
______ async_timeout
______ requests
______ l__
______ t___

____ pages.all_books_page ______ AllBooksPage

l__.?(?_'%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]  _ m.. _,
                    datefmt='%d-%m-%Y %H:%M:%S',
                    ?_l__.D..
                    filename='logs.txt')
logger = l__.getLogger('scraping')

loop = _.get_event_loop()

print('Loading books list...')
logger.info('Loading books list.')

logger.info('Requesting http://books.toscrape.com')
page_content = requests.get('http://books.toscrape.com').content

logger.d..('Creating AllBooksPage from page content.')
page = AllBooksPage(page_content)

_books   # list


@ ___ fetch_page(session, url):
    page_start = t___.t___()
    logger.info(f'Requesting {url}')
    @ w__ session.get(url) __ response:
        print(f'{url} took {t___.t___() - page_start}')
        r.. await response.text()


@ ___ get_multiple_pages(loop, *urls):
    tasks   # list
    @ w__ aiohttp.ClientSession(loop=loop) __ session:
        ___ url __ urls:
            tasks.a..(fetch_page(session, url))
        r.. await _.gather(*tasks)


logger.info(f'Going through {page.page_count} pages of books...')

# other URLs to try:
# https://www.johnlewis.com/herman-miller-new-aeron-office-chair-graphite-polished-aluminium/p3177260
# http://google.com
urls = [f'http://books.toscrape.com/catalogue/page-{page_num+1}.html' ___ page_num __ r...(page.page_count)]
start = t___.t___()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'Total page requests took {t___.t___() - start}')
___ page_content __ pages:
    logger.d..('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    _books.extend(page.books)

books = _books
