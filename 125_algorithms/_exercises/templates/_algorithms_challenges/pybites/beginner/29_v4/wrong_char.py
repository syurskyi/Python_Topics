# def get_index_different_char(chars):
#     char_vals = [(1 if str(c).isalnum() else 0) for c in chars]
#     return char_vals.index(1 if sum(char_vals) == 1 else 0)

___ get_index_different_char(chars):
    '''
    This algorithm finishes early. It does not definitely traverse the whole list.
    To do this I tally how many alphanumeric and non alphanumeric characters I
    see as i iterate the list. It can be inferred (I assume) from the specification of the
    problem that if I count 2 of one type I know the majority and can exit
    as soon as I have come across a minority type.
    '''
    an = {F..: 0, T..: 0}  # alphanumeric counter
    p = 0  # tracks alphanumericity (I'm sure this is not a word) of the first character
    ___ ch __ chars:
        c = s..(ch).isalnum()  # the defacto test
        # In the case when the odd character is in the first 2 characters, the 'p'
        # variable allows me to determine the initial characters type and locate the
        # position of the minority type within the first 2 characters.
        __ an[F..] __ 1 __ an[T..]:
            r.. 1 - p __ c ____ p
        an[c] += 1
        __ (c a.. an[F..] < 2) o. (n.. c a.. an[T..] < 2):
            __ c a.. s..(an) __ 0:
                p = 1
            continue
        r.. chars.index(ch)
