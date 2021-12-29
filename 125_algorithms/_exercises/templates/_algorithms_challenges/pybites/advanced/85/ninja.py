scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

    ___ __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    ___ _get_belt(self, new_score):
        """Might be a useful helper"""
        pass
    


    ___ _get_score(self):
        return self._score

    ___ _set_score(self, new_score):

        __ not isinstance(new_score,int):
            raise ValueError("Score takes an int")
        __ new_score < self.score:
            raise ValueError("Cannot lower score")


        
        self._score = new_score

        for i,(score,rank) in enumerate(zip(scores,ranks)):
            __ score > self.score:
                rank = ranks[i -1]
                break


        __ rank != self._last_earned_belt:
            self._last_earned_belt = rank

            print(f"Congrats, you earned {self.score} points obtaining the PyBites Ninja {self._last_earned_belt.capitalize()} Belt")
        else:
            print(f"Set new score to {self.score}")











    score = property(_get_score, _set_score)
