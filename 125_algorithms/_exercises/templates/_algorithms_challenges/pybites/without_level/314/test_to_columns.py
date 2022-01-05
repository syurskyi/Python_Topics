_______ p__

____ to_columns _______ print_names_to_columns


@p__.f..
___ names
    r.. "Bob Julian Tim Sara Eva Ana Jake Maria".s.. 


___ test_default(capfd, names):
    print_names_to_columns(names)
    actual = ?.r .. 0].s..
    expected = ("| Bob       | Julian    \n"
                "| Tim       | Sara      \n"
                "| Eva       | Ana       \n"
                "| Jake      | Maria")
    ... actual __ expected


___ test_three_columns(capfd, names):
    print_names_to_columns(names, cols=3)
    actual = ?.r .. 0].s..
    expected = ("| Bob       | Julian    | Tim       \n"
                "| Sara      | Eva       | Ana       \n"
                "| Jake      | Maria")
    ... actual __ expected


___ test_four_columns(capfd, names):
    print_names_to_columns(names, cols=4)
    actual = ?.r .. 0].s..
    expected = ("| Bob       | Julian    | Tim       | Sara      \n"
                "| Eva       | Ana       | Jake      | Maria")
    ... actual __ expected