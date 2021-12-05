______ re
______ logging

____ locators.all_books_page ______ AllBooksPageLocators
____ parsers.book ______ BookParser
____ bs4 ______ BeautifulSoup

logger = logging.getLogger('scraping.all_books_page')


class AllBooksPage:
    ___ __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    ___ books(self):
        logger.debug(f'Finding all books in the page using `{AllBooksPageLocators.BOOKS}`')
        return [BookParser(e) ___ e __ self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    ___ page_count(self):
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        logger.info(f'Found number of catalogue pages available: `{content}`')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.info(f'Extracted number of pages as integer: `{pages}`.')
        return pages
