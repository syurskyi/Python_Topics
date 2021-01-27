import pytest

from groceries import Item, Groceries, create_parser, handle_args


@pytest.fixture
def cart():
    # faking some data (normally would load from DB)
    products = 'celery apples water coffee chicken pizza'.split()
    prices = [1, 4, 2, 5, 6, 4]
    cravings = False, False, False, False, False, True

    items = []
    for item in zip(products, prices, cravings):
        items.append(Item(*item))

    return Groceries(items)


@pytest.fixture
def parser():
    return create_parser()


def test_list(parser, cart, capfd):
    args = parser.parse_args(['-l'])
    handle_args(args, cart)
    output = capfd.readouterr()[0].split('\n')
    a__ 'pizza (craving)                |   4' in output
    a__ 'Total                          |  22' in output


def test_search(parser, cart, capfd):
    args = parser.parse_args(['-s', 'coffee'])
    handle_args(args, cart)
    output = capfd.readouterr()[0].split('\n')
    a__ 'coffee                         |   5' in output
    a__ 'Total                          |   5' in output


def test_add(parser, cart):
    a__ len(cart) == 6
    a__ cart.due == 22

    args = parser.parse_args(['-a', 'honey', '5', 'False'])
    handle_args(args, cart)

    a__ len(cart) == 7
    a__ cart.due == 27

    new_item = cart[-1]
    a__ new_item.product == 'honey'
    a__ new_item.price == 5
    a__ not new_item.craving


def test_delete(parser, cart):
    # nice: fixture gives me a clean slate each test!
    a__ len(cart) == 6
    a__ cart.due == 22

    args = parser.parse_args(['-d', 'pizza'])
    handle_args(args, cart)

    a__ len(cart) == 5
    a__ cart.due == 18

    new_last_item = cart[-1]
    a__ new_last_item.product == 'chicken'
    a__ new_last_item.price == 6
    a__ not new_last_item.craving


def test_args_mulually_exclusive(parser):
    # argument -l/--list: not allowed with argument -d/--delete
    with pytest.raises(SystemExit):
        parser.parse_args(['-d', 'pizza', '-l'])

    # argument -a/--add: expected 3 arguments
    with pytest.raises(SystemExit):
        parser.parse_args(['-a', 'pizza'])

    # unrecognized arguments: coffee
    with pytest.raises(SystemExit):
        parser.parse_args(['-d', 'pizza', 'coffee'])