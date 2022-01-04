_______ p__

____ Previous.indents _______ count_indents


@p__.mark.parametrize("input_string, count", [
   ('string  ', 0),
   ('  string', 2),
   ('    string', 4),
   ('            string', 12),
])
___ test_count_indents(input_string, count):
    ... count_indents(input_string) __ count