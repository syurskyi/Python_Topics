import numpy as np
import pandas as pd


def return_at_index(ser: pd.Series, idx: int) -> object:
    """Return the Object at the given index of the Series
    If you want to be extra careful catch and raise an error if
       the index does not exist.
    """
    try:
        return ser[idx]
    except KeyError:
        raise KeyError

def get_slice(ser: pd.Series, start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end.
    """
    try:
        return ser[start:end]
    except KeyError:
        raise KeyError

def get_slice_inclusive(ser: pd.Series,
                        start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end inclusive.
    """
    try:
        return ser.loc[start:end]
    except KeyError:
        raise KeyError

def return_head(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the first num elements of the given Series.
    """
    try:
        return ser.head(num)
    except KeyError:
        raise KeyError

def return_tail(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the last num elements of the given Series.
    """
    try:
        return ser.tail(num)
    except KeyError:
        raise KeyError

def get_index(ser: pd.Series) -> pd.core.indexes.base.Index:
    """Return all indexes of the given Series.
    """
    try:
        return ser.index
    except KeyError:
        raise KeyError

def get_values(ser: pd.Series) -> np.ndarray:
    """Return all the values of the given Series.
    """
    #return ser.to_numpy()
    return ser.values

def get_every_second_indexes(ser: pd.Series,
                             even_index=True) -> pd.core.series.Series:
    """Return all rows where the index is either even or odd.
    If even_index is True return every index where idx % 2 == 0
    If even_index is False return every index where idx % 2 != 0
    Assume default indexing i.e. 0 -> n
    """
    return ser.iloc[lambda x: x.index % 2 == 0] if even_index else ser.iloc[lambda x: x.index % 2 != 0]









pdseries = pd.Series([float(n) / 1000 for n in range(0, 1001)])

print(type(pdseries.head(5)))
print(pdseries.head(5)[4])


#print(return_head(pdseries,5)[5])