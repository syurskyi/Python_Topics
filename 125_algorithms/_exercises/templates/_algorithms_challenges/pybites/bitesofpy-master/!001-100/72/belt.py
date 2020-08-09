from collections ______ OrderedDict
from itertools ______ filterfalse

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


___ get_belt(user_score
    __ user_score < MIN_SCORE:
        r_ None
    r_ HONORS[list(filterfalse(lambda x: x > user_score, HONORS.keys()))[-1]]
