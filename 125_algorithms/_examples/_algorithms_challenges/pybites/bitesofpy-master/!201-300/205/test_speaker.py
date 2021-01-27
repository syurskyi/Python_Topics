import pytest

from speaker import (get_pycon_speaker_first_names,
                     get_percentage_of_female_speakers)


@pytest.fixture(scope='module')
def first_names():
    return get_pycon_speaker_first_names()


def test_get_pycon_speaker_first_names(first_names):
    a__ len(first_names) == 112
    a__ 'Luciano' in first_names
    a__ 'Erin' in first_names
    a__ 'Rachael' in first_names


def test_get_percentage_of_female_speakers(first_names):
    actual = get_percentage_of_female_speakers(first_names)
    expected = 28.57
    a__ actual == expected