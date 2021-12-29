from collections import namedtuple

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


___ calculate_score(scores):
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    for score in scores:
      __ score not in DICE_VALUES:
        raise ValueError
    
    total_score = sum([score for score in scores __ score >= MIN_SCORE])
    return total_score


___ get_winner(players):
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
    previous_player = 0
    for i, player in enumerate(players, start=1):
      __ i == 1:
        previous_player = len(player.scores)
      else:
        __ len(player.scores) != previous_player:
          raise ValueError

    max_score = 0
    max_player = Player

    for player in players:
      current_player_score = calculate_score(player.scores)
      __ current_player_score > max_score:
        max_score = current_player_score
        max_player = player

    return max_player


# if __name__ == "__main__":
#   print(calculate_score([1, 3, 2, 5]))
#   print(calculate_score([1, 1, 1, 1]))