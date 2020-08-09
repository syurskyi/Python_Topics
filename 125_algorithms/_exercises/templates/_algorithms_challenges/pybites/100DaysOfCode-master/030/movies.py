______ csv
from contextlib ______ contextmanager
______ os
from pprint ______ pprint as pp
______ sqlite3
______ sys

# Useful:
# A thorough guide to SQLite database operations in Python
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

DB = 'movies.sqlite'
CSV_FILE = 'data.csv'

# thanks Julian
# https://github.com/pybites/100DaysOfCode/blob/master/025/gen_testdb.py


@contextmanager
___ conn_db(
    try:
        conn = sqlite3.connect(DB)
        conn.row_factory = sqlite3.Row  # want dict rows, thanks Row
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.commit()
        conn.close()


___ clean_name(input_var
    # from rasbt article
    r_ ''.join(char for char in input_var __ char.isalnum())


___ read_csv(cf=CSV_FILE
    with open(cf, 'r') as csvfile:
        r_ list(csv.DictReader(csvfile))


___ create_db(table, col_names, overwrite=False
    __ overwrite:
        print('Recreating DB')
        __ os.path.isfile(DB
            os.remove(DB)

    idx = 'id INTEGER PRIMARY KEY AUTOINCREMENT,'

    with conn_db() as c:
        try:
            c.execute('CREATE TABLE {} ({} {})'.format(
                table, idx, ', '.join(col_names)))
        except sqlite3.OperationalError:
            print('Table already exists')


___ insert_movies(data
    cols = ', '.join(data[0].keys())
    placeholders = ', '.join(['?'] * le.(data[0]))

    with conn_db() as c:
        rows = [list(d.values()) for d in data]

        c.executemany('INSERT INTO movies ({}) VALUES ({})'.format(
            cols, placeholders), rows)


___ get_movies(
    with conn_db() as c:
        c.execute("SELECT * FROM movies;")
        for row in c.fetchall(
            yield dict(row)


___ get_movie_info(idx
    idx = clean_name(str(idx))
    with conn_db() as c:
        c.execute("SELECT * FROM movies WHERE id LIKE ?", (idx, ))
        r_ dict(c.fetchone())


__ __name__ __ '__main__':
    overwrite = '-r' in sys.argv[1:]

    data = read_csv()
    col_names = data[0].keys()

    create_db('movies', col_names, overwrite)

    insert_movies(data)

    movie = get_movie_info(111)
    pp(movie)
