#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ ?

con _ ?.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

uId _ 1
uPrice _ 62300

con _ ?.c..(database_'testdb', user_'syurskyi',
                    password_'1234')

w__ con:

    cur _ con.c..
    cur.e..("U.. cars SET price=%s W.. id=%s", (uPrice, uId))

    print _*Number of rows updated: {cur.rowcount}")


#$ parameterized_query.py
# Number of rows updated: 1
#
# testdb=> S.. * F.. cars W.. id=1;
#  id | name | price
# ----+------+-------
#   1 | Audi | 62300
# (1 row)