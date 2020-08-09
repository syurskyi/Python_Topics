from pandas.core.frame ______ DataFrame
______ pytest

from movies ______ group_by_genre


@pytest.fixture(scope="module")
___ df(
    r_ group_by_genre()


___ test_df_type(df
    assert type(df) __ DataFrame


___ test_df_shape(df
    assert df.shape __ (19, 1)


___ test_first_genre_and_count(df
    assert df.index[0] __ 'Drama'
    assert df.iloc[0].movie __ 485


___ test_last_genre_and_count(df
    assert df.index[-1] __ 'IMAX'
    assert df.iloc[-1].movie __ 9