from datetime import date
import os
from pathlib import Path
import pickle
from typing import Sequence, NamedTuple
from urllib.request import urlretrieve

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
PICKLE_INFILE = TMP / 'input.pkl'
PICKLE_OUTFILE = TMP / 'output.pkl'


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


def download_pickle_file():
    """download a pickle file we created with a
       list of namedtuples
    """
    urlretrieve(f'{S3}/bite317.pkl', PICKLE_INFILE)


def deserialize(pkl_file: Path = PICKLE_INFILE) -> Sequence[NamedTuple]:
    """Load the list of namedtuples from the pickle file passed in"""
    file = open(pkl_file, "rb")
    nt = pickle.load(file)
    file.close()
    return nt


def serialize(pkl_file: Path = PICKLE_OUTFILE,
              data: Sequence[NamedTuple] = None) -> None:
    """Save the data passed in to the pickle file passed in"""
    if data is None:
        data = deserialize()
    # you code ...
    else:
        file = open(pkl_file, "ab")
        pickle.dump(data, file)
        file.close()

if __name__ == "__main__":
    download_pickle_file()
    deserialize()