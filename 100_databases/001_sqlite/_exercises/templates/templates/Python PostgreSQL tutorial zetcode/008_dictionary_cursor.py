#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ ?
_____ ?.extras

con _ ?.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

w__ con:

    cursor _ con.cursor(cursor_factory_?.extras.DictCursor)
    cursor.e..("S.. * F.. cars")

    rows _ cursor.f_a..

    ___ row __ rows:
        print _*{row['id']} {row['name']} {row['price']}")