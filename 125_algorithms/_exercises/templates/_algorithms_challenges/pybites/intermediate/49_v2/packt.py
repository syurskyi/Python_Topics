from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


___ get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""


    soup = Soup(CONTENT,"html.parser")

    title = soup.find('div',class_='dotd-title').getText(strip=True)
    description = soup.select_one('div[class="dotd-main-book-summary float-left"] > div:nth-child(4)').getText(strip=True)

    link = soup.select_one('div.dotd-main-book-image > a')['href']
    image = soup.select_one('div.dotd-main-book-image > a > img')['data-original']


    return Book(title,description,image,link)

