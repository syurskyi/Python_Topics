scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.s.. 
BELTS = d..(z..(scores, ranks


c_ NinjaBelt:

    ___ - , score=0
        _score = score
        _last_earned_belt = N..

    ___ _get_belt  new_score
        """Might be a useful helper"""
        p..
    


    ___ _get_score
        r.. _score

    ___ _set_score  new_score

        __ n.. isi..(new_score,i..
            r.. V...("Score takes an int")
        __ new_score < score:
            r.. V...("Cannot lower score")


        
        _score = new_score

        ___ i,(score,rank) __ e..(z..(scores,ranks:
            __ score > score:
                rank = ranks[i -1]
                _____


        __ rank != _last_earned_belt:
            _last_earned_belt = rank

            print(f"Congrats, you earned {score} points obtaining the PyBites Ninja {_last_earned_belt.capitalize()} Belt")
        ____
            print(f"Set new score to {score}")











    score = property(_get_score, _set_score)
