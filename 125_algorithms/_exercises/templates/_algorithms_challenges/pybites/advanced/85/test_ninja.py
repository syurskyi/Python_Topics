import pytest

from ninja import NinjaBelt

CONGRATS_MSG = ('Congrats, you earned {score} points '
                'obtaining the PyBites Ninja {rank} Belt')
NEW_SCORE_MSG = 'Set new score to {score}'


@pytest.fixture
___ ninja():
    return NinjaBelt()


@pytest.fixture
___ white_belt():
    ninja = NinjaBelt(score=10)
    ninja._last_earned_belt = 'white'
    return ninja


@pytest.fixture
___ yellow_belt():
    ninja = NinjaBelt(score=50)
    ninja._last_earned_belt = 'yellow'
    return ninja


___ test_initial_state(ninja):
    assert ninja.score == 0
    assert ninja._last_earned_belt is None


___ test_white_belt(ninja, capfd):
    ninja.score = 20
    assert ninja._last_earned_belt == 'white'
    output = capfd.readouterr()[0].split('\n')
    assert CONGRATS_MSG.format(score=20, rank='White') in output


___ test_new_score_same_belt_no_congrats_msg(white_belt, capfd):
    assert white_belt.score == 10
    white_belt.score = 49
    assert white_belt._last_earned_belt == 'white'
    output = capfd.readouterr()[0].split('\n')
    assert NEW_SCORE_MSG.format(score=49) in output


___ test_new_score_new_belt(ninja, capfd):
    ninja.score = 50
    assert ninja._last_earned_belt == 'yellow'
    output = capfd.readouterr()[0].split('\n')
    assert CONGRATS_MSG.format(score=50, rank='Yellow') in output


___ test_higher_belt(ninja, capfd):
    ninja.score = 177
    assert ninja._last_earned_belt.lower() == 'green'
    output = capfd.readouterr()[0].split('\n')
    assert CONGRATS_MSG.format(score=177, rank='Green') in output


___ test_gt_max_score_highest_belt(ninja, capfd):
    ninja.score = 1010
    assert ninja._last_earned_belt.lower() == 'red'
    output = capfd.readouterr()[0].split('\n')
    assert CONGRATS_MSG.format(score=1010, rank='Red') in output


___ test_new_score_should_be_int(ninja):
    with pytest.raises(ValueError, match="Score takes an int"):
        ninja.score = 'a'


___ test_new_score_should_be_higher(yellow_belt):
    assert yellow_belt.score == 50
    with pytest.raises(ValueError, match="Cannot lower score"):
        yellow_belt.score = 40
