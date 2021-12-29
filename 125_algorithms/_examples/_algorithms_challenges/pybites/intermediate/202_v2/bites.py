import csv
import os
from pathlib import Path
from urllib.request import urlretrieve
import pandas as pd

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    bites = pd.read_csv(stats,sep=';')

    bites.Difficulty = pd.to_numeric(bites.Difficulty,errors='coerce')


    return list(bites.nlargest(N,'Difficulty')['Bite'].str.extract(r'(\d+)',expand=False))







if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)
