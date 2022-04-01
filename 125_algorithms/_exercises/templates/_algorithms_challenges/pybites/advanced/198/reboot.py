_______ d__ __ td
____ dateutil.parser _______ p..
MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


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


    lines = reboots.splitlines()

    
    previous_date = N..
    max_date = N..
    max_diff = f__("-inf")
    ___ line __ lines:
        __ line:
            _,date = line.s..('~')
            date = p..(date)
            __ previous_date:
                days = (previous_date - date).days
                __ days > max_diff:
                    max_diff = days
                    max_date = previous_date 

            previous_date = date

    

    r.. max_diff,max_date.s..("%Y-%m-%d")




calc_max_uptime(MAC1)


