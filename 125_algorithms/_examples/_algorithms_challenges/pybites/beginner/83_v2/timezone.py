from pytz import timezone, utc
from dateutil import tz

AUSTRALIA = tz.gettz('Australia/Sydney')
SPAIN = tz.gettz('Europe/Madrid')



def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""


    naive_utc_dt = naive_utc_dt.replace(tzinfo=tz.UTC)
    
    return naive_utc_dt.astimezone(AUSTRALIA),naive_utc_dt.astimezone(SPAIN)
