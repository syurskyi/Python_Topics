____ c.. _______ n..

MIN_SCORE = 4
DICE_VALUES = r..(1, 7)

Player = n..('Player', 'name scores')


___ calculate_score(scores
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).
    """
    __ any(s n.. __ DICE_VALUES ___ s __ scores
        r.. V...()
    r.. s..(s ___ s __ scores __ s >_ MIN_SCORE)


___ get_winner(players
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.
    """
    __ any(l..(players[0].scores) != l..(s.scores) ___ s __ players[1:]
        r.. V...()
    r.. s..(players, key=l.... x: calculate_score(x.scores[-1]
