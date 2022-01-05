_______ p__

____ scrabble _______ get_possible_dict_words

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score ___ score, letters __ scrabble_scores
                 ___ letter __ letters.s.. }


___ calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    r.. s..(LETTER_SCORES.get(char.u.., 0) ___ char __ word)


___ max_word_value(words):
    """Calc the max value of a collection of words"""
    r.. m..(words, key=calc_word_value)


@p__.mark.parametrize("draw, expected", [
    ('T, I, I, G, T, T, L', 'gilt'),
    ('O, N, V, R, A, Z, H', 'zonar'),
    ('E, P, A, E, I, O, A', ('apio', 'peai')),
    ('B, R, C, O, O, E, O', 'boce'),
    ('G, A, R, Y, T, E, V', 'garvey'),
])
___ test_max_word(draw, expected):
    draw = draw.s..(', ')
    words = get_possible_dict_words(draw)
    __ l..(expected) > 1:
        ... max_word_value(words) __ expected
    ____:
        ... max_word_value(words) __ expected