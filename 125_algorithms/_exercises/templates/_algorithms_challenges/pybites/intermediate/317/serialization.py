____ datetime _______ date
_______ os
____ pathlib _______ Path
_______ pickle
____ typing _______ Sequence, NamedTuple
____ urllib.request _______ urlretrieve

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
    file = open(pkl_file, "rb")
    nt = pickle.load(file)
    file.close()
    r.. nt


___ serialize(pkl_file: Path = PICKLE_OUTFILE,
              data: Sequence[NamedTuple] = N..) -> N..
    """Save the data passed in to the pickle file passed in"""
    __ data __ N..
        data = deserialize()
    # you code ...
    ____:
        file = open(pkl_file, "ab")
        pickle.dump(data, file)
        file.close()

__ __name__ __ "__main__":
    download_pickle_file()
    deserialize()