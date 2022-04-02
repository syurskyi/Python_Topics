_______ i..
_______ os
_______ urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.j..(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

w__ o.. DICTIONARY) __ f:
    dictionary = s..([word.s...l.. ___ word __ f.r...s.. ])

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score ___ score, letters __ scrabble_scores
                 ___ letter __ letters.s.. }


___ calc_word_value(word
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    r.. s..(LETTER_SCORES.get(char.u.., 0) ___ char __ word)

___ get_possible_dict_words(draw
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    possible_word    # dict
    in_str = ''.j..([letter ___ letter __ draw __ letter.isalpha()])
    permute_list = _get_permutations_draw(in_str)
    ___ word __ permute_list:
        temp_word = ''.j..(word)
        __ temp_word.l.. __ dictionary:
            possible_word[temp_word.l..] = calc_word_value(temp_word.l..
    listOfKeys = l..()
    max_value = m..(possible_word.values())
    ___ key, value __ possible_word.i..:
        __ value __ max_value:
            listOfKeys.a..(key)
    r.. listOfKeys

___ _get_permutations_draw(draw
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    permute_words_list    # list
    ___ i __ r..(l..(draw)):
        permute_words = l..(i...permutations(draw, i+1))
        permute_words_list += permute_words
    r.. permute_words_list

