"""
In this exercise you will analyze some basic car data. Here is the (fake) JSON data we created with Mockeroo - snippet below / full output here:

  [{"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":1999},
   {"id":2,"automaker":"Chrysler","model":"Town & Country","year":2002},
   {"id":3,"automaker":"Porsche","model":"Cayenne","year":2008},
   ... 997 car entries more ...
  ]
First you will write most_prolific_automaker to find out which automaker produces the most new models for a particular year.

Secondly you will write get_models which filters the data set down to car models produced by a particular automaker and year (as passed into the function).

To keep it a Beginner Bite we'll pause here, but if you like this data set, let us know and we make a sequel Bite, maybe we can add some financial data :)

Check out the docstrings and pytests and give it a shot. Good luck and keep calm keep and code in Python.
"""

"""
what I'm building:
{
    "Dodge": 5,
    "Chrysler", 6
}

"""

from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    result = {}
    for d in data:
        if d['year'] == year:
            try:
                result[d['automaker']] += 1
            except:
                result[d['automaker']] = 0
    t = ""
    cur = 0
    for k,v in result.items():
        if v > cur:
            t = k
            cur = v
    return t


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    s = set()
    for d in data:
        if d['automaker'] == automaker and d['year'] == year:
            s.add(d['model'])
    return s

most_prolific_automaker(1995)
get_models("Chrysler", 1999)