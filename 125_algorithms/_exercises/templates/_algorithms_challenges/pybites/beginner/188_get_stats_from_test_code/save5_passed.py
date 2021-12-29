import pandas as pd
import statistics as st

url = 'https://bites-data.s3.us-east-2.amazonaws.com/testfiles_number_loc.txt'
DATA = pd.read_csv(url, header=None)

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


___ get_all_line_counts(data: str = DATA) -> list:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    values = []
    for value in DATA[DATA.columns[0]]:
        values.append(int(value.split()[0]))
    return values


___ create_stats_report(data_ N..
    __ data is None:
        # converting to a list in case a generator was returned
        data = list(get_all_line_counts())

    # taking a sample for the last section
    sample = list(data)[::2]

    stats = dict(count=len(data),
                 min_=min(data),
                 max_=max(data),
                 mean=round(st.mean(data), 2),
                 pstdev=round(st.pstdev(data), 2),
                 pvariance=round(st.pvariance(data), 2),
                 sample_count=len(sample),
                 sample_stdev=round(st.stdev(sample), 2),
                 sample_variance=round(st.variance(sample), 2),
                 )

    return STATS_OUTPUT.format(**stats)