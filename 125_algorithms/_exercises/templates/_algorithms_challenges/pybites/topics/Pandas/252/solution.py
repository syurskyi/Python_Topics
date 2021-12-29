import numpy as np
import pandas as pd


___ return_at_index(ser: pd.Series, idx: int) -> object:
    """Return the Object at the given index of the Series
    If you want to be extra careful catch and raise an error if
       the index does not exist.
    """
    try:
        return ser[idx]
    except KeyError:
        raise


___ get_slice(ser: pd.Series, start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end.
    """
    return ser[start:end]


___ get_slice_inclusive(ser: pd.Series,
                        start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end inclusive.
    """
    return ser.loc[start:end]


___ return_head(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the first num elements of the given Series.
    """
    return ser.head(num)


___ return_tail(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the last num elements of the given Series.
    """
    return ser.tail(num)


___ get_index(ser: pd.Series) -> pd.core.indexes.base.Index:
    """Return all indexes of the given Series.
    """
    return ser.index


___ get_values(ser: pd.Series) -> np.ndarray:
    """Return all the values of the given Series.
    """
    return ser.values


___ get_every_second_indexes(ser: pd.Series,
                             even_index=True) -> pd.core.series.Series:
    """Return all rows where the index is either even or odd.
    If even_index is True return every index where idx % 2 == 0
    If even_index is False return every index where idx % 2 != 0
    Assume default indexing i.e. 0 -> n
    """
    first_idx = 0 __ even_index else 1
    return ser.iloc[first_idx::2]