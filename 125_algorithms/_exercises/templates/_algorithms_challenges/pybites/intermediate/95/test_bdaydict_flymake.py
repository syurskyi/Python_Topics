____ d__ _______ date

_______ p__

____ bdaydict _______ BirthdayDict, MSG


?p__.f..(scope='module')
___ bd
    """This creates a bday dict that can be shared among the tests
       (scope = module)"""
    r.. BirthdayDict()


___ test_2_bdays_different_dates_not_print_msg(bd, capfd
    bd 'bob'  = date(1987, 6, 15)
    bd 'tim'  = date(1984, 7, 15)
    output = ?.r .. 0].s..
    ... n.. output.s..


___ test_another_bday_same_yymmdd_print_msg(bd, capfd
    bd 'mary'  = date(1987, 6, 15)
    output = ?.r .. 0].s..
    ... output __ MSG.f..('mary')  # exactly the same as bob


___ test_another_bday_same_yymm_diff_day_not_print_msg(bd, capfd
    # not a bday match
    bd 'sara'  = date(1987, 6, 14)
    output = ?.r .. 0].s..
    ... n.. output.s..


___ test_another_bday_same_mmdd_diff_year_print_msg(bd, capfd
    # if same day and month, but different year = match
    bd 'mike'  = date(1981, 7, 15)  # same as tim, except year
    output = ?.r .. 0].s..
    ... output __ MSG.f..('mike')