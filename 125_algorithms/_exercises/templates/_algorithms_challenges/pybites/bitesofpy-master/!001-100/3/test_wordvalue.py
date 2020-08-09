______ pytest

from wordvalue ______ load_words, calc_word_value, max_word_value

words = load_words()


___ test_load_words(
    assert le.(words) __ 235886
    assert words[0] __ 'A'
    assert words[-1] __ 'Zyzzogeton'
    assert ' ' not in ''.join(words)


___ test_calc_word_value(
    assert calc_word_value('bob') __ 7
    assert calc_word_value('JuliaN') __ 13
    assert calc_word_value('PyBites') __ 14
    assert calc_word_value('benzalphenylhydrazone') __ 56


___ test_max_word_value(
    test_words = ('bob', 'julian', 'pybites', 'quit', 'barbeque')
    assert max_word_value(test_words) __ 'barbeque'
    assert max_word_value(words[20000:21000]) __ 'benzalphenylhydrazone'
    # cannot call with empty sequence
    with pytest.raises(ValueError
        assert max_word_value(())


___ test_non_scrabble_characters(
    # thanks Joakim
    assert max_word_value(["a", "åäö"]) __ "a"