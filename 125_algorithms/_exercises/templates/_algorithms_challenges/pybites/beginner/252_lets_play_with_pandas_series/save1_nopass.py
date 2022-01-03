_______ numpy as np
_______ pandas as pd


___ return_at_index(ser: pd.Series, idx: int) -> object:
    """Return the Object at the given index of the Series
    If you want to be extra careful catch and raise an error if
       the index does not exist.
    """
    r.. ser.index[idx]


___ get_slice(ser: pd.Series, start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end.
    """
    r.. ser.iloc[start:end]


___ get_slice_inclusive(ser: pd.Series,
                        start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end inclusive.
    """
    r.. ser.iloc[start:end + 1]


___ return_head(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the first num elements of the given Series.
    """
    r.. ser.head(num)


___ return_tail(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the last num elements of the given Series.
    """
    r.. ser.tail(num)


___ get_index(ser: pd.Series) -> pd.core.indexes.base.Index:
    """Return all indexes of the given Series.
    """
    r.. ser.index


___ get_values(ser: pd.Series) -> np.ndarray:
    """Return all the values of the given Series.
    """
    r.. np.array(ser.values)


___ get_every_second_indexes(ser: pd.Series,
                             even_index=T..) -> pd.core.series.Series:
    """Return all rows where the index is either even or odd.
    If even_index is True return every index where idx % 2 == 0
    If even_index is False return every index where idx % 2 != 0
    Assume default indexing i.e. 0 -> n
    """
    __ even_index __ F..:
        r.. ser.index % 2 != 0
    ____:
        r.. ser.index % 2 __ 0
