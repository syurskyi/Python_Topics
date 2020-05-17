import psycopg2

def connect():
    psycopg2.connect(user='syurskyi', password='1234', database='learning', host='localhost')