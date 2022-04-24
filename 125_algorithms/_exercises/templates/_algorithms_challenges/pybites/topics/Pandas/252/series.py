_______ n.... __ np
_______ p.... __ pd


___ return_at_index ser ?.S..  idx i.. __ o..
    """Return the Object at the given index of the Series
    If you want to be extra careful catch and raise an error if
       the index does not exist.
    """
    ___
        r.. ser[idx]
    ______ K..
        r.. K..

___ get_slice ser ?.S.., start: i.., end: i..) __ ?.c__.s__.S.:
    """Return the slice of the given Series in the range between
    start and end.
    """
    ___
        r.. ser ?|?
    ______ K..
        r.. K..

___ get_slice_inclusive ser ?.S..,
                        start: i.., end: i..) __ ?.c__.s__.S.:
    """Return the slice of the given Series in the range between
    start and end inclusive.
    """
    ___
        r.. ?.loc ?|?
    ______ K..
        r.. K..

___ return_head ser ?.S.., num: i..) __ ?.c__.s__.S.:
    """Return the first num elements of the given Series.
    """
    ___
        r.. ?.h.. ?
    ______ K..
        r.. K..

___ return_tail ser ?.S.., num: i..) __ ?.c__.s__.S.:
    """Return the last num elements of the given Series.
    """
    ___
        r.. ?.t.. ?
    ______ K..
        r.. K..

___ get_index ser ?.S..) __ >?.c__.i__.b__.I..
    """Return all indexes of the given Series.
    """
    ___
        r.. ?.index
    ______ K..
        r.. K..

___ get_values ser ?.S..) __ ?.n
    """Return all the values of the given Series.
    """
    #return ser.to_numpy()
    r.. ?.values

___ get_every_second_indexes ser ?.S..,
                             even_index=T..) __ ?.c__.s__.S.:
    """Return all rows where the index is either even or odd.
    If even_index is True return every index where idx % 2 == 0
    If even_index is False return every index where idx % 2 != 0
    Assume default indexing i.e. 0 -> n
    """
    r.. ?,i..[l.... x: x.index % 2 __ 0] __ even_index ____ ?,i..[l.... x: x.index % 2 !_ 0]









pdseries ?.S..([f__(n) / 1000 ___ n __ r..(0, 1001)])

print(t..(pdseries.head(5)))
print(pdseries.head(5)[4])


#print(return_head(pdseries,5)[5])