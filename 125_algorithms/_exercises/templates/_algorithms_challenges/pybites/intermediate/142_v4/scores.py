____ c.. _______ n..


MIN_SCORE 4
DICE_VALUES r..(1, 7)

Player n..('Player', 'name scores')


___ calculate_score(scores
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    __ n.. a..(s __ r..(1, 7) ___ s __ scores
        r.. V...

    r.. s..(s ___ s __ scores __ s >_ MIN_SCORE)


___ get_winner(players
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.

       If the length of the scores lists of the players passed in
       don't match up raise a ValueError.

       Returns a Player namedtuple of the winner.
       You can assume there is only one winner.

       For example - input:
         Player(name='player 1', scores=[1, 3, 2, 5])
         Player(name='player 2', scores=[1, 1, 1, 1])
         Player(name='player 3', scores=[4, 5, 1, 2])

       output:
         Player(name='player 3', scores=[4, 5, 1, 2])
    """
    __ n.. a..(l..(x.scores) __ l..(players[0].scores) ___ x __ players[1:]
        r.. V...

    r.. m..(players, key=l.... x: calculate_score(x.scores
