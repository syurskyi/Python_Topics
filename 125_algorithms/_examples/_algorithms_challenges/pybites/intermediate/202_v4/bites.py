import csv
import os
from pathlib import Path
from u__.r.. import u..

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

if not stats.exists():
    u..(data, stats)


def _bitenum(bite_str):
    return bite_str.split('.')[0].split(' ')[1]


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats, encoding="utf-8-sig") as f:
        bites = list(csv.reader(f, delimiter=';'))
    bites.pop(0)  # remove header
    bites = [[b[0], float(b[1])] for b in bites if b[1] != 'None']
    bites.sort(key=lambda x: x[1], reverse=True)

    n_most_comp = bites[:N]

    return [_bitenum(b[0]) for b in n_most_comp]


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)
