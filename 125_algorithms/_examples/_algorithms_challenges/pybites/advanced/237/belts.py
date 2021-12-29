import json
import os
from pathlib import Path
import datetime as dt
from dateutil.parser import parse

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ('white yellow orange green blue brown black '
         'paneled red').split()
TMP = Path(os.getenv("TMP", "/tmp"))


def get_belts(data: str) -> dict:
    """Parsed the passed in json data:
       {"date":"5/1/2019","score":1},
       {"date":"9/13/2018","score":3},
       {"date":"10/25/2019","score":1},

       Loop through the scores in chronological order,
       determining when belts were achieved (use SCORES
       and BELTS).

       Return a dict with keys = belts, and values =
       readable dates, example entry:
       'yellow': 'January 25, 2018'
    """
    with open(data,'r') as f:
        dates = json.load(f)

    dates.sort(key=lambda x: parse(x['date']))
    
    
    belts = {}
    score_index = 0
    score_marker = SCORES[score_index]
    points = 0
    for date in dates:
        points += date['score']
        if points >= score_marker:

            month,day,year = map(int,date['date'].split('/'))
            date = dt.date(year,month,day)
            date_string = date.strftime('%B %d, %Y')
            belts[BELTS[score_index]] = date_string
            score_index += 1
            if score_index == len(SCORES):
                break
            score_marker = SCORES[score_index]



    return belts 


