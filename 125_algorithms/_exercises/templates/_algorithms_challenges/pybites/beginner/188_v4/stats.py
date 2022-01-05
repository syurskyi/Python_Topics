_______ __
____ os _______ path
_______ statistics __ st
____ urllib.request _______ urlretrieve

STATS = path.j..('/tmp', 'testfiles_number_loc.txt')
__ n.. path.isfile(STATS):
    urlretrieve('https://bit.ly/2Jp5CUt', STATS)

STATS_OUTPUT = """
Basic statistics:
- count     : {count:7d}
- min       : {min_:7d}
- max       : {max_:7d}
- mean      : {mean:7.2f}

Population variance:
- pstdev    : {pstdev:7.2f}
- pvariance : {pvariance:7.2f}

Estimated variance for sample:
- count     : {sample_count:7.2f}
- stdev     : {sample_stdev:7.2f}
- variance  : {sample_variance:7.2f}
"""


___ get_all_line_counts(data: s.. = STATS) __ l..:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    # TODO 1: get the 186 ints from downloaded STATS file
    w__ open(data) __ f:
        content = f.read()
    r.. l..(map(i.., __.f..(r'\s+(\d+)\s+.*?\n', content)))


___ create_stats_report(data_ N..
    __ data __ N..
        # converting to a list in case a generator was returned
        data = l..(get_all_line_counts())

    # taking a sample for the last section
    sample = l..(data)[::2]

    # TODO 2: complete this dict, use data list and
    # for the last 3 sample_ variables, use sample list
    stats = d..(count=l..(data),
                 min_=m..(data),
                 max_=m..(data),
                 mean=st.mean(data),
                 pstdev=st.pstdev(data),
                 pvariance=st.pvariance(data),
                 sample_count=l..(sample),
                 sample_stdev=st.stdev(sample),
                 sample_variance=st.variance(sample),
                 )

    r.. STATS_OUTPUT.f..(**stats)
