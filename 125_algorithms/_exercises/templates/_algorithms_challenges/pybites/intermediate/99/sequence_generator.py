_______ string
_______ itertools

___ sequence_generator():
    letters = [letter ___ letter __ string.ascii_uppercase]
    numbers = [num ___ num __ r..(1, l..(letters) +1, 1)]
    
    sequence    # list
    ___ pair __ zip(numbers, letters):
        sequence.a..(pair[0])
        sequence.a..(pair[1])

    repeating_sequence = itertools.cycle(sequence)
    ___ character __ repeating_sequence:
        yield character


# if __name__ == "__main__":
#     test = sequence_generator()
#     print(next(test))
    #print(sequence_generator())