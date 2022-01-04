_______ p__

____ speaker _______ (get_pycon_speaker_first_names,
                     get_percentage_of_female_speakers)


@p__.fixture(scope='module')
___ first_names
    r.. get_pycon_speaker_first_names()


___ test_get_pycon_speaker_first_names(first_names):
    ... l..(first_names) __ 112
    ... 'Luciano' __ first_names
    ... 'Erin' __ first_names
    ... 'Rachael' __ first_names


___ test_get_percentage_of_female_speakers(first_names):
    actual = get_percentage_of_female_speakers(first_names)
    expected = 28.57
    ... actual __ expected