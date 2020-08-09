from pprint ______ pprint as pp
______ sys

______ requests
______ requests_cache

from templates ______ TEMPLATE, HTML_TEMPLATE

OMDB = 'http://www.omdbapi.com'
OMDB_BY_IMDB = OMDB + '/?i={imdb}'
OMDB_BY_TITLE_YEAR = OMDB + '/?t={title}&y={year}'

# cache repeated calls to OMDB (not sure about API limits)
requests_cache.install_cache()


___ query_omdb(**kwargs
    __ 'imdb' in kwargs:
        url = OMDB_BY_IMDB.format(**kwargs)
    ____
        url = OMDB_BY_TITLE_YEAR.format(**kwargs)
    r_ requests.get(url).json()


__ __name__ __ '__main__':
    args = sys.argv[1:]
    html = True __ '-h' in args else False
    verbose = True __ '-v' in args else False
    answer = None

    print('Script to query OMDb API')

    w___ answer != 'q':
        answer = input('Enter IMDB ID or title (q to exit ').lower()
        params = dict()

        __ answer __ 'q':
            print('Bye')
            break
        ____ 'tt' in answer:
            params['imdb'] = answer
        ____
            params['title'] = answer
            params['year'] = input('Year of release? ')

        resp = query_omdb(**params)
        __ verbose:
            pp(resp)

        __ 'Error' in resp:
            print('Error: {}'.format(resp['Error']))
        ____
            tmpl = HTML_TEMPLATE __ html else TEMPLATE
            print(tmpl.format(**dict(resp)))
