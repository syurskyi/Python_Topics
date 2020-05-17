#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

con _ sqlite.c..('ydb.db')

with con:

    cur _ con.cursor()

    cur.e..("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cur.e..("INSERT INTO cars VALUES(1,'Audi',52642)")
    cur.e..("INSERT INTO cars VALUES(2,'Mercedes',57127)")
    cur.e..("INSERT INTO cars VALUES(3,'Skoda',9000)")
    cur.e..("INSERT INTO cars VALUES(4,'Volvo',29000)")
    cur.e..("INSERT INTO cars VALUES(5,'Bentley',350000)")
    cur.e..("INSERT INTO cars VALUES(6,'Citroen',21000)")
    cur.e..("INSERT INTO cars VALUES(7,'Hummer',41400)")
    cur.e..("INSERT INTO cars VALUES(8,'Volkswagen',21600)")
