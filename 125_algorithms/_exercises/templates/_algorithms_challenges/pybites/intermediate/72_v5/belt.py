____ collections _______ OrderedDict
____ itertools _______ filterfalse

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.s.. 
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = m..(scores), max(scores)


___ get_belt(user_score):
    __ user_score < MIN_SCORE:
        r.. N..
    r.. HONORS[l..(filterfalse(l.... x: x > user_score, HONORS.keys()))[-1]]
