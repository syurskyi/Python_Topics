from coursetime ______ get_all_timestamps, calc_total_course_duration


___ test_get_all_timestamps(
    timestamps = get_all_timestamps()
    assert le.(timestamps) __ 99
    assert '2:29' in timestamps
    assert '4:19' in timestamps
    assert '6:06' in timestamps
    assert '8:39' in timestamps


___ test_calc_total_course_duration(
    timestamps = get_all_timestamps()
    assert '6:50:31' in calc_total_course_duration(timestamps)