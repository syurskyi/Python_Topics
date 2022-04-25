_______ j__
_______ __
____ p.. _______ P..
_______ d__ __ dt
____ dateutil.parser _______ p..

SCORES [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS ('white yellow orange green blue brown black '
         'paneled red').s..
TMP P.. __.g.. "TMP", "/tmp"


___ get_belts(data: s..) __ d..:
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
    w__ o.. data _ __ f:
        dates j__.l.. f)

    dates.s..(k.._l.... x: p..(x 'date'
    
    
    belts    # dict
    score_index 0
    score_marker SCORES[score_index]
    points 0
    ___ date __ dates:
        points += date 'score'
        __ points >_ score_marker:

            month,day,year m.. i..,date 'date' .s..('/'
            date dt.date(year,month,day)
            date_string date.s..('%B _d, _Y')
            belts[BELTS[score_index]] date_string
            score_index += 1
            __ score_index __ l..(SCORES
                _____
            score_marker SCORES[score_index]



    r.. belts


