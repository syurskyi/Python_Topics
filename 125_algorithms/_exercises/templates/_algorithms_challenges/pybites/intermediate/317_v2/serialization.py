____ d__ _______ date
_______ os
____ pathlib _______ Path
_______ pickle
____ typing _______ Sequence, NamedTuple
____ urllib.request _______ urlretrieve

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
PICKLE_INFILE = TMP / 'input.pkl'
PICKLE_OUTFILE = TMP / 'output.pkl'


c_ MovieRented(NamedTuple):
    title: s..
    price: i..
    date: date


___ download_pickle_file
    """download a pickle file we created with a
       list of namedtuples
    """
    urlretrieve(f'{S3}/bite317.pkl', PICKLE_INFILE)


___ deserialize(pkl_file: Path = PICKLE_INFILE) __ Sequence[NamedTuple]:
    """Load the list of namedtuples from the pickle file passed in"""
    w__ open(pkl_file, 'rb') __ f:
        data = f.read()
        r.. pickle.loads(data)


___ serialize(pkl_file: Path = PICKLE_OUTFILE,
              data: Sequence[NamedTuple] = N..) __ N..
    """Save the data passed in to the pickle file passed in"""
    __ data __ N..
        data = deserialize()
    w__ open(pkl_file, 'wb') __ f:
        pickle.dump(data, f)
