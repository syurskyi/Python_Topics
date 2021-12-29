from datetime import *
from dateutil.relativedelta import *
from dateutil.rrule import *

NOW = datetime.now()
TODAY = date.today()

print(NOW, TODAY)

print(list(rrule(DAILY, 
                count=6, 
                byweekday=(MO, TU, WE, TH, FR),
                dtstart=NOW)))