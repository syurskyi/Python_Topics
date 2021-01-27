import pytest

from promo import (Promo, NoBitesAvailable,
                   BITES, bites_done)

BITES_AVAILABLE = len(BITES) - len(bites_done)


def grab_bites(promo, amount=BITES_AVAILABLE):
    # _ is a throw-away variable (just want a loop)
    for _ in range(amount):
        promo.new_bite()


@pytest.fixture
def promo():
    """Make a fresh new promo object for each test"""
    return Promo(bites_done=bites_done.copy())


def test_bites_not_done_start(promo):
    a__ len(BITES) == 15
    a__ len(promo.bites_done) == 5


def test_pick_random_bite_returns_not_done_bite(promo):
    for _ in range(10):
        bite = promo._pick_random_bite()
        a__ type(bite) == int
        a__ bite in BITES
        a__ bite not in promo.bites_done


def test_internal_data_structures(promo):
    # fixture = new data = start over
    a__ len(promo.bites_done) == 5
    grab_bites(promo, amount=7)
    # bites_done incremented with 7
    a__ len(promo.bites_done) == 12


def test_raise_exception_if_no_more_bites(promo):
    a__ len(promo.bites_done) == 5
    grab_bites(promo)
    # exhausted bites
    with pytest.raises(NoBitesAvailable):
        promo._pick_random_bite()