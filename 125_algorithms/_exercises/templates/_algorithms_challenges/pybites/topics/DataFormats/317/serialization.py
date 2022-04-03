____ d__ _______ date
_______ __
____ pathlib _______ Path
_______ pickle
____ typing _______ Sequence, NamedTuple
____ u__.r.. _______ u..
_______ time


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
    input_file = o.. pkl_file, "rb")
    r.. pickle.load(input_file)


___ serialize(pkl_file: Path = PICKLE_OUTFILE,
              data: Sequence[NamedTuple] = N..) __ N..
    """Save the data passed in to the pickle file passed in"""
    #if data is None:
    #    data = deserialize()
    output_file = o.. pkl_file, "wb")
    pickle.dump(data, output_file)

c_ Bite(NamedTuple
    title: s..
    number: i..
    level: s..

data = [
    Bite('Sum of Numbers', 1, 'Beginner'),
    Bite('Regex Fun', 2, 'Advanced'),
]
pkl_file = 'khoo.pickle'
serialize(pkl_file, data=data)
actual = deserialize(pkl_file)

print(actual)