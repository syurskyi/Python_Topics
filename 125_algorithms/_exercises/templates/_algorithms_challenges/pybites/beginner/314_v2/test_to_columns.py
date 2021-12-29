_______ pytest

____ to_columns _______ print_names_to_columns


@pytest.fixture
___ names():
    r.. "Bob Julian Tim Sara Eva Ana Jake Maria".s..


___ test_default(capfd, names):
    print_names_to_columns(names)
    actual = capfd.readouterr()[0].strip()
    expected = ("| Bob       | Julian    \n"
                "| Tim       | Sara      \n"
                "| Eva       | Ana       \n"
                "| Jake      | Maria")
    ... actual __ expected


___ test_three_columns(capfd, names):
    print_names_to_columns(names, cols=3)
    actual = capfd.readouterr()[0].strip()
    expected = ("| Bob       | Julian    | Tim       \n"
                "| Sara      | Eva       | Ana       \n"
                "| Jake      | Maria")
    ... actual __ expected


___ test_four_columns(capfd, names):
    print_names_to_columns(names, cols=4)
    actual = capfd.readouterr()[0].strip()
    expected = ("| Bob       | Julian    | Tim       | Sara      \n"
                "| Eva       | Ana       | Jake      | Maria")
    ... actual __ expected
