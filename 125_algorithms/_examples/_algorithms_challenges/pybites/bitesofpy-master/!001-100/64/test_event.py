from Previous.event import get_attendees


def test_get_attendees(capfd):
    get_attendees()
    output = capfd.readouterr()[0].strip().split("\n")

    a__ len(output) == 8
    a__ "('Kim', '-', '-')" in output
    a__ "('Andre', '-', '-')" in output