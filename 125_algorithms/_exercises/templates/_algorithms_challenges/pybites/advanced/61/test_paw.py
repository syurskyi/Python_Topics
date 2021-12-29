____ collections _______ Counter

_______ pytest

____ paw _______ create_paw_deck


@pytest.fixture(scope="module")
___ deck():
    r.. l..(create_paw_deck())


@pytest.fixture(scope="module")
___ small_deck():
    r.. l..(create_paw_deck(4))


@pytest.fixture(scope="module")
___ big_deck():
    r.. l..(create_paw_deck(16))


___ test_deck_size(deck, small_deck, big_deck):
    ... l..(deck) __ 32
    ... l..(small_deck) __ 16
    ... l..(big_deck) __ 64


___ test_number_action_cards(deck, small_deck, big_deck):
    ... s..(1 ___ card __ deck __ card.action __ n.. N..) __ 8
    ... s..(1 ___ card __ deck __ card.action __ N..) __ 24

    ... s..(1 ___ card __ small_deck __ card.action __ n.. N..) __ 4
    ... s..(1 ___ card __ small_deck __ card.action __ N..) __ 12

    ... s..(1 ___ card __ big_deck __ card.action __ n.. N..) __ 16
    ... s..(1 ___ card __ big_deck __ card.action __ N..) __ 48


___ test_all_action_cards_used(deck, small_deck, big_deck):
    cards = [card.action ___ card __ deck __ card.action __ n.. N..]
    ... s..(Counter(cards).values()) __ 8

    cards = [card.action ___ card __ small_deck __ card.action __ n.. N..]
    ... s..(Counter(cards).values()) __ 4

    cards = [card.action ___ card __ big_deck __ card.action __ n.. N..]
    ... s..(Counter(cards).values()) __ 16


___ test_action_cards_in_different_positions(deck):
    action_cards = [card.card ___ card __ deck __ card.action __ n.. N..]

    deck2 = l..(create_paw_deck())
    action_cards2 = [card.card ___ card __ deck2 __ card.action __ n.. N..]
    ... action_cards != action_cards2

    deck3 = l..(create_paw_deck())
    action_cards3 = [card.card ___ card __ deck3 __ card.action __ n.. N..]
    ... action_cards != action_cards2 != action_cards3


___ test_deck_cards_numbers_constant(deck, small_deck, big_deck):
    ___ i __ l..('ABCDEFGH'):
        ... s..(1 ___ card __ deck __ card.card[0] __ i) __ 4
    ___ i __ l..('ABCD'):
        ... s..(1 ___ card __ small_deck __ card.card[0] __ i) __ 4
    ___ i __ l..('ABCDEFGHIJKLMNOP'):
        ... s..(1 ___ card __ big_deck __ card.card[0] __ i) __ 4


___ test_deck_numbers_used():
    ___ i __ r..(1, 27):
        deck = l..(create_paw_deck(i))
        ... s..(1 ___ card __ deck __ int(card.card[1:]) __ 1) __ i


___ test_out_of_bound_arg():
    with pytest.raises(ValueError):
        create_paw_deck(n=27)
