____ event _______ get_attendees


___ test_get_attendees(capfd):
    get_attendees()
    output = capfd.readouterr()[0].strip().split("\n")

    ... l..(output) __ 8
    ... "('Kim', '-', '-')" __ output
    ... "('Andre', '-', '-')" __ output