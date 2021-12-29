import datetime as td
from dateutil.parser import parse
MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
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

    
    previous_date = None
    max_date = None
    max_diff = float("-inf")
    for line in lines:
        if line:
            _,date = line.split('~')
            date = parse(date)
            if previous_date:
                days = (previous_date - date).days
                if days > max_diff:
                    max_diff = days
                    max_date = previous_date 

            previous_date = date

    

    return max_diff,max_date.strftime("%Y-%m-%d")




calc_max_uptime(MAC1)


