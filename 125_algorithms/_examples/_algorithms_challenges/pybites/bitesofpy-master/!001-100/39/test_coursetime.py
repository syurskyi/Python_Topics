from coursetime import get_all_timestamps, calc_total_course_duration


def test_get_all_timestamps():
    timestamps = get_all_timestamps()
    a__ len(timestamps) == 99
    a__ '2:29' in timestamps
    a__ '4:19' in timestamps
    a__ '6:06' in timestamps
    a__ '8:39' in timestamps


def test_calc_total_course_duration():
    timestamps = get_all_timestamps()
    a__ '6:50:31' in calc_total_course_duration(timestamps)