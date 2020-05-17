#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

con _ w..
fout _ w..

___

    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

    cur _ con.c..
    fout _ o..('cars.csv', 'w')
    cur.copy_to(fout, 'cars', sep_"|")

______ psycopg2.DatabaseError __ e:

    print(f'Error {e}')
    ___.e.. 1)

______ IO.. __ e:

    print(f'Error {e}')
    ___.e.. 1)

f__

    __ con:
        con.c..

    __ fout:
        fout.c..

# $ cat cars.csv
# 2|Mercedes|57127
# 3|Skoda|9000
# 4|Volvo|29000
# 5|Bentley|350000
# 6|Citroen|21000
# 7|Hummer|41400
# 8|Volkswagen|21600
# 1|Audi|62300

