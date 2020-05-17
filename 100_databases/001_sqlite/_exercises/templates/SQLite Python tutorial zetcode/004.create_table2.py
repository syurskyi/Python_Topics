_____ ? as sqlite

cars _ (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

con _ sqlite.c..('ydb.db')

with con:

    cur _ con.cursor()

    cur.e..("DROP TABLE IF EXISTS cars")
    cur.e..("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)