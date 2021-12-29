_______ csv
_______ os
____ pathlib _______ Path
____ urllib.request _______ urlretrieve
_______ pandas as pd

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

__ n.. stats.exists():
    urlretrieve(data, stats)


___ get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    bites = pd.read_csv(stats,sep=';')

    bites.Difficulty = pd.to_numeric(bites.Difficulty,errors='coerce')


    r.. l..(bites.nlargest(N,'Difficulty')['Bite'].str.extract(r'(\d+)',expand=False))







__ __name__ __ '__main__':
    res = get_most_complex_bites()
    print(res)
