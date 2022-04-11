
scores [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts 'white yellow orange green blue brown black paneled red'.s..


___ get_belt(user_score, scores=scores, belts=belts
    result    # list
    ___ index, i __ e..(scores
        __ index __ 0:
            ___ j __ r..(0, i
                result.insert(j, N..)
            last i
        ____
            ___ j __ r..(last, i
                result.insert(j, belts[index - 1])
            last i
    __ user_score >_ scores[l..(scores)-1]:
        r.. belts[l..(belts)-1]
    ____
        r.. result[user_score]

print(get_belt(1000, scores, belts



