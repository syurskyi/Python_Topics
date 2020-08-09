______ pytest

from promo ______ (Promo, NoBitesAvailable,
                   BITES, bites_done)

BITES_AVAILABLE = le.(BITES) - le.(bites_done)


___ grab_bites(promo, amount=BITES_AVAILABLE
    # _ is a throw-away variable (just want a loop)
    for _ in range(amount
        promo.new_bite()


@pytest.fixture
___ promo(
    """Make a fresh new promo object for each test"""
    r_ Promo(bites_done=bites_done.copy())


___ test_bites_not_done_start(promo
    assert le.(BITES) __ 15
    assert le.(promo.bites_done) __ 5


___ test_pick_random_bite_returns_not_done_bite(promo
    for _ in range(10
        bite = promo._pick_random_bite()
        assert type(bite) __ int
        assert bite in BITES
        assert bite not in promo.bites_done


___ test_internal_data_structures(promo
    # fixture = new data = start over
    assert le.(promo.bites_done) __ 5
    grab_bites(promo, amount=7)
    # bites_done incremented with 7
    assert le.(promo.bites_done) __ 12


___ test_raise_exception_if_no_more_bites(promo
    assert le.(promo.bites_done) __ 5
    grab_bites(promo)
    # exhausted bites
    with pytest.raises(NoBitesAvailable
        promo._pick_random_bite()