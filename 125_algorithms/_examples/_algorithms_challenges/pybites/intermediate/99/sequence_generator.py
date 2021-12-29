import string
import itertools

def sequence_generator():
    letters = [letter for letter in string.ascii_uppercase]
    numbers = [num for num in range(1, len(letters) +1, 1)]
    
    sequence = []
    for pair in zip(numbers, letters):
        sequence.append(pair[0])
        sequence.append(pair[1])

    repeating_sequence = itertools.cycle(sequence)
    for character in repeating_sequence:
        yield character


# if __name__ == "__main__":
#     test = sequence_generator()
#     print(next(test))
    #print(sequence_generator())