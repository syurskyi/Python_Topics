_______ p__

____ groceries _______ Item, Groceries, create_parser, handle_args


?p__.f..
___ cart
    # faking some data (normally would load from DB)
    products 'celery apples water coffee chicken pizza'.s..
    prices [1, 4, 2, 5, 6, 4]
    cravings F.., F.., F.., F.., F.., T..

    items    # list
    ___ item __ z..(products, prices, cravings
        items.a..(Item(*item

    r.. Groceries(items)


?p__.f..
___ parser
    r.. ?


___ test_list(parser, cart, capfd
    args parser..p..  '-l' )
    handle_args(args, cart)
    output ?.r .. 0 .s..('\n')
    ... 'pizza (craving)                |   4' __ output
    ... 'Total                          |  22' __ output


___ test_search(parser, cart, capfd
    args parser..p..  '-s', 'coffee' )
    handle_args(args, cart)
    output ?.r .. 0 .s..('\n')
    ... 'coffee                         |   5' __ output
    ... 'Total                          |   5' __ output


___ test_add(parser, cart
    ... l..(cart) __ 6
    ... cart.due __ 22

    args parser..p..  '-a', 'honey', '5', 'False' )
    handle_args(args, cart)

    ... l..(cart) __ 7
    ... cart.due __ 27

    new_item cart[-1]
    ... new_item.product __ 'honey'
    ... new_item.price __ 5
    ... n.. new_item.craving


___ test_delete(parser, cart
    # nice: fixture gives me a clean slate each test!
    ... l..(cart) __ 6
    ... cart.due __ 22

    args parser..p..  '-d', 'pizza' )
    handle_args(args, cart)

    ... l..(cart) __ 5
    ... cart.due __ 18

    new_last_item cart[-1]
    ... new_last_item.product __ 'chicken'
    ... new_last_item.price __ 6
    ... n.. new_last_item.craving


___ test_args_mulually_exclusive(parser
    # argument -l/--list: not allowed with argument -d/--delete
    w__ p__.r..(S..
        parser..p..  '-d', 'pizza', '-l' )

    # argument -a/--add: expected 3 arguments
    w__ p__.r..(S..
        parser..p..  '-a', 'pizza' )

    # unrecognized arguments: coffee
    w__ p__.r..(S..
        parser..p..  '-d', 'pizza', 'coffee' )