_______ os
_______ statistics
____ urllib.request _______ urlretrieve

TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'testfiles_number_loc.txt'
STATS = os.path.join(TMP, DATA)
__ n.. os.path.isfile(STATS):
    urlretrieve(os.path.join(S3, DATA), STATS)

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


___ get_all_line_counts(data: s.. = STATS) -> l..:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    # TODO 1: get the 186 ints from downloaded STATS file
    counter = 0
    ___ i __ STATS.s..("\n"):
        __ i:
            counter += 1
    r.. counter


___ create_stats_report(data_ N..
    __ data __ N..
        # converting to a list in case a generator was returned
        data = l..(get_all_line_counts())

    # taking a sample for the last section
    sample = l..(data)[::2]

    # TODO 2: complete this dict, use data list and
    # for the last 3 sample_ variables, use sample list
    stats = d..(count=N..,
                 min_=N..,
                 max_=N..,
                 mean=N..,
                 pstdev=N..,
                 pvariance=N..,
                 sample_count=N..,
                 sample_stdev=N..,
                 sample_variance=N..,
                 )

    r.. STATS_OUTPUT.f..(**stats)