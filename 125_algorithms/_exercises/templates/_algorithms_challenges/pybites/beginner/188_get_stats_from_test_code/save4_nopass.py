_______ pandas __ pd
_______ statistics __ st

url = 'https://bites-data.s3.us-east-2.amazonaws.com/testfiles_number_loc.txt'
DATA = pd.read_csv(url, header=N..)


___ get_all_line_counts(data: s.. = DATA) __ l..:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    values    # list
    ___ value __ DATA[DATA.columns[0]]:
        values.a..(i..(value.s.. [0]))
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
                 mean=r..(st.mean(data), 2),
                 pstdev=r..(st.pstdev(data), 2),
                 pvariance=r..(st.pvariance(data), 2),
                 sample_count=l..(sample),
                 sample_stdev=r..(st.stdev(sample), 2),
                 sample_variance=r..(st.variance(sample), 2),
                 )
    r.. stats