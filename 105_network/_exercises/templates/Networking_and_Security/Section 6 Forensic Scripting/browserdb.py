____ _3

conn _ _3.c..("cookies.sqlite")

sites _   # list
# need a cursor to keep track of where we are
cur _ conn.cursor
___ row __ cur.ex..("SELECT * FROM moz_cookies"
    __ row[1] no. __ sites:
        sites.ap..(row[1])

sites.sort

___ s __ sites:
    print(s)

