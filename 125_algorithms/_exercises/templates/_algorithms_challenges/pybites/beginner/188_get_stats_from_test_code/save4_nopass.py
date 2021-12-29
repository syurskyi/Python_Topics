_______ pandas as pd
_______ statistics as st

url = 'https://bites-data.s3.us-east-2.amazonaws.com/testfiles_number_loc.txt'
DATA = pd.read_csv(url, header=N..)


___ get_all_line_counts(data: str = DATA) -> l..:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    values    # list
    ___ value __ DATA[DATA.columns[0]]:
        values.a..(int(value.s.. [0]))
    r.. values


___ create_stats_report(data_ N..
    __ data __ N..
        # converting to a list in case a generator was returned
        data = l..(get_all_line_counts())

    # taking a sample for the last section
    sample = l..(data)[::2]

    stats = d..(count=l..(data),
                 min_=m..(data),
                 max_=max(data),
                 mean=round(st.mean(data), 2),
                 pstdev=round(st.pstdev(data), 2),
                 pvariance=round(st.pvariance(data), 2),
                 sample_count=l..(sample),
                 sample_stdev=round(st.stdev(sample), 2),
                 sample_variance=round(st.variance(sample), 2),
                 )
    r.. stats