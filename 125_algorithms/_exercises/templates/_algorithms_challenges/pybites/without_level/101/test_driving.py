____ driving _______ allowed_driving


___ test_not_allowed_to_drive(capfd
    allowed_driving('tim', 17)
    output ?.r .. 0 .s..
    ... ? __ 'tim is not allowed to drive'


___ test_allowed_to_drive(capfd
    allowed_driving('bob', 18)
    output ?.r .. 0 .s..
    ... ? __ 'bob is allowed to drive'


___ test_allowed_to_drive_other_name(capfd
    allowed_driving('julian', 19)
    output ?.r .. 0 .s..
    ... ? __ 'julian is allowed to drive'