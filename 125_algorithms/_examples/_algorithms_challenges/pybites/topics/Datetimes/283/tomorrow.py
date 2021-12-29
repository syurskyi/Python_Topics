from datetime import date, timedelta

def tomorrow(input_dt=None):
    if not input_dt:
        input_dt = date.today()
    return input_dt + timedelta(days=1)

""" fr = freeze_time('2020-07-09')
fr.start()
print(tomorrow(datetime.datetime.now()))
fr.stop()
print(tomorrow(datetime.datetime.now())) """

#print(type(tomorrow(datetime.date(2020, 5, 1))))