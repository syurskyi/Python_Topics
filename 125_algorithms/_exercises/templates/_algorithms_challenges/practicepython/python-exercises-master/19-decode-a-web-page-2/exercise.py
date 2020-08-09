#! /usr/bin/env python

______ requests
from bs4 ______ BeautifulSoup


___ getPortions(soup
    # this is a generator
    heading = soup.find('div', {'class': 'deck'})
    __ heading:
        yield heading.text

    ___ p in soup.find_all('p', {'class': ''}
        yield p.text


___ readPage(url
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    ___ element in getPortions(soup
        print('\n%s' % element)
        input("\nPress 'Enter' to continue: ")

    print('\nEnd of article.')


__ __name__ __ '__main__':
    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    readPage(url)
