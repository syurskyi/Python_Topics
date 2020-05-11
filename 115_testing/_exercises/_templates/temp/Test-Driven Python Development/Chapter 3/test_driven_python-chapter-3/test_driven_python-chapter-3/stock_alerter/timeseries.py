_____ bisect
_____ collections
____ d_t_ _____ timedelta

Update = collections.namedtuple("Update", ["timestamp", "value"])


c_ TimeSeries:
    ___  -
        series = []

    ___ __getitem__ index):
        r_ series[index]

    ___ u.. timestamp, value):
        bisect.insort_left(series, Update(timestamp, value))

    ___ get_closing_price_list on_date, num_days):
        closing_price_list = []
        ___ i __ range(num_days):
            chk = on_date.date() - timedelta(i)
            ___ price_event __ reversed(series):
                __ price_event.timestamp.date() > chk:
                    pass
                __ price_event.timestamp.date() == chk:
                    closing_price_list.insert(0, price_event)
                    break
                __ price_event.timestamp.date() < chk:
                    closing_price_list.insert(0, price_event)
                    break
        r_ closing_price_list
