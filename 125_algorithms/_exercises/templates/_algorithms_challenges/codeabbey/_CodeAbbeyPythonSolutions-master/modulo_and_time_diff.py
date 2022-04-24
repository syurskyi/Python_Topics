amount_values i..(input
results    # list

___ get_time_diff(d1, h1, m1, s1, d2, h2, m2, s2
    day_in_seconds 24*60*60
    hour_in_seconds 60*60
    minute_in_seconds 60

    time2_in_seconds (d2*day_in_seconds)+(h2*hour_in_seconds)+(m2*minute_in_seconds)+s2
    time1_in_seconds (d1*day_in_seconds)+(h1*hour_in_seconds)+(m1*minute_in_seconds)+s1

    time_diff_in_seconds time2_in_seconds - time1_in_seconds
    time_diff_day (time_diff_in_seconds)//(day_in_seconds)

    time_diff_in_seconds -_ (day_in_seconds* time_diff_day)
    time_diff_hour (time_diff_in_seconds)//(hour_in_seconds)

    time_diff_in_seconds -_ (hour_in_seconds* time_diff_hour)
    time_diff_minute (time_diff_in_seconds)//(minute_in_seconds)

    time_diff_seconds time_diff_in_seconds - (minute_in_seconds*time_diff_minute)

    r.. "("+s..(time_diff_day)+" "+s..(time_diff_hour) +" "+ s..(time_diff_minute)+" "+ s..(time_diff_seconds)+")"

___ i __ r..(amount_values
    d1,h1,m1,s1,d2,h2,m2,s2 m.. i..,i.. ).s..
    results.a..(get_time_diff(d1,h1,m1,s1, d2, h2, m2, s2

print(*results)