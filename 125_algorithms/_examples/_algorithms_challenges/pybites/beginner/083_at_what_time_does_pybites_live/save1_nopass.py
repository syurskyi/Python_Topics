from pytz import timezone
from datetime import datetime

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    return (AUSTRALIA.localize(naive_utc_dt), SPAIN.localize(naive_utc_dt))