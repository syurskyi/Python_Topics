import string
import itertools
___ sequence_generator():
    

    numbers = list(range(1,27))
    sequence  = [numbers[i//2] __ i % 2 == 0 else string.ascii_uppercase[i//2] for i in range(52)]

    yield from itertools.cycle(sequence)




__ __name__ == "__main__":

    sequence_generator()
