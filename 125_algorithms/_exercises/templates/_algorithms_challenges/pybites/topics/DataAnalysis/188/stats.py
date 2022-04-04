_______ __
_______ statistics
____ u__.r.. _______ u..

TMP = __.g..("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'testfiles_number_loc.txt'
STATS = __.p...j..(TMP, DATA)
__ n.. __.p...isfile(STATS
    u..(__.p...j..(S3, DATA), STATS)

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
    f = o.. STATS)
    r.. [i..(line.s...s.. [0]) ___ line __ o.. STATS).r..]


___ create_stats_report(data_ N..
    __ data __ N..
        # converting to a list in case a generator was returned
        data = l..(get_all_line_counts

    # taking a sample for the last section
    sample = l..(data)[::2]

    # TODO 2: complete this dict, use data list and
    # for the last 3 sample_ variables, use sample list
    stats = d..(count=l..(data),
                 min_=m..(data),
                 max_=m..(data),
                 mean=r..(statistics.mean(data),2),
                 pstdev=r..(statistics.pstdev(data),2),
                 pvariance=r..(statistics.pvariance(data),2),
                 sample_count=l..(sample),
                 sample_stdev=r..(statistics.stdev(sample),2),
                 sample_variance=r..(statistics.variance(sample),2),
                 )

    r.. STATS_OUTPUT.f..(**stats)

data = get_all_line_counts()
sample = l..(data)[::2]


print(l..(data
print(m..(data
print(m..(data
print(r..(statistics.mean(data),2
print(r..(statistics.pstdev(data),2
print(r..(statistics.pvariance(data),2
print(r..(l..(sample)))
print(r..(statistics.stdev(sample),2
print(r..(statistics.variance(sample),2
