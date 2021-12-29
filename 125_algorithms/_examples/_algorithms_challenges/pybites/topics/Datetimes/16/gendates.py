from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    newdate = PYBITES_BORN
    datelist = []
    for i in range(10):
        newdate += timedelta(days=100)
        datelist.append(newdate)
    return(datelist)