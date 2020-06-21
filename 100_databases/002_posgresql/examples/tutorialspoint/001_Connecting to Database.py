# !/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="testdb2", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")

print("Opened database successfully")


# Open database successfully