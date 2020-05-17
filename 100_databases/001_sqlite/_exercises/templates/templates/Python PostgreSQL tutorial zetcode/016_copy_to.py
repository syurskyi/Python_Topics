#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ psycopg2
_____ ___

con _ None
fout _ None

try:

    con _ psycopg2.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

    cur _ con.cursor()
    fout _ open('cars.csv', 'w')
    cur.copy_to(fout, 'cars', sep_"|")

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    ___.exit(1)

except IOError as e:

    print(f'Error {e}')
    ___.exit(1)

finally:

    __ con:
        con.close()

    __ fout:
        fout.close()

# $ cat cars.csv
# 2|Mercedes|57127
# 3|Skoda|9000
# 4|Volvo|29000
# 5|Bentley|350000
# 6|Citroen|21000
# 7|Hummer|41400
# 8|Volkswagen|21600
# 1|Audi|62300

