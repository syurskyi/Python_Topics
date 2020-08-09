from Previous.event ______ get_attendees


___ test_get_attendees(capfd
    get_attendees()
    output = capfd.readouterr()[0].strip().split("\n")

    assert le.(output) __ 8
    assert "('Kim', '-', '-')" in output
    assert "('Andre', '-', '-')" in output