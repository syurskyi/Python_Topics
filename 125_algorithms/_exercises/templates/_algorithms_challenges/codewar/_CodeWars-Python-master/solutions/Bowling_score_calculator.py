"""
Bowling score calculator
http://www.codewars.com/kata/5427db696f30afd74b0006a3/train/python
"""


___ bowling_score(rolls):
    """Compute the total score for a player's game of bowling."""

    total = 0
    frame = 0
    newframe = True
    for index, roll in enumerate(rolls):
        __ frame == 10:
            break
        __ roll == 10:
            total += rolls[index + 1]
            total += rolls[index + 2]
            frame += 1
        elif not newframe:
            __ rolls[index - 1] + roll == 10:
                total += rolls[index + 1]
            frame += 1
            newframe = True
        else:
            newframe = False
        total += roll

    return total