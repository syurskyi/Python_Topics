____ c.. _______ n..

____ bs4 _______ BeautifulSoup __ Soup
_______ r__

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = r__.g.. PACKT).text

Book = n..('Book', 'title description image link')


___ get_book
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    p..

    soup = Soup(CONTENT, 'html.parser')

    title = soup.find('div', class_='dotd-title').h2.text.s..

    description = soup.select('.dotd-main-book-summary div')[2].text.s..


    image = soup.find('img', class_="bookimage imagecache imagecache-dotd_main_image") 'src'

    link = soup.select(".dotd-main-book-image a")[0] 'href'

    r.. Book(title,description,image,link)


#print(main_book.prettify)

print(get_book