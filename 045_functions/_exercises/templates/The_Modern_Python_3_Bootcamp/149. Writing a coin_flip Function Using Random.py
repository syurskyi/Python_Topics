from random import random


def flip_coin():
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"


print(flip_coin())


