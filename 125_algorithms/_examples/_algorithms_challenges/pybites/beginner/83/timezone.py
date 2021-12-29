from pytz import timezone, utc
from datetime import datetime

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    #print(naive_utc_dt)
    #print(utc.localize(naive_utc_dt))
    #print(utc.localize(naive_utc_dt).astimezone(SPAIN))
    #print(utc.localize(naive_utc_dt).astimezone(AUSTRALIA))
    return (utc.localize(naive_utc_dt).astimezone(AUSTRALIA), 
            utc.localize(naive_utc_dt).astimezone(SPAIN))



naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)

print(what_time_lives_pybites(naive_utc_dt))