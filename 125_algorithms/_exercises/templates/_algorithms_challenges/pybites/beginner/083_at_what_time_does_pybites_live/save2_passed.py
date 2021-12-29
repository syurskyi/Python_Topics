____ pytz _______ timezone, utc
____ datetime _______ datetime

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


___ what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    date = naive_utc_dt.replace(tzinfo=utc)
    r.. date.astimezone(AUSTRALIA), date.astimezone(SPAIN)