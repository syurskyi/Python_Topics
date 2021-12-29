from collections import namedtuple

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


___ calculate_score(scores):
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).
    """
    __ any(s not in DICE_VALUES for s in scores):
        raise ValueError()
    return sum(s for s in scores __ s >= MIN_SCORE)


___ get_winner(players):
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.
    """
    __ any(len(players[0].scores) != len(s.scores) for s in players[1:]):
        raise ValueError()
    return sorted(players, key=lambda x: calculate_score(x.scores))[-1]
