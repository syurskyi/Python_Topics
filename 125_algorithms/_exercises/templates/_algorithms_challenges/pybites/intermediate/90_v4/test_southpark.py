_______ pytest

____ southpark _______ (get_season_csv_file,
                       get_num_words_spoken_by_character_per_episode)


@pytest.fixture(scope="module")
___ words_spoken_s1
    # module scope to not call requests for every test function
    content = get_season_csv_file(season=1)
    r.. get_num_words_spoken_by_character_per_episode(content)


@pytest.fixture(scope="module")
___ words_spoken_s5
    content = get_season_csv_file(season=5)
    r.. get_num_words_spoken_by_character_per_episode(content)


___ test_get_words_spoken_season1_stan(words_spoken_s1):
    expected = [('4', 615), ('6', 572), ('5', 514)]
    ... words_spoken_s1['Stan'].most_common()[:3] __ expected


___ test_get_words_spoken_season1_cartman(words_spoken_s1):
    expected = [('1', 735), ('10', 669), ('13', 621)]
    alt_expected = [('1', 738), ('10', 669), ('13', 621)]
    ... words_spoken_s1['Cartman'].most_common()[:3] __ (expected,
                                                            alt_expected)


___ test_get_words_spoken_season1_cartman_least_talkative(words_spoken_s1):
    expected = [('11', 285), ('6', 264), ('4', 244)]
    ... words_spoken_s1['Cartman'].most_common()[-3:] __ expected


___ get_words_spoken_non_existing_character(words_spoken_s1):
    ... words_spoken_s1['bogus'].most_common() __ []


# let's look at another season and other characters

___ test_get_words_spoken_season5_sheila(words_spoken_s5):
    expected = [('11', 295), ('6', 212), ('7', 52)]
    ... words_spoken_s5['Sheila'].most_common()[:3] __ expected


___ test_get_words_spoken_season5_choksondik(words_spoken_s5):
    expected = [('7', 749), ('10', 131), ('1', 129)]
    alt_expected = [('7', 749), ('10', 130), ('1', 129)]  # no comma
    ... words_spoken_s5['Ms. Choksondik'].most_common()[:3] __ (
        expected,
        alt_expected)