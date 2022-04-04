_______ a__
____ c.. _______ n..

Item = n..('Item', 'product price craving')


c_ Groceries:

    ___ - , items_ N..
        """This cart can be instantiated with a list of namedtuple
           items, if not provided use an empty list"""
        _items = items __ items __ n.. N.. ____ []

    ___ show  items_ N..
        """Print a simple table of cart items with total at the end"""
        items = items __ items __ n.. N.. ____ self
        ___ item __ items:
            product = f'{item.product}'
            __ item.craving:
                product += ' (craving)'
            print _*{product:<30} | {item.price:>3}')
        _print_total(items)

    ___ _print_total  items
        """Calculate and print total price of cart"""
        total = s..(item.price ___ item __ items)
        print('-' * 36)
        print _*{"Total":<30} | {total:>3}')

    ___ add  new_item
        """Add a new item to cart, exceptions left out for simplicity"""
        _items.a..(new_item)
        show()

    ___ delete  product
        """Delete item matching 'product', raises IndexError
           if no item matches"""
        ___ i, item __ e..
            __ item.product __ product:
                _items.pop(i)
                _____
        ____:
            r.. IndexError _*{product} not in cart')
        show()

    ___ s..  s..
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

    ___ __getitem__  index
        """Making the class iterable (cart = Groceries() -> cart[1] etc)
           without this dunder I would get 'TypeError: 'Cart' object does
           not support indexing' when trying to index it"""
        r.. _items[index]


___ create_parser
    p.. = a__.A..(d.._'')
    group = p...add_mutually_exclusive_group()
    group.a..('-a', '--add', nargs=3, h.._'add item providing name (str), price (int), and craving (bool)')
    group.a..('-d', '--delete', nargs=1, h.._'delete a product by name (str)')
    group.a..('-l', '--list', a.._'store_true', h.._'show items in cart')
    group.a..('-s', '--search', nargs=1, h.._'search items by name')
    r.. p..


___ handle_args(args=N.., cart_ N..
    __ args __ N..
        parser = create_parser()
        args = parser.p..

    __ cart __ N..
        cart = Groceries()

    ___ op, param __ vars(args).i..:
        __ op __ 'add' a.. param:
            cart.add(Item(param[0], i..(param[1]), param[2].l.. __ 'true'
        ____ op __ 'delete' a.. param:
            cart.delete(param[0])
        ____ op __ 'list' a.. param:
            cart.show()
        ____ op __ 'search' a.. param:
            cart.s..(param[0])
