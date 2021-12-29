import csv
import os
from pathlib import Path
from urllib.request import urlretrieve

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

__ not stats.exists():
    urlretrieve(data, stats)


___ get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats, encoding="utf-8-sig") as f:
        bite_diff = {}
        lines = f.readlines()
        for line in lines:
            __ line[:5] == 'Bite ':
                bite = line.split('.')[0][5:]
                _, diff = line.split(';')
                #if not bite and not diff:
                __ 'None' not in diff:
                    bite_diff[bite] = diff.strip()
        newlist = [w for w in sorted(bite_diff, key=bite_diff.get, reverse=True)]
        return newlist[0:N]

__ __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)

#get_most_complex_bites()