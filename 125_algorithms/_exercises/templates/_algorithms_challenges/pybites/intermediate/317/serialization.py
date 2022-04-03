____ d__ _______ date
_______ __
____ pathlib _______ Path
_______ pickle
____ typing _______ Sequence, NamedTuple
____ u__.r.. _______ u..

TMP = Path(__.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
PICKLE_INFILE = TMP / 'input.pkl'
PICKLE_OUTFILE = TMP / 'output.pkl'


c_ MovieRented(NamedTuple
    title: s..
    price: i..
    date: date


___ download_pickle_file
    """download a pickle file we created with a
       list of namedtuples
    """
    u.. _*{S3}/bite317.pkl', PICKLE_INFILE)


___ deserialize(pkl_file: Path = PICKLE_INFILE) __ Sequence[NamedTuple]:
    """Load the list of namedtuples from the pickle file passed in"""
    file = o.. pkl_file, "rb")
    nt = pickle.load(file)
    file.c..
    r.. nt


___ serialize(pkl_file: Path = PICKLE_OUTFILE,
              data: Sequence[NamedTuple] = N..) __ N..
    """Save the data passed in to the pickle file passed in"""
    __ data __ N..
        data = deserialize()
    # you code ...
    ____:
        file = o.. pkl_file, "ab")
        pickle.dump(data, file)
        file.c..

__ _______ __ _______
    download_pickle_file()
    deserialize()