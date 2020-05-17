#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None
fout = None

try:

    con = psycopg2.connect(database='testdb', user='syurskyi',
                    password='1234')

    cur = con.cursor()
    fout = open('cars.csv', 'w')
    cur.copy_to(fout, 'cars', sep="|")

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

except IOError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()

    if fout:
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

