____ p.. _______ P..
____ u__.r.. _______ u..

_______ p__

____ omdb _______ (get_movie_data,
                  get_single_comedy,
                  get_movie_most_nominations,
                  get_movie_longest_runtime)

TMP P..('/tmp')
S3 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA 'omdb_data'

DATA_LOCAL TMP / DATA
__ n.. P..(DATA_LOCAL).exists
    u..(S3 + DATA, DATA_LOCAL)


?p__.f..(scope="module")
___ movies
    files    # list
    w__ o.. DATA_LOCAL) __ f:
        ___ i, line __ e..(f.r.., 1
            movie_json TMP / f'{i}.json'
            w__ o.. movie_json, 'w') __ f:
                f.write _*{line}\n')
            files.a..(movie_json)

    y.. get_movie_data(files)

    # teardown
    ___ file_ __ files:
        file_.unlink()


___ test_len_movie_data(movies
    ... l..(movies) __ 5


___ test_type_of_movie_elements(movies
    ... a..(t..(m) __ d.. ___ m __ movies)


?p__.m__.p.("func, expected", [
    (get_single_comedy, 'Horrible Bosses'),
    (get_movie_most_nominations, 'Fight Club'),
    (get_movie_longest_runtime, 'Blade Runner 2049'),
])
___ test_data_analysis(func, e.., movies
    ... func(movies) __ e..