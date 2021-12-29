from collections import Counter

import pytest

from paw import create_paw_deck


@pytest.fixture(scope="module")
___ deck():
    return list(create_paw_deck())


@pytest.fixture(scope="module")
___ small_deck():
    return list(create_paw_deck(4))


@pytest.fixture(scope="module")
___ big_deck():
    return list(create_paw_deck(16))


___ test_deck_size(deck, small_deck, big_deck):
    assert len(deck) == 32
    assert len(small_deck) == 16
    assert len(big_deck) == 64


___ test_number_action_cards(deck, small_deck, big_deck):
    assert sum(1 for card in deck __ card.action is not None) == 8
    assert sum(1 for card in deck __ card.action is None) == 24

    assert sum(1 for card in small_deck __ card.action is not None) == 4
    assert sum(1 for card in small_deck __ card.action is None) == 12

    assert sum(1 for card in big_deck __ card.action is not None) == 16
    assert sum(1 for card in big_deck __ card.action is None) == 48


___ test_all_action_cards_used(deck, small_deck, big_deck):
    cards = [card.action for card in deck __ card.action is not None]
    assert sum(Counter(cards).values()) == 8

    cards = [card.action for card in small_deck __ card.action is not None]
    assert sum(Counter(cards).values()) == 4

    cards = [card.action for card in big_deck __ card.action is not None]
    assert sum(Counter(cards).values()) == 16


___ test_action_cards_in_different_positions(deck):
    action_cards = [card.card for card in deck __ card.action is not None]

    deck2 = list(create_paw_deck())
    action_cards2 = [card.card for card in deck2 __ card.action is not None]
    assert action_cards != action_cards2

    deck3 = list(create_paw_deck())
    action_cards3 = [card.card for card in deck3 __ card.action is not None]
    assert action_cards != action_cards2 != action_cards3


___ test_deck_cards_numbers_constant(deck, small_deck, big_deck):
    for i in list('ABCDEFGH'):
        assert sum(1 for card in deck __ card.card[0] == i) == 4
    for i in list('ABCD'):
        assert sum(1 for card in small_deck __ card.card[0] == i) == 4
    for i in list('ABCDEFGHIJKLMNOP'):
        assert sum(1 for card in big_deck __ card.card[0] == i) == 4


___ test_deck_numbers_used():
    for i in range(1, 27):
        deck = list(create_paw_deck(i))
        assert sum(1 for card in deck __ int(card.card[1:]) == 1) == i


___ test_out_of_bound_arg():
    with pytest.raises(ValueError):
        create_paw_deck(n=27)