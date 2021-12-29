import pandas as pd
from datetime import date

___ get_missing_dates(dates):
   """Receives a range of dates and returns a sequence
      of missing datetime.date objects (no worries about order).

      You can assume that the first and last date of the
      range is always present (assumption made in tests).

      See the Bite description and tests for example outputs.
   """
   dates_sorted = sorted(dates)
   ds = pd.Series([i for i in range(len(dates_sorted))], dates_sorted)
   ds = ds.asfreq("D").index.values.astype("datetime64[s]").tolist()
   all_dates = [date(d.year, d.month, d.day) for d in ds]
   return [d for d in all_dates __ d not in dates_sorted]


__ __name__ == "__main__":
   date_range = [date(year=2019, month=2, day=n) for n in range(1, 11, 2)]
   print(get_missing_dates(date_range))