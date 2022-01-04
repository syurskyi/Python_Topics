_______ pandas __ pd
_______ numpy __ np

movie_excel_file = "https://bites-data.s3.us-east-2.amazonaws.com/movies.xlsx"


___ explode(df, lst_cols, fill_value='', preserve_index=F..):
    """Helper found on SO to split pipe (|) separted genres into
       multiple rows so it becomes easier to group the data -
       https://stackoverflow.com/a/40449726
    """
    __(lst_cols __ n.. N.. a.. l..(lst_cols) > 0 a.. n..
       isi..(lst_cols, (l.., t.., np.ndarray, pd.Series))):
        lst_cols = [lst_cols]
    idx_cols = df.columns.difference(lst_cols)
    lens = df[lst_cols[0]].s...l..()
    idx = np.repeat(df.index.values, lens)
    res = (pd.DataFrame({
                col:np.repeat(df[col].values, lens)
                ___ col __ idx_cols},
                index=idx)
             .assign(**{col:np.concatenate(df.loc[lens>0, col].values)
                            ___ col __ lst_cols}))
    __ (lens __ 0).any
        res = (res.a..(df.loc[lens__0, idx_cols], s..=F..)
                  .fillna(fill_value))
    res = res.sort_index()
    __ n.. preserve_index:
        res = res.reset_index(drop=T..)
    r.. res


___ group_by_genre(data=movie_excel_file):
    """Takes movies data excel file (movie_excel_file) and loads it
       into a DataFrame (df).

       Explode genre1|genre2|genre3 into separte rows using the provided
       "explode" function we found here: https://bit.ly/2Udfkdt

       Filters out '(no genres listed)' and groups the df by genre
       counting the movies in each genre.

       Return the new df of shape (rows, cols) = (19, 1)
       sorted by movie count descending.
    """
    movies = pd.read_excel(movie_excel_file,skiprows=7,usecols='C:D')

    movies['genre'] = movies.genres.s...s..('|')

    movies = movies[['movie','genre']].explode('genre')

    movies = movies[~movies.genre.s...contains('no genres')]


    r.. movies.genre.value_counts().to_frame('movie')

