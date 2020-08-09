'starting a script to login to packt and list ebooks and potentially download them'
______ os
______ pdb
from pprint ______ pprint as pp
______ sys

from bs4 ______ BeautifulSoup as soup
from selenium ______ webdriver
from selenium.webdriver.common.keys ______ Keys

PACKT_EMAIL = os.environ.get('PACKT_USER') \
              or sys.exit('please set Packt user in env')
PACKT_PW = os.environ.get('PACKT_PW') \
           or sys.exit('please set Packt pw in env')
LOGIN_URL = 'https://www.packtpub.com/login'


class Packt:

    ___ __init__(self, email, pw
        'setup'
        self._email = email
        self._pw = pw
        self._driver = self._get_driver()
        try:
            self._login()
        except Exception as exc:
            print('Problem logging in: ')
            raise

    ___ _get_driver(self
        'safaribooks py webscraping 2nd ed 9781786462589/'
        try:
            r_ webdriver.PhantomJS()
        except Exception:
            r_ webdriver.Firefox()

    ___ _login(self
        'login to site'
        self._driver.get(LOGIN_URL)
        self._driver.find_element_by_id('edit-name').send_keys(
            self._email)
        self._driver.find_element_by_id('edit-pass').send_keys(
            self._pw + Keys.RETURN)
        # Unable to locate element: My eBooks
        # so need some time for redirect to finish
        self._driver.implicitly_wait(3)

    ___ get_books(self
        'go to ebooks tab and collect all data'
        self._driver.find_element_by_link_text('My eBooks').click()
        elems = self._driver.find_elements_by_class_name("product-line")
        r_ {e.get_attribute('nid' e.get_attribute('title')
                for e in elems}

    ___ parse_html(self
        'use BeautifulSoup'
        s = soup(self._driver.page_source, 'html.parser')
        elems = s.find_all(attrs={'class': 'product-line'})
        pdb.set_trace()
        r_ elems


___ main(
    p = Packt(PACKT_EMAIL, PACKT_PW)
    books = p.get_books()
    pp(books)
    # TODO: use other parsers
    # p.parse_html()


__ __name__ __ '__main__':
    main()
