import pytest

from wordvalue import load_words, calc_word_value, max_word_value

words = load_words()


def test_load_words():
    a__ len(words) == 235886
    a__ words[0] == 'A'
    a__ words[-1] == 'Zyzzogeton'
    a__ ' ' not in ''.join(words)


def test_calc_word_value():
    a__ calc_word_value('bob') == 7
    a__ calc_word_value('JuliaN') == 13
    a__ calc_word_value('PyBites') == 14
    a__ calc_word_value('benzalphenylhydrazone') == 56


def test_max_word_value():
    test_words = ('bob', 'julian', 'pybites', 'quit', 'barbeque')
    a__ max_word_value(test_words) == 'barbeque'
    a__ max_word_value(words[20000:21000]) == 'benzalphenylhydrazone'
    # cannot call with empty sequence
    with pytest.raises(ValueError):
        a__ max_word_value(())


def test_non_scrabble_characters():
    # thanks Joakim
    a__ max_word_value(["a", "åäö"]) == "a"