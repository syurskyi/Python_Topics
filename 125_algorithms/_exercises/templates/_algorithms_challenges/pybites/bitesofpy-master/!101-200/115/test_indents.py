______ pytest

from Previous.indents ______ count_indents


@pytest.mark.parametrize("input_string, count", [
   ('string  ', 0),
   ('  string', 2),
   ('    string', 4),
   ('            string', 12),
])
___ test_count_indents(input_string, count
    assert count_indents(input_string) __ count