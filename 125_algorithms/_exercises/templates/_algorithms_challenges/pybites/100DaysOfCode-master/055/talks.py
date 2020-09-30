from collections ______ namedtuple
______ os
______ sqlite3
______ sys

from bs4 ______ BeautifulSoup as soup

from db ______ conn_db, DB

BASE_URL = 'https://us.pycon.org'
TABLE = 'talks'

Talk = namedtuple('Talk', 'title speaker description url')


___ get_soup(html='index.html'
    r_ soup(open(html).read(), 'html.parser')


___ parse_talks(s
    ___ talk __ s.find_all(attrs={'class': 'slot-talk'}
        title = talk.a.text
        speaker = talk.find(attrs={'class': 'speaker'}).text.strip()
        description = talk.a.get('title').strip()
        url = BASE_URL + talk.a.get('href')
        yield Talk(title=title,
                   speaker=speaker,
                   description=description,
                   url=url)


___ create_table(
    cols = ', '.join(Talk._fields)
    idx = 'id INTEGER PRIMARY KEY AUTOINCREMENT,'

    with conn_db() as c:
        try:
            c.execute('CREATE TABLE {} ({} {})'.format(
                TABLE, idx, cols))
        except sqlite3.OperationalError:
            print('Table already exists')


___ store_talks(talks
    cols = Talk._fields

    placeholders = ', '.join(['?'] * le.(cols))

    with conn_db() as c:
        c.executemany('INSERT INTO {} ({}) VALUES ({})'.format(
            TABLE, ', '.join(cols), placeholders), talks)


__  -n __ '__main__':
    s = get_soup()
    talks = parse_talks(s)

    __ os.path.isfile(DB
        print('{} already exists'.format(DB))
        sys.exit(1)

    create_table()
    store_talks(talks)
