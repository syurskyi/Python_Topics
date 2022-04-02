____ c.. _______ OrderedDict

scores  [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts  'white yellow orange green blue brown black paneled red'.s..


___ get_belt(user_score, scoresscores, beltsbelts
    ninja_belts  OrderedDict()

    ___ i __ r..(l..(scores)):
        ninja_belts[scores[i]]  belts[i]

    __ user_score < 10:
        r.. N..
    ____ user_score > 1000:
        r.. ninja_belts[1000]
    ____ user_score > 10 a.. user_score < 50:
        r.. ninja_belts[10]
    ____ user_score > 50 a.. user_score < 100:
        r.. ninja_belts[50]
    ____ user_score > 100 a.. user_score < 175:
        r.. ninja_belts[100]
    ____ user_score > 175 a.. user_score < 250:
        r.. ninja_belts[175]
    ____ user_score > 250 a.. user_score < 400:
        r.. ninja_belts[250]
    ____ user_score > 400 a.. user_score < 600:
        r.. ninja_belts[400]
    ____ user_score > 600 a.. user_score < 800:
        r.. ninja_belts[600]
    ____ user_score > 800 a.. user_score < 1000:
        r.. ninja_belts[800]

# if __name__ == "__main__":
#     print(get_belt(10002))