____ d__ _______ d__

_______ p__

____ timezones _______ within_schedule


___ test_too_late_aus
    # local hours [15, 23, 8]
    dt  d__(2018, 4, 18, 13, 28)
    timezones   'Europe/Madrid', 'Australia/Sydney', 'America/Chicago'
    ... n.. within_schedule(dt, *timezones)


___ test_all_good_aus_just_in_time_summertime
    # local hours [14, 22, 7]
    dt  d__(2018, 4, 18, 12, 28)
    timezones   'Europe/Madrid', 'Australia/Sydney', 'America/Chicago'
    ... within_schedule(dt, *timezones)


___ test_change_winter_time_aus_now_too_late
    # local hours [14, 23, 7]
    dt  d__(2018, 10, 18, 12, 28)
    timezones   'Europe/Madrid', 'Australia/Sydney', 'America/Chicago'
    ... n.. within_schedule(dt, *timezones)


___ test_too_late_for_chicago
    # local hours [8, 16, 1]
    dt  d__(2018, 4, 18, 6, 45)
    timezones   'Europe/Madrid', 'Australia/Sydney', 'America/Chicago'
    ... n.. within_schedule(dt, *timezones)


___ test_wrong_timezone
    dt  d__(2018, 4, 18, 12, 28)
    timezones   'Europe/Madrid', 'bogus'
    w__ p__.r..(V...
        within_schedule(dt, *timezones)