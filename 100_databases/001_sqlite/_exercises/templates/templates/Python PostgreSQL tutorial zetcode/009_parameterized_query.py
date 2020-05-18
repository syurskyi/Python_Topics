#!/usr/bin/env python
# -*- coding: utf-8 -*-

_____ ?

con _ ?.c..(d.._'testdb', u.._'syurskyi',
                    p.._'1234')

uId _ 1
uPrice _ 62300

con _ ?.c..(d.._'testdb', u.._'syurskyi',
                    p.._'1234')

w__ con:

    cur _ con.c..
    ?.e..("U.. cars SET price=%s W.. id=%s", (uPrice, uId))

    print _*Number of rows updated: {?.r..}")


#$ parameterized_query.py
# Number of rows updated: 1
#
# testdb=> S.. * F.. cars W.. id=1;
#  id | name | price
# ----+------+-------
#   1 | Audi | 62300
# (1 row)