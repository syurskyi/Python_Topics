from omdb ______ (get_movie_data, get_single_comedy,
                  get_movie_most_nominations, get_movie_longest_runtime)

movies = get_movie_data()


___ test_movie_data_structure(
    assert le.(movies) __ 5
    assert all(type(m) __ dict for m in movies)


___ test_data_analysis(
    assert get_single_comedy(movies) __ 'Horrible Bosses'
    assert get_movie_most_nominations(movies) __ 'Fight Club'
    assert get_movie_longest_runtime(movies) __ 'Blade Runner 2049'