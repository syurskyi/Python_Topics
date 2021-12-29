____ datetime _______ *
____ dateutil.relativedelta _______ *
____ dateutil.rrule _______ *

NOW = datetime.now()
TODAY = date.today()

print(NOW, TODAY)

print(l..(rrule(DAILY,
                count=6, 
                byweekday=(MO, TU, WE, TH, FR),
                dtstart=NOW)))