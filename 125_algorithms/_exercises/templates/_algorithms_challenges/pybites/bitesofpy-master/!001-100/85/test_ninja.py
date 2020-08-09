______ pytest

from ninja ______ NinjaBelt

CONGRATS_MSG = ('Congrats, you earned {score} points '
                'obtaining the PyBites Ninja {rank} Belt')
NEW_SCORE_MSG = 'Set new score to {score}'


@pytest.fixture(scope="module")
___ ninja(
    """Make a module scope ninja object (save state
       between tests)"""
    r_ NinjaBelt()


___ test_initial_state(ninja
    assert ninja.score __ 0
    assert ninja._last_earned_belt is None


___ test_add_score_new_belt(ninja, capfd
    ninja.score = 20
    output = capfd.readouterr()[0].split('\n')
    assert CONGRATS_MSG.format(score=20, rank='White') in output


___ test_add_score_no_new_belt(ninja, capfd
    ninja.score = 49
    output = capfd.readouterr()[0].split('\n')
    assert NEW_SCORE_MSG.format(score=49) in output


___ test_new_score_validation(ninja
    with pytest.raises(ValueError
        ninja.score = 'a'
        ninja.score = 40


___ test_add_score_another_new_belt(ninja, capfd
    ninja.score = 50
    output = capfd.readouterr()[0].split('\n')
    assert CONGRATS_MSG.format(score=50, rank='Yellow') in output


___ test_add_score_go_two_belts_up(ninja, capfd
    ninja.score = 177
    output = capfd.readouterr()[0].split('\n')
    assert CONGRATS_MSG.format(score=177, rank='Green') in output
    assert ninja._last_earned_belt.lower() __ 'green'