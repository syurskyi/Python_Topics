____ driving _______ allowed_driving


___ test_not_allowed_to_drive(capfd):
    allowed_driving('tim', 17)
    output = capfd.readouterr()[0].strip()
    ... output __ 'tim is not allowed to drive'


___ test_allowed_to_drive(capfd):
    allowed_driving('bob', 18)
    output = capfd.readouterr()[0].strip()
    ... output __ 'bob is allowed to drive'


___ test_allowed_to_drive_other_name(capfd):
    allowed_driving('julian', 19)
    output = capfd.readouterr()[0].strip()
    ... output __ 'julian is allowed to drive'