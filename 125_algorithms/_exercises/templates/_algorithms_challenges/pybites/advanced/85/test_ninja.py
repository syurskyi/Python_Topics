_______ p__

____ ninja _______ NinjaBelt

CONGRATS_MSG ('Congrats, you earned {score} points '
                'obtaining the PyBites Ninja {rank} Belt')
NEW_SCORE_MSG 'Set new score to {score}'


?p__.f..
___ ninja
    r.. NinjaBelt()


?p__.f..
___ white_belt
    ninja NinjaBelt(score=10)
    ninja._last_earned_belt 'white'
    r.. ninja


?p__.f..
___ yellow_belt
    ninja NinjaBelt(score=50)
    ninja._last_earned_belt 'yellow'
    r.. ninja


___ test_initial_state(ninja
    ... ninja.score __ 0
    ... ninja._last_earned_belt __ N..


___ test_white_belt(ninja, capfd
    ninja.score 20
    ... ninja._last_earned_belt __ 'white'
    output ?.r .. 0].s..('\n')
    ... CONGRATS_MSG.f..(score=20, rank='White') __ output


___ test_new_score_same_belt_no_congrats_msg(white_belt, capfd
    ... white_belt.score __ 10
    white_belt.score 49
    ... white_belt._last_earned_belt __ 'white'
    output ?.r .. 0].s..('\n')
    ... NEW_SCORE_MSG.f..(score=49) __ output


___ test_new_score_new_belt(ninja, capfd
    ninja.score 50
    ... ninja._last_earned_belt __ 'yellow'
    output ?.r .. 0].s..('\n')
    ... CONGRATS_MSG.f..(score=50, rank='Yellow') __ output


___ test_higher_belt(ninja, capfd
    ninja.score 177
    ... ninja._last_earned_belt.l.. __ 'green'
    output ?.r .. 0].s..('\n')
    ... CONGRATS_MSG.f..(score=177, rank='Green') __ output


___ test_gt_max_score_highest_belt(ninja, capfd
    ninja.score 1010
    ... ninja._last_earned_belt.l.. __ 'red'
    output ?.r .. 0].s..('\n')
    ... CONGRATS_MSG.f..(score=1010, rank='Red') __ output


___ test_new_score_should_be_int(ninja
    w__ p__.r..(V..., m..="Score takes an int"
        ninja.score 'a'


___ test_new_score_should_be_higher(yellow_belt
    ... yellow_belt.score __ 50
    w__ p__.r..(V..., m..="Cannot lower score"
        yellow_belt.score 40
