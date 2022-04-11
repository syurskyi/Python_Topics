_______ csv
_______ __
____ p.. _______ P..
____ u__.r.. _______ u..
_______ p.... __ pd

data 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp  P..(__.g..("TMP", "/tmp"
stats tmp / 'bites.csv'

__ n.. stats.exists
    u..(data, stats)


___ get_most_complex_bites(N=10, stats=stats
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    bites pd.read_csv(stats,sep=';')

    bites.Difficulty pd.to_numeric(bites.Difficulty,errors='coerce')


    r.. l..(bites.nlargest(N,'Difficulty') 'Bite' .s...extract(r'(\d+)',expand=F..







__ _____ __ _____
    res get_most_complex_bites()
    print(res)
