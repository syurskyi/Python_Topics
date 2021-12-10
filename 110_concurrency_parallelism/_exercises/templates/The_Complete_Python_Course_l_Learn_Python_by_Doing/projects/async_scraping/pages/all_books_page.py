______ __
______ l__

____ locators.all_books_page ______ AllBooksPageLocators
____ parsers.book ______ BookParser
____ bs4 ______ BeautifulSoup

logger = l__.getLogger('scraping.all_books_page')


c_ AllBooksPage:
    ___  -   page):
        logger.d..('Parsing page content with BeautifulSoup HTML parser.')
        soup = BeautifulSoup(page, 'html.parser')

    @property
    ___ books
        logger.d..(f'Finding all books in the page using `{AllBooksPageLocators.BOOKS}`')
        r.. [BookParser(e) ___ e __ soup.select(AllBooksPageLocators.BOOKS)]

    @property
    ___ page_count
        logger.d..('Finding all number of catalogue pages available...')
        content = soup.select_one(AllBooksPageLocators.PAGER).string
        logger.info(f'Found number of catalogue pages available: `{content}`')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = __.s..(pattern, content)
        pages = i..(matcher.g..(1))
        logger.info(f'Extracted number of pages as integer: `{pages}`.')
        r.. pages
