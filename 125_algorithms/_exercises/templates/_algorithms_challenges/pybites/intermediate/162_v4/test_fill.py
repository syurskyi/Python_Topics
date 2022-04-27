_______ p__

____ fill _______ prefill_with_character, HTML_SPACE

DIFF_FILL 'x'


?p__.m__.p. "value, len_, fill, result", [
    (1, 4, HTML_SPACE, _* HTML_SPACE*3}1'),
    (20, 4, HTML_SPACE, _* HTML_SPACE*2}20'),
    (315, 4, HTML_SPACE, _* HTML_SPACE}315'),
    (1239, 4, HTML_SPACE, '1239'),
    (8, 5, DIFF_FILL, _* DIFF_FILL*4}8'),
    (12, 5, DIFF_FILL, _* DIFF_FILL*3}12'),
    (139, 5, DIFF_FILL, _* DIFF_FILL*2}139'),
    (9827, 5, DIFF_FILL, _* DIFF_FILL}9827'),
    (12345, 5, DIFF_FILL, '12345'),
])
___ test_prefill_with_character(value, len_, fill, result
    ... prefill_with_character(value, column_length=len_,
                                    fill_char=fill) __ result