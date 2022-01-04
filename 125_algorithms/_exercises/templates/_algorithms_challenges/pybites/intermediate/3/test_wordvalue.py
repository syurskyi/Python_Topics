____ wordvalue _______ load_words, calc_word_value, max_word_value

words = load_words()


___ test_load_words
    ... t..(words) __ l..
    ... l..(words) __ 235886
    ... words[0] __ 'A'
    ... words[-1] __ 'Zyzzogeton'
    ... ' ' n.. __ ''.j..(words)


___ test_calc_word_value
    ... calc_word_value('bob') __ 7
    ... calc_word_value('JuliaN') __ 13
    ... calc_word_value('PyBites') __ 14
    ... calc_word_value('benzalphenylhydrazone') __ 56


___ test_max_word_value
    test_words = ['bob', 'julian', 'pybites', 'quit', 'barbeque']
    ... max_word_value(test_words) __ 'barbeque'
    ... max_word_value(words[20000:21000]) __ 'benzalphenylhydrazone'


___ test_non_scrabble_characters
    # thanks Joakim
    ... max_word_value(["a", "åäö"]) __ "a"