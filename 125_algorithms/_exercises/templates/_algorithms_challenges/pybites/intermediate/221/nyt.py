_______ r__

YOUR_KEY = '123abc'
DEFAULT_LIST = 'hardcover-nonfiction'

URL_NON_FICTION =  _*https://api.nytimes.com/svc/books/v3/lists/current/'
                   f'{DEFAULT_LIST}.json?api-key={YOUR_KEY}')
URL_FICTION = URL_NON_FICTION.r..('nonfiction', 'fiction')


___ get_best_seller_titles(url=URL_NON_FICTION
    """Use the NY Times Books API endpoint above to get the titles that are
       on the best seller list for the longest time.

       Return a list of (title, weeks_on_list) tuples, e.g. for the nonfiction:

       [('BETWEEN THE WORLD AND ME', 86),
        ('EDUCATED', 79),
        ('BECOMING', 41),
        ('THE SECOND MOUNTAIN', 18),
         ... 11 more ...
       ]

       Dev docs: https://developer.nytimes.com/docs/books-product/1/overview
    """
    base_url = 'https://api.nytimes.com/svc/books/v3'


    url = f"{base_url}/lists/hardcover-nonfiction.json"
        
    params = {'api-key': N..}
    

    books    # list
    ___
        response = r__.g.. url,params=params)
        response.raise_for_status()
    ______ r__.HTTPError __ e:
        print('HTTP Error')
        print(e)
    ______ E.. __ e:
        print('Other exception')
        print(e)
    ____:
        results = response.j..


        ___ book __ results 'results'  'books' :
            books.a..((book 'title' ,book 'weeks_on_list'
        r.. books
        











__ _____ __ _____
    ret = get_best_seller_titles()
    print(ret)
