import string
import itertools
def sequence_generator():
    

    numbers = list(range(1,27))
    sequence  = [numbers[i//2] if i % 2 == 0 else string.ascii_uppercase[i//2] for i in range(52)]

    yield from itertools.cycle(sequence)




if __name__ == "__main__":

    sequence_generator()
