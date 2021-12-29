____ datetime _______ date
_______ os
____ pathlib _______ Path
_______ pickle
____ typing _______ Sequence, NamedTuple
____ urllib.request _______ urlretrieve
_______ time


TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
PICKLE_INFILE = TMP / 'input.pkl'
PICKLE_OUTFILE = TMP / 'output.pkl'


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


___ download_pickle_file():
    """download a pickle file we created with a
       list of namedtuples
    """
    urlretrieve(f'{S3}/bite317.pkl', PICKLE_INFILE)


___ deserialize(pkl_file: Path = PICKLE_INFILE) -> Sequence[NamedTuple]:
    """Load the list of namedtuples from the pickle file passed in"""
    input_file = open(pkl_file, "rb")
    r.. pickle.load(input_file)


___ serialize(pkl_file: Path = PICKLE_OUTFILE,
              data: Sequence[NamedTuple] = N..) -> N..
    """Save the data passed in to the pickle file passed in"""
    #if data is None:
    #    data = deserialize()
    output_file = open(pkl_file, "wb")
    pickle.dump(data, output_file)

class Bite(NamedTuple):
    title: str
    number: int
    level: str

data = [
    Bite('Sum of Numbers', 1, 'Beginner'),
    Bite('Regex Fun', 2, 'Advanced'),
]
pkl_file = 'khoo.pickle'
serialize(pkl_file, data=data)
actual = deserialize(pkl_file)

print(actual)