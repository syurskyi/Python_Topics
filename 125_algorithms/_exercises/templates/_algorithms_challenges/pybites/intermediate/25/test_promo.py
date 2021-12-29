import inspect
from unittest.mock import patch

import pytest

from promo import Promo, NoBitesAvailable


___ grab_bites(promo, amount=10):
    # _ is a throw-away variable (just want a loop)
    for _ in range(amount):
        promo.new_bite()


@pytest.fixture
___ promo():
    """Make a fresh new promo object for each test"""
    return Promo()


___ test_bites_not_done_start(promo):
    assert len(promo.all_bites) == 15
    assert len(promo.bites_done) == 5


@patch('random.choice', side_effect=[7, 9, 11])
@patch('random.sample', side_effect=[[7], [9], [11]])
___ test_new_bite(choice_mock, sample_mock, promo):
    assert promo.new_bite() == 7
    assert promo.new_bite() == 9
    assert promo.new_bite() == 11


___ test_random_is_used(promo):
    src = inspect.getsource(promo._pick_random_bite)
    assert 'sample' in src or 'choice' in src


___ test_pick_random_bite_returns_not_done_bite(promo):
    for _ in range(10):
        bite = promo._pick_random_bite()
        assert type(bite) == int
        assert bite in promo.all_bites
        assert bite not in promo.bites_done


___ test_internal_data_structures(promo):
    # fixture = new data = start over
    assert len(promo.bites_done) == 5
    grab_bites(promo, amount=7)
    # bites_done incremented with 7
    assert len(promo.bites_done) == 12


___ test_raise_exception_if_no_more_bites(promo):
    assert len(promo.bites_done) == 5
    grab_bites(promo)
    # exhausted bites
    with pytest.raises(NoBitesAvailable):
        promo._pick_random_bite()


___ test_work_with_2_users_and_promo_instances(promo):
    alices_promo = Promo()
    grab_bites(alices_promo)
    assert len(alices_promo.bites_done) == 15
    # exhausted Bites:
    with pytest.raises(NoBitesAvailable):
        alices_promo.new_bite()
    # another user = new independent Promo instance
    bobs_promo = Promo()
    assert len(bobs_promo.bites_done) == 5