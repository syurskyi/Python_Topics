from collections import namedtuple
from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""

    soup = Soup(CONTENT, 'html.parser')
    soup1 = soup.find('div', class_='dotd-main-book-summary float-left')
    soup2 = soup.find('div', class_='dotd-main-book-image float-left')

    title = soup1.find(class_='dotd-title').select('h2').__str__()
    title = title.split('\t')[15]

    description = soup1.select('div')[2].__str__()
    description = description.split('\t')[8]

    image = soup2.select('img')[0]['src']

    link = soup2.select('a')[0]['href']

    return Book(title=title, description=description,
                image=image, link=link)