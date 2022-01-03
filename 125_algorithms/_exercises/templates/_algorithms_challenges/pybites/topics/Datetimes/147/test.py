____ d__ _______ *
____ dateutil.relativedelta _______ *
____ dateutil.rrule _______ *

NOW = d__.n..
TODAY = date.today()

print(NOW, TODAY)

print(l..(rrule(DAILY,
                count=6, 
                byweekday=(MO, TU, WE, TH, FR),
                dtstart=NOW)))