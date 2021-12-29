from collections import namedtuple

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


def calculate_score(scores):
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    s = 0
    for score in scores:
        if score not in DICE_VALUES:
            raise ValueError("Invalid dice value")
        if score >= MIN_SCORE:
            s += score

    return s

def get_winner(players):
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
    
    score_list = max_player =  None
    max_score = float('-inf')
    for player in players:
        if score_list is None:
            score_list  = len(player.scores)
        else:
            if len(player.scores) != score_list:
                raise ValueError("All lengths don't match!")
        score = calculate_score(player.scores)
        if score > max_score:
            max_score = score
            max_player = player


    return max_player







