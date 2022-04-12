_______ i___
____ ?.m.. _______ p..

_______ p__

____ promo _______ Promo, NoBitesAvailable


___ grab_bites(promo, amount=10
    # _ is a throw-away variable (just want a loop)
    ___ _ __ r.. ?
        ?.n..


?p__.f..
___ promo
    """Make a fresh new promo object for each test"""
    r.. Promo()


___ test_bites_not_done_start(promo
    ... l..(?.a..) __ 15
    ... l.. ?.b.. __ 5


$p.. ('random.choice', s.._ 7, 9, 11])
$p.. ('random.sample', side_effect=[[7], [9], [11]])
___ test_new_bite(choice_mock, sample_mock, promo
    ... ?.n.. __ 7
    ... ?.n.. __ 9
    ... ?.n.. __ 11


___ test_random_is_used(promo
    src i___.g.. ?._p
    ... 'sample' __ src o. 'choice' __ src


___ test_pick_random_bite_returns_not_done_bite(promo
    ___ _ __ r..(10
        bite ?._p
        ... t..(bite) __ i..
        ... bite __ ?.a..
        ... bite n.. __ ?.b..


___ test_internal_data_structures(promo
    # fixture = new data = start over
    ... l.. ?.b.. __ 5
    grab_bites(promo, a.._7)
    # bites_done incremented with 7
    ... l.. ?.b.. __ 12


___ test_raise_exception_if_no_more_bites(promo
    ... l.. ?.b.. __ 5
    g.. ?
    # exhausted bites
    w__ p__.r.. N..
        ?._p


___ test_work_with_2_users_and_promo_instances(promo
    alices_promo Promo()
    grab_bites(alices_promo)
    ... l..?.b.. __ 15
    # exhausted Bites:
    w__ p__.r.. N..
        ?.n..
    # another user = new independent Promo instance
    bobs_promo Promo()
    ... l.. ?.b.. __ 5
