____ d__ _______ date, d__

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


___ extract_date(reboots):
    months = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
    }
    lines = reboots.splitlines(keepends=F..)
    ___ line __ lines:
        __ l..(line.strip()) __ 0:
            continue
        line_parts = line.s...s..
        time_part = line_parts[-1].s..(':')
        y.. d__ y.._2019,
                        m.._months[line_parts[-3]],
                        d.._int(line_parts[-2]),
                       hour=int(time_part[0]),
                       minute=int(time_part[1]))


___ calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    previous = N..
    records    # list
    ___ this_date __ extract_date(reboots):
        __ previous __ N..
            previous = this_date
            continue
        records.a..(((previous - this_date).days, s..(previous.date())))
        previous = this_date
    r.. s..(records)[-1]
