from Previous.event import get_attendees


___ test_get_attendees(capfd):
    get_attendees()
    output = capfd.readouterr()[0].strip().split("\n")

    assert len(output) == 8
    assert "('Kim', '-', '-')" in output
    assert "('Andre', '-', '-')" in output