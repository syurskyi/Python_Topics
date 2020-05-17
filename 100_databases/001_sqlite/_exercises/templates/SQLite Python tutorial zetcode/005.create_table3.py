#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ sqlite
_____ ___

con _ None

___
    con _ sqlite.c..('ydb.db')

    cur _ con.c..

    cur.executescript("""
        DROP T.. IF EXISTS cars;
        C.. T.. cars(id INT, name T..., price INT);
        I.. I.. cars V..(1,'Audi',52642);
        I.. I.. cars V..(2,'Mercedes',57127);
        I.. I.. cars V..(3,'Skoda',9000);
        I.. I.. cars V..(4,'Volvo',29000);
        I.. I.. cars V..(5,'Bentley',350000);
        I.. I.. cars V..(6,'Citroen',21000);
        I.. I.. cars V..(7,'Hummer',41400);
        I.. I.. cars V..(8,'Volkswagen',21600);
        """)

    con.c..

______ sqlite.Error __ e:

    __ con:
        con.rollback()

    print(f"Error {e.args[0]}")
    ___.exit(1)

f__

    __ con:
        con.c..
