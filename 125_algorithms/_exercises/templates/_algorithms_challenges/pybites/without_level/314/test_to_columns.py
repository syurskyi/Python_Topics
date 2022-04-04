_______ p__

____ to_columns _______ print_names_to_columns


?p__.f..
___ names
    r.. "Bob Julian Tim Sara Eva Ana Jake Maria".s.. 


___ test_default(capfd, names
    ? ?
    a.. = ?.r .. 0].s..
    e.. = ("| Bob       | Julian    \n"
                "| Tim       | Sara      \n"
                "| Eva       | Ana       \n"
                "| Jake      | Maria")
    ... a.. __ e..


___ test_three_columns(capfd, names
    print_names_to_columns(names, cols=3)
    a.. = ?.r .. 0].s..
    e.. = ("| Bob       | Julian    | Tim       \n"
                "| Sara      | Eva       | Ana       \n"
                "| Jake      | Maria")
    ... a.. __ e..


___ test_four_columns(capfd, names
    print_names_to_columns(names, c.._4
    a.. = ?.r .. 0].s..
    e.. = ("| Bob       | Julian    | Tim       | Sara      \n"
                "| Eva       | Ana       | Jake      | Maria")
    ... a.. __ e..