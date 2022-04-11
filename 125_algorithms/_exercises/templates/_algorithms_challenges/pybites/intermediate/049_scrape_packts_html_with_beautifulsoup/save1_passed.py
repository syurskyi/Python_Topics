____ c.. _______ n..
____ bs4 _______ BeautifulSoup __ Soup
_______ r__

PACKT 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT r__.g.. PACKT).text

Book n..('Book', 'title description image link')


___ get_book
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""

    soup Soup(CONTENT, 'html.parser')
    soup1 soup.find('div', class_='dotd-main-book-summary float-left')
    soup2 soup.find('div', class_='dotd-main-book-image float-left')

    title soup1.find(class_='dotd-title').select('h2').-s()
    title title.s..('\t')[15]

    description soup1.select('div')[2].-s()
    description description.s..('\t')[8]

    image soup2.select('img')[0] 'src'

    link soup2.select('a')[0] 'href'

    r.. Book(title=title, d.._description,
                image=image, link=link)