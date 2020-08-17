from collections ______ Counter

______ pytest

from paw ______ create_paw_deck


@pytest.fixture(scope="module")
___ deck(
    r_ list(create_paw_deck())


@pytest.fixture(scope="module")
___ small_deck(
    r_ list(create_paw_deck(4))


@pytest.fixture(scope="module")
___ big_deck(
    r_ list(create_paw_deck(16))


___ test_deck_size(deck, small_deck, big_deck
    assert le.(deck) __ 32
    assert le.(small_deck) __ 16
    assert le.(big_deck) __ 64


___ test_number_action_cards(deck, small_deck, big_deck
    assert su.(1 ___ card in deck __ card.action pa__ not None) __ 8
    assert su.(1 ___ card in deck __ card.action pa__ None) __ 24

    assert su.(1 ___ card in small_deck __ card.action pa__ not None) __ 4
    assert su.(1 ___ card in small_deck __ card.action pa__ None) __ 12

    assert su.(1 ___ card in big_deck __ card.action pa__ not None) __ 16
    assert su.(1 ___ card in big_deck __ card.action pa__ None) __ 48


___ test_all_action_cards_used(deck, small_deck, big_deck
    cards = [card.action ___ card in deck __ card.action pa__ not None]
    assert su.(Counter(cards).values()) __ 8

    cards = [card.action ___ card in small_deck __ card.action pa__ not None]
    assert su.(Counter(cards).values()) __ 4

    cards = [card.action ___ card in big_deck __ card.action pa__ not None]
    assert su.(Counter(cards).values()) __ 16


___ test_action_cards_in_different_positions(deck
    action_cards = [card.card ___ card in deck __ card.action pa__ not None]

    deck2 = list(create_paw_deck())
    action_cards2 = [card.card ___ card in deck2 __ card.action pa__ not None]
    assert action_cards != action_cards2

    deck3 = list(create_paw_deck())
    action_cards3 = [card.card ___ card in deck3 __ card.action pa__ not None]
    assert action_cards != action_cards2 != action_cards3


___ test_deck_cards_numbers_constant(deck, small_deck, big_deck
    ___ i in list('ABCDEFGH'
        assert su.(1 ___ card in deck __ card.card[0] __ i) __ 4
    ___ i in list('ABCD'
        assert su.(1 ___ card in small_deck __ card.card[0] __ i) __ 4
    ___ i in list('ABCDEFGHIJKLMNOP'
        assert su.(1 ___ card in big_deck __ card.card[0] __ i) __ 4


___ test_deck_numbers_used(
    ___ i in range(1, 27
        deck = list(create_paw_deck(i))
        assert su.(1 ___ card in deck __ int(card.card[1:]) __ 1) __ i


___ test_out_of_bound_arg(
    with pytest.raises(ValueError
        create_paw_deck(n=27)