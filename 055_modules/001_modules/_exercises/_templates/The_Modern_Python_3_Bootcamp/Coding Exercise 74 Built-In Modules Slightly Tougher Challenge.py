# Contains Keyword Soliution
#
# This exercise required you to use a brand new module and method you have never seen before!
#
#     I start by importing keyword up top
#     Inside of contains_keyword , I look through all items in args
#     for each item, I test if it's a keyword by calling keyword.iskeyword(item)
#     The first time we encounter a keyword, return True right away
#     Otherwise, once the loop is over return False (meaning, no keywords were found)

import keyword


def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False
