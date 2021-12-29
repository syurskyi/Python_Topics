from pytz import timezone, utc
from datetime import datetime

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    date = naive_utc_dt.replace(tzinfo=utc)
    return date.astimezone(AUSTRALIA), date.astimezone(SPAIN)