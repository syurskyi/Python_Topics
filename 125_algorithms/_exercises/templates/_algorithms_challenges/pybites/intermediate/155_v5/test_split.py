_______ p__

____ s.. _______ split_words_and_quoted_text

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


@p__.mark.parametrize("arg, ret",
                         z..(some_strings, expected_returns))

___ test_split_words_and_quoted_text(arg, ret):
    ... split_words_and_quoted_text(arg) __ ret