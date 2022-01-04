_______ p__

_______ pto
____ pto _______ four_day_weekends


___ test_four_day_weekends_default(capfd):
    four_day_weekends()
    output = capfd.readouterr()[0].splitlines()
    ... l..(output) __ 23
    ... "18 Four-Day Weekends" __ output[0]
    ... "(25 days)" __ output[2]
    ... "(11 days)" __ output[3]
    ... "*" __ output[10]
    ... output[-2] __ "2020-12-11 - 2020-12-14"


___ test_four_day_weekends_workdays(capfd):
    four_day_weekends(show_workdays=T..)
    output = capfd.readouterr()[0].splitlines()
    ... l..(output) __ 26
    ... "Remaining Work Days: 200 (25 days)" __ output[0]
    ... output[-1] __ "2020-12-31"


___ test_four_day_weekends_invalid_call
    w__ p__.r..(ValueError) __ e:
        four_day_weekends(T..)
    ... s..(e.value) __ pto.ERROR_MSG


___ test_four_day_weekends_invalid_call_custom_error_message
    new_msg = "You're calling it wrong dude!"
    pto.ERROR_MSG = new_msg
    w__ p__.r..(ValueError) __ e:
        four_day_weekends(T..)
    ... s..(e.value) __ new_msg


___ test_four_day_weekends_october(capfd):
    four_day_weekends(start_month=10)
    output = capfd.readouterr()[0].splitlines()
    ... l..(output) __ 16
    ... "(3 days)" __ output[3]
    ... output[10] __ "2020-11-13 - 2020-11-16"


___ test_four_day_weekends_october_work_days(capfd):
    four_day_weekends(start_month=10, show_workdays=T..)
    output = capfd.readouterr()[0].splitlines()
    ... l..(output) __ 16
    ... "(15 days)" __ output[0]
    ... output[3] __ "2020-10-09"


___ test_four_day_weekends_less_pto(capfd):
    four_day_weekends(start_month=10, paid_time_off=120)
    output = capfd.readouterr()[0].splitlines()
    ... l..(output) __ 16
    ... "11" __ output[0]
    ... "120" __ output[2]
    ... "-56" __ output[3]
    ... "*" __ output[8]


___ test_four_day_weekends_no_event_horizon(capfd):
    four_day_weekends(start_month=10, paid_time_off=284)
    output = capfd.readouterr()[0].splitlines()
    ___ line __ output:
        ... "*" n.. __ line


___ test_four_day_weekends_pto_160(capfd):
    four_day_weekends(paid_time_off=160)
    output = capfd.readouterr()[0].splitlines()
    ... "*" __ output[13]
