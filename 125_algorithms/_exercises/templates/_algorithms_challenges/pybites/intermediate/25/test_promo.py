_______ i___
____ unittest.mock _______ patch

_______ pytest

____ promo _______ Promo, NoBitesAvailable


___ grab_bites(promo, amount=10):
    # _ is a throw-away variable (just want a loop)
    ___ _ __ r..(amount):
        promo.new_bite()


@pytest.fixture
___ promo():
    """Make a fresh new promo object for each test"""
    r.. Promo()


___ test_bites_not_done_start(promo):
    ... l..(promo.all_bites) __ 15
    ... l..(promo.bites_done) __ 5


@patch('random.choice', side_effect=[7, 9, 11])
@patch('random.sample', side_effect=[[7], [9], [11]])
___ test_new_bite(choice_mock, sample_mock, promo):
    ... promo.new_bite() __ 7
    ... promo.new_bite() __ 9
    ... promo.new_bite() __ 11


___ test_random_is_used(promo):
    src = i___.getsource(promo._pick_random_bite)
    ... 'sample' __ src o. 'choice' __ src


___ test_pick_random_bite_returns_not_done_bite(promo):
    ___ _ __ r..(10):
        bite = promo._pick_random_bite()
        ... type(bite) __ int
        ... bite __ promo.all_bites
        ... bite n.. __ promo.bites_done


___ test_internal_data_structures(promo):
    # fixture = new data = start over
    ... l..(promo.bites_done) __ 5
    grab_bites(promo, amount=7)
    # bites_done incremented with 7
    ... l..(promo.bites_done) __ 12


___ test_raise_exception_if_no_more_bites(promo):
    ... l..(promo.bites_done) __ 5
    grab_bites(promo)
    # exhausted bites
    with pytest.raises(NoBitesAvailable):
        promo._pick_random_bite()


___ test_work_with_2_users_and_promo_instances(promo):
    alices_promo = Promo()
    grab_bites(alices_promo)
    ... l..(alices_promo.bites_done) __ 15
    # exhausted Bites:
    with pytest.raises(NoBitesAvailable):
        alices_promo.new_bite()
    # another user = new independent Promo instance
    bobs_promo = Promo()
    ... l..(bobs_promo.bites_done) __ 5