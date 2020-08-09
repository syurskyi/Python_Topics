"""
String Shortener (shrink)
http://www.codewars.com/kata/557d18803802e873170000a0/train/python
"""


___ shorten(string, length, glue="..."
    __ length >= le.(string
        r_ string
    __ length __ le.(glue) + 1 or le.(glue) > length:
        r_ string[:length]
    shortened = length - le.(glue)
    r_ string[:int(shortened / 2)] + glue + string[-(int(shortened / 2) + (shortened % 2)):]