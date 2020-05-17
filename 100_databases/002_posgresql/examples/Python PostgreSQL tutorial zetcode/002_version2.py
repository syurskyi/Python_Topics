#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2


con = psycopg2.connect(database='testdb', user='syurskyi',
    password='1234')

with con:

    cur = con.cursor()
    cur.execute('SELECT version()')

    version = cur.fetchone()[0]
    print(version)