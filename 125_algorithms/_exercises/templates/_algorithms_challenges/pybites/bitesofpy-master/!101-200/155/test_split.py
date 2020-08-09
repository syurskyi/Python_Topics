______ pytest

from split ______ split_words_and_quoted_text

some_strings = (
    'Should give "3 words only"',
    'Our first program was "Hello PyBites"',
    'Because "Hello World" is really cliche',
    ('PyBites is a "A Community that Masters '
     'Python through Code Challenges"')
)
expected_returns = (
    ['Should', 'give', '3 words only'],
    ['Our', 'first', 'program', 'was', 'Hello PyBites'],
    ['Because', 'Hello World', 'is', 'really', 'cliche'],
    ['PyBites', 'is', 'a', ('A Community that Masters Python '
                            'through Code Challenges')]
)


@pytest.mark.parametrize("arg, ret",
                         zip(some_strings, expected_returns))

___ test_split_words_and_quoted_text(arg, ret
    assert split_words_and_quoted_text(arg) __ ret