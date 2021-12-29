____ string _______ ascii_uppercase
____ itertools _______ cycle


___ sequence_generator():
    alphabet_list = cycle(ascii_uppercase)
    number_list = cycle(r..(1,27))
    ___ i __ r..(100):
        yield next(number_list)
        yield next(alphabet_list)



print(l..(sequence_generator()))