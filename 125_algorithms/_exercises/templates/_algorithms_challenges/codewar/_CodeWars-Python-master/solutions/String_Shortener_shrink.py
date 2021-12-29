"""
String Shortener (shrink)
http://www.codewars.com/kata/557d18803802e873170000a0/train/python
"""


___ shorten(string, length, glue="..."):
    __ length >= l..(string):
        r.. string
    __ length __ l..(glue) + 1 o. l..(glue) > length:
        r.. string[:length]
    shortened = length - l..(glue)
    r.. string[:int(shortened / 2)] + glue + string[-(int(shortened / 2) + (shortened % 2)):]