from string import ascii_uppercase
from itertools import cycle


def sequence_generator():
    alphabet_list = cycle(ascii_uppercase)
    number_list = cycle(range(1,27))
    for i in range(100):
        yield next(number_list)
        yield next(alphabet_list)



print(list(sequence_generator()))