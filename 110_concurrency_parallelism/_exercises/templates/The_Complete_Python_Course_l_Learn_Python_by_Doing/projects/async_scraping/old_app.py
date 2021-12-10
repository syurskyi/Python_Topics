______ requests
______ l__
______ t___

____ pages.all_books_page ______ AllBooksPage

l__.?(?_'%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]  _ m.. _,
                    datefmt='%d-%m-%Y %H:%M:%S',
                    ?_l__.INFO,
                    filename='logs.txt')
logger = l__.getLogger('scraping')

print('Loading books list...')
logger.info('Loading books list.')

logger.info('Requesting http://books.toscrape.com')
page_content = requests.get('http://books.toscrape.com').content

logger.d..('Creating AllBooksPage from page content.')
page = AllBooksPage(page_content)

_books   # list

start = t___.t___()
logger.info(f'Going through {page.page_count} pages of books...')
___ page_num __ r...(page.page_count):
    page_start = t___.t___()
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    logger.info(f'Requesting {url}')
    page_content = requests.get(url).content
    logger.d..('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    print(f'{url} took {t___.t___() - page_start}')
    _books.extend(page.books)
print(f'Total took {t___.t___() - start}')

books = _books
