____ pandas.core.frame _______ DataFrame
_______ p__

____ movies _______ group_by_genre


?p__.f..(scope="module")
___ df
    r.. group_by_genre()


___ test_df_type(df
    ... t..(df) __ DataFrame


___ test_df_shape(df
    ... df.shape __ (19, 1)


___ test_first_genre_and_count(df
    ... df.index[0] __ 'Drama'
    ... df.iloc[0].movie __ 485


___ test_last_genre_and_count(df
    ... df.index[-1] __ 'IMAX'
    ... df.iloc[-1].movie __ 9