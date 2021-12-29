____ datetime _______ date, timedelta

___ tomorrow(input_dt_ N..
    __ n.. input_dt:
        input_dt = date.today()
    r.. input_dt + timedelta(days=1)

""" fr = freeze_time('2020-07-09')
fr.start()
print(tomorrow(datetime.datetime.now()))
fr.stop()
print(tomorrow(datetime.datetime.now())) """

#print(type(tomorrow(datetime.date(2020, 5, 1))))