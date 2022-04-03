____ c.. _______ n..

____ bs4 _______ BeautifulSoup __ Soup
_______ r__

CONTENT = r__.g.. 'http://bit.ly/2EN2Ntv').text

Book = n..('Book', 'title description image link')


___ get_book
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT)
    dotd = soup.find(id='deal-of-the-day')
    image_base = dotd.find(class_='dotd-main-book-image')
    title_base = dotd.find(class_='dotd-title')

    title = title_base.find('h2').text.s..
    description = title_base.parent.find_all('div')[2].text.s..
    image = image_base.find('img').attrs 'src'
    link = image_base.find('a').attrs 'href'

    r.. Book(title, description, image, link)
