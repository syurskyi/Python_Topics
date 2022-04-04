____ d__ _______ date
_______ __
____ p.. _______ P..
_______ p..
____ t___ _______ S.., N..
____ u__.r.. _______ u..

TMP = P..(__.g..("TMP", "/tmp"
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
PICKLE_INFILE = TMP / 'input.pkl'
PICKLE_OUTFILE = TMP / 'output.pkl'


c_ MovieRented(N..
    title: s..
    price: i..
    date: date


___ download_pickle_file
    """download a pickle file we created with a
       list of namedtuples
    """
    u.. _*{S3}/bite317.pkl', PICKLE_INFILE)


___ deserialize(pkl_file: P.. = PICKLE_INFILE) __ S..[N..]:
    """Load the list of namedtuples from the pickle file passed in"""
    w__ o.. pkl_file, 'rb') __ f:
        data = f.r..
        r.. p...loads(data)


___ serialize(pkl_file: P.. = PICKLE_OUTFILE,
              data: S..[N..] = N..) __ N..
    """Save the data passed in to the pickle file passed in"""
    __ data __ N..
        data = deserialize()
    w__ o.. pkl_file, __) __ f:
        p...d.. data, f)
