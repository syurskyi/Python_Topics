______ pytest

from speaker ______ (get_pycon_speaker_first_names,
                     get_percentage_of_female_speakers)


@pytest.fixture(scope='module')
___ first_names(
    r_ get_pycon_speaker_first_names()


___ test_get_pycon_speaker_first_names(first_names
    assert le.(first_names) __ 112
    assert 'Luciano' in first_names
    assert 'Erin' in first_names
    assert 'Rachael' in first_names


___ test_get_percentage_of_female_speakers(first_names
    actual = get_percentage_of_female_speakers(first_names)
    expected = 28.57
    assert actual __ expected