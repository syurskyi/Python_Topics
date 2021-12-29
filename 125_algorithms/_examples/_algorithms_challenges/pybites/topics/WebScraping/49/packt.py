from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    pass

    soup = Soup(CONTENT, 'html.parser')

    title = soup.find('div', class_='dotd-title').h2.text.strip()

    description = soup.select('.dotd-main-book-summary div')[2].text.strip()


    image = soup.find('img', class_="bookimage imagecache imagecache-dotd_main_image")['src']

    link = soup.select(".dotd-main-book-image a")[0]['href']

    return Book(title,description,image,link)


#print(main_book.prettify)

print(get_book())