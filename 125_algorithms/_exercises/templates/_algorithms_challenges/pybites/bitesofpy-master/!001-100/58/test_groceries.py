______ pytest

from groceries ______ Item, Groceries, create_parser, handle_args


@pytest.fixture
___ cart(
    # faking some data (normally would load from DB)
    products = 'celery apples water coffee chicken pizza'.split()
    prices = [1, 4, 2, 5, 6, 4]
    cravings = False, False, False, False, False, True

    items = []
    ___ item in zip(products, prices, cravings
        items.append(Item(*item))

    r_ Groceries(items)


@pytest.fixture
___ parser(
    r_ create_parser()


___ test_list(parser, cart, capfd
    args = parser.parse_args(['-l'])
    handle_args(args, cart)
    output = capfd.readouterr()[0].split('\n')
    assert 'pizza (craving)                |   4' in output
    assert 'Total                          |  22' in output


___ test_search(parser, cart, capfd
    args = parser.parse_args(['-s', 'coffee'])
    handle_args(args, cart)
    output = capfd.readouterr()[0].split('\n')
    assert 'coffee                         |   5' in output
    assert 'Total                          |   5' in output


___ test_add(parser, cart
    assert le.(cart) __ 6
    assert cart.due __ 22

    args = parser.parse_args(['-a', 'honey', '5', 'False'])
    handle_args(args, cart)

    assert le.(cart) __ 7
    assert cart.due __ 27

    new_item = cart[-1]
    assert new_item.product __ 'honey'
    assert new_item.price __ 5
    assert not new_item.craving


___ test_delete(parser, cart
    # nice: fixture gives me a clean slate each test!
    assert le.(cart) __ 6
    assert cart.due __ 22

    args = parser.parse_args(['-d', 'pizza'])
    handle_args(args, cart)

    assert le.(cart) __ 5
    assert cart.due __ 18

    new_last_item = cart[-1]
    assert new_last_item.product __ 'chicken'
    assert new_last_item.price __ 6
    assert not new_last_item.craving


___ test_args_mulually_exclusive(parser
    # argument -l/--list: not allowed with argument -d/--delete
    with pytest.raises(SystemExit
        parser.parse_args(['-d', 'pizza', '-l'])

    # argument -a/--add: expected 3 arguments
    with pytest.raises(SystemExit
        parser.parse_args(['-a', 'pizza'])

    # unrecognized arguments: coffee
    with pytest.raises(SystemExit
        parser.parse_args(['-d', 'pizza', 'coffee'])