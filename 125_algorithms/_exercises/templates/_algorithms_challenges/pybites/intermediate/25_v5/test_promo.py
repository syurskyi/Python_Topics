_______ pytest

____ promo _______ (Promo, NoBitesAvailable,
                   BITES, bites_done)

BITES_AVAILABLE = l..(BITES) - l..(bites_done)


___ grab_bites(promo, amount=BITES_AVAILABLE):
    # _ is a throw-away variable (just want a loop)
    ___ _ __ r..(amount):
        promo.new_bite()


@pytest.fixture
___ promo
    """Make a fresh new promo object for each test"""
    r.. Promo(bites_done=bites_done.copy())


___ test_bites_not_done_start(promo):
    ... l..(BITES) __ 15
    ... l..(promo.bites_done) __ 5


___ test_pick_random_bite_returns_not_done_bite(promo):
    ___ _ __ r..(10):
        bite = promo._pick_random_bite()
        ... t..(bite) __ i..
        ... bite __ BITES
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