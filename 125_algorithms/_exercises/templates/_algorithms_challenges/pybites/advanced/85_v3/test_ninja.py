_______ p__

____ ninja _______ NinjaBelt

CONGRATS_MSG = ('Congrats, you earned {score} points '
                'obtaining the PyBites Ninja {rank} Belt')
NEW_SCORE_MSG = 'Set new score to {score}'


@p__.fixture(scope="module")
___ ninja
    """Make a module scope ninja object (save state
       between tests)"""
    r.. NinjaBelt()


___ test_initial_state(ninja):
    ... ninja.score __ 0
    ... ninja._last_earned_belt __ N..


___ test_add_score_new_belt(ninja, capfd):
    ninja.score = 20
    output = capfd.readouterr()[0].s..('\n')
    ... CONGRATS_MSG.f..(score=20, rank='White') __ output


___ test_add_score_no_new_belt(ninja, capfd):
    ninja.score = 49
    output = capfd.readouterr()[0].s..('\n')
    ... NEW_SCORE_MSG.f..(score=49) __ output


___ test_new_score_validation(ninja):
    w__ p__.r..(ValueError):
        ninja.score = 'a'
        ninja.score = 40


___ test_add_score_another_new_belt(ninja, capfd):
    ninja.score = 50
    output = capfd.readouterr()[0].s..('\n')
    ... CONGRATS_MSG.f..(score=50, rank='Yellow') __ output


___ test_add_score_go_two_belts_up(ninja, capfd):
    ninja.score = 177
    output = capfd.readouterr()[0].s..('\n')
    ... CONGRATS_MSG.f..(score=177, rank='Green') __ output
    ... ninja._last_earned_belt.l.. __ 'green'