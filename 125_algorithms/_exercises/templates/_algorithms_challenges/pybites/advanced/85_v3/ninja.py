scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.s..
BELTS = d..(z..(scores, ranks))


c_ NinjaBelt:

    ___ - , score=0
        _score = score
        _last_earned_belt_number = N..

    $
    ___ _last_earned_belt
        """Return the name of the currently qualified belt, if no belt has been awarded None is returned"""
        r.. ranks[_last_earned_belt_number] __ _last_earned_belt_number __ n.. N.. ____ N..

    @staticmethod
    ___ _get_belt(new_score
        """Find the index number of the belt for the provide score"""
        r.. l..([x ___ x __ scores __ x <= new_score]) - 1

    ___ _get_score
        r.. _score

    ___ _set_score  new_score
        """
        Set the current score and update any belt qualification
        new_score must be an integer and cannot be less than the current score
        """
        __ n.. isi..(new_score, i..
            r.. V...('Score can only be an integer')
        __ _score > new_score:
            r.. V... _*New score ({new_score}) must be higher than previous score ({_score})')
        _score = new_score
        belt = _get_belt(new_score)
        __ _last_earned_belt __ N.. o. _last_earned_belt_number < belt:
            _last_earned_belt_number = belt
            print _*Congrats, you earned {new_score} points obtaining the PyBites Ninja '
                  f'{_last_earned_belt.t..} Belt')
        ____:
            print _*Set new score to {new_score}')

    score = property(_get_score, _set_score)
