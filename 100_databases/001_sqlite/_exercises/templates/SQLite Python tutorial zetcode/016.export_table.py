#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? as sqlite

cars _ (
    (1, 'Audi', 52643),
    (2, 'Mercedes', 57642),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)


def writeData(data):

    f _ open('cars.sql', 'w')

    with f:
        f.write(data)


con _ sqlite.c..(':memory:')

with con:

    cur _ con.cursor()

    cur.e..("DROP TABLE IF EXISTS cars")
    cur.e..("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)
    cur.e..("DELETE FROM cars WHERE price < 30000")

    data _ '\n'.join(con.iterdump())

    writeData(data)