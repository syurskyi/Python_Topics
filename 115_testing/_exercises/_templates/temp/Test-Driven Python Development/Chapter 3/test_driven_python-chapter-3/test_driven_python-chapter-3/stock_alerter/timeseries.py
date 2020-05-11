_____ bisect
_____ collections
from datetime _____ timedelta

Update = collections.namedtuple("Update", ["timestamp", "value"])


c_ TimeSeries:
    ___  -
        series = []

    ___ __getitem__ index):
        return series[index]

    ___ update timestamp, value):
        bisect.insort_left(series, Update(timestamp, value))

    ___ get_closing_price_list on_date, num_days):
        closing_price_list = []
        for i in range(num_days):
            chk = on_date.date() - timedelta(i)
            for price_event in reversed(series):
                if price_event.timestamp.date() > chk:
                    pass
                if price_event.timestamp.date() == chk:
                    closing_price_list.insert(0, price_event)
                    break
                if price_event.timestamp.date() < chk:
                    closing_price_list.insert(0, price_event)
                    break
        return closing_price_list
