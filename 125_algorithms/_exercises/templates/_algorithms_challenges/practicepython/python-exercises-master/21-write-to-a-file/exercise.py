#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
______ requests
from bs4 ______ BeautifulSoup


___ getPortions(soup
    # this is a generator
    heading = soup.find('div', {'class': 'deck'})
    __ heading:
        yield heading.text

    ___ p __ soup.find_all('p', {'class': ''}
        yield p.text


___ writePageToFile(url
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    name = input('Tell me the name of file in which page should be saved: ')

    open_file = open(name + '.txt', 'a')

    ___ element __ getPortions(soup
        open_file.write(element + '\n')

    open_file.close()

    print('\nArticle was saved in ' + name + '.txt file.')


__  -n __ '__main__':
    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    writePageToFile(url)
