____ coursetime _______ get_all_timestamps, calc_total_course_duration


___ test_get_all_timestamps
    timestamps = get_all_timestamps()
    ... l..(timestamps) __ 99
    ... '2:29' __ timestamps
    ... '4:19' __ timestamps
    ... '6:06' __ timestamps
    ... '8:39' __ timestamps


___ test_calc_total_course_duration
    timestamps = get_all_timestamps()
    ... '6:50:31' __ calc_total_course_duration(timestamps)