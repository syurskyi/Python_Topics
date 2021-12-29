scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.s.. 


___ get_belt(user_score, scores=scores, belts=belts):
    print(user_score)
    ___ index, score __ e..(scores):
        __ user_score < scores[0]:
            r.. N..
        ____ user_score < score:
            r.. belts[index-1]
    r.. belts[l..(belts)-1]




print(get_belt(10))