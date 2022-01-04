_______ argparse
____ collections _______ n..

Item = n..('Item', 'product price craving')


c_ Groceries:

    ___ - , items_ N..
        """This cart can be instantiated with a list of namedtuple
           items, if not provided use an empty list"""
        _items = items __ items __ n.. N.. ____ []

    ___ show(self, items_ N..
        """Print a simple table of cart items with total at the end"""
        items = items __ items __ n.. N.. ____ self
        ___ item __ items:
            product = f'{item.product}'
            __ item.craving:
                product += ' (craving)'
            print(f'{product:<30} | {item.price:>3}')
        _print_total(items)

    ___ _print_total(self, items):
        """Calculate and print total price of cart"""
        total = s..(item.price ___ item __ items)
        print('-' * 36)
        print(f'{"Total":<30} | {total:>3}')

    ___ add(self, new_item):
        """Add a new item to cart, exceptions left out for simplicity"""
        _items.a..(new_item)
        show()

    ___ delete(self, product):
        """Delete item matching 'product', raises IndexError
           if no item matches"""
        ___ i, item __ e..
            __ item.product __ product:
                _items.pop(i)
                break
        ____:
            r.. IndexError(f'{product} not in cart')
        show()

    ___ s..(self, s..):
        """Filters items matching insensitive 'contains' search, and passes
           them to show for printing"""
        items = [item ___ item __ self __ s...l..
                 __ item.product.l..]
        show(items)

    $
    ___ due
        r.. s..(item.price ___ item __ self)

    ___ __len__
        """The len of cart"""
        r.. l..(_items)

    ___ __getitem__(self, index):
        """Making the class iterable (cart = Groceries() -> cart[1] etc)
           without this dunder I would get 'TypeError: 'Cart' object does
           not support indexing' when trying to index it"""
        r.. _items[index]


___ create_parser
    parse = argparse.ArgumentParser(description='')
    group = parse.add_mutually_exclusive_group()
    group.add_argument('-a', '--add', nargs=3, help='add item providing name (str), price (int), and craving (bool)')
    group.add_argument('-d', '--delete', nargs=1, help='delete a product by name (str)')
    group.add_argument('-l', '--list', action='store_true', help='show items in cart')
    group.add_argument('-s', '--search', nargs=1, help='search items by name')
    r.. parse


___ handle_args(args=N.., cart_ N..
    __ args __ N..
        parser = create_parser()
        args = parser.parse_args()

    __ cart __ N..
        cart = Groceries()

    ___ op, param __ vars(args).i..:
        __ op __ 'add' a.. param:
            cart.add(Item(param[0], i..(param[1]), param[2].l.. __ 'true'))
        ____ op __ 'delete' a.. param:
            cart.delete(param[0])
        ____ op __ 'list' a.. param:
            cart.show()
        ____ op __ 'search' a.. param:
            cart.s..(param[0])
