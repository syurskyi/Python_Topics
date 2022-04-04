"""
Bowling score calculator
http://www.codewars.com/kata/5427db696f30afd74b0006a3/train/python
"""


___ bowling_score(rolls
    """Compute the total score for a player's game of bowling."""

    total = 0
    frame = 0
    newframe = T..
    ___ index, roll __ e..(rolls
        __ frame __ 10:
            _____
        __ roll __ 10:
            total += rolls[index + 1]
            total += rolls[index + 2]
            frame += 1
        ____ n.. newframe:
            __ rolls[index - 1] + roll __ 10:
                total += rolls[index + 1]
            frame += 1
            newframe = T..
        ____
            newframe = F..
        total += roll

    r.. total