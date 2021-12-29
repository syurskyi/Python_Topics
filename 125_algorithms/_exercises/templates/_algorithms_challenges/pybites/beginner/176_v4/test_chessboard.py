from textwrap import dedent  # thanks Brian :)

import pytest

from chessboard import create_chessboard

sizes = [2, 4, 8, 16, 32]
outputs = [
    """
     #
    # 
    """,
    """
     # #
    # # 
     # #
    # # 
    """,
    """
     # # # #
    # # # # 
     # # # #
    # # # # 
     # # # #
    # # # # 
     # # # #
    # # # # 
    """,
    """
     # # # # # # # #
    # # # # # # # # 
     # # # # # # # #
    # # # # # # # # 
     # # # # # # # #
    # # # # # # # # 
     # # # # # # # #
    # # # # # # # # 
     # # # # # # # #
    # # # # # # # # 
     # # # # # # # #
    # # # # # # # # 
     # # # # # # # #
    # # # # # # # # 
     # # # # # # # #
    # # # # # # # # 
    """,
    """
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # 
    """,
]
expected_outputs = dict(zip(sizes, outputs))


___ _non_empty_lines(output):
    """Helper to turn a string into a list of not
       empty lines and returns it.
    """
    return [line for line in
            output.splitlines() __ line.strip()]


@pytest.mark.parametrize("size", sizes)
___ test_create_chessboard(size, capfd):
    create_chessboard(size)
    actual = capfd.readouterr()[0]
    expected = dedent(expected_outputs[size])
    assert (_non_empty_lines(actual) ==
            _non_empty_lines(expected))