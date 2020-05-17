#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite
_____ ___

con _ None

try:
    con _ sqlite.c..('ydb.db')

    cur _ con.c..

    cur.executescript("""
        DROP T.. IF EXISTS cars;
        C.. T.. cars(id INT, name T..., price INT);
        INSERT INTO cars VALUES(1,'Audi',52642);
        INSERT INTO cars VALUES(2,'Mercedes',57127);
        INSERT INTO cars VALUES(3,'Skoda',9000);
        INSERT INTO cars VALUES(4,'Volvo',29000);
        INSERT INTO cars VALUES(5,'Bentley',350000);
        INSERT INTO cars VALUES(6,'Citroen',21000);
        INSERT INTO cars VALUES(7,'Hummer',41400);
        INSERT INTO cars VALUES(8,'Volkswagen',21600);
        """)

    con.c..

except sqlite.Error as e:

    __ con:
        con.rollback()

    print(f"Error {e.args[0]}")
    ___.exit(1)

finally:

    __ con:
        con.c..
