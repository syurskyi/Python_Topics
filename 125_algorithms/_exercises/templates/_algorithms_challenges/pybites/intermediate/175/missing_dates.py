_______ pandas as pd
____ d__ _______ date

___ get_missing_dates(dates):
   """Receives a range of dates and returns a sequence
      of missing datetime.date objects (no worries about order).

      You can assume that the first and last date of the
      range is always present (assumption made in tests).

      See the Bite description and tests for example outputs.
   """
   dates_sorted = s..(dates)
   ds = pd.Series([i ___ i __ r..(l..(dates_sorted))], dates_sorted)
   ds = ds.asfreq("D").index.values.astype("datetime64[s]").tolist()
   all_dates = [date(d.year, d.month, d.day) ___ d __ ds]
   r.. [d ___ d __ all_dates __ d n.. __ dates_sorted]


__ __name__ __ "__main__":
   date_range = [date y.._2019,  m.._2,  d.._n) ___ n __ r..(1, 11, 2)]
   print(get_missing_dates(date_range))