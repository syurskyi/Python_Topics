______ argparse
from collections ______ namedtuple

Item = namedtuple('Item', 'product price craving')


class Groceries:

    ___ __init__(self, items=None
        """This cart can be instantiated with a list of namedtuple
           items, if not provided use an empty list"""
        self._items = items __ items is not None else []

    ___ show(self, items=None
        """Print a simple table of cart items with total at the end"""
        items = items __ items is not None else self
        for item in items:
            product = f'{item.product}'
            __ item.craving:
                product += ' (craving)'
            print(f'{product:<30} | {item.price:>3}')
        self._print_total(items)

    ___ _print_total(self, items
        """Calculate and print total price of cart"""
        total = sum(item.price for item in items)
        print('-' * 36)
        print(f'{"Total":<30} | {total:>3}')

    ___ add(self, new_item
        """Add a new item to cart, exceptions left out for simplicity"""
        self._items.append(new_item)
        self.show()

    ___ delete(self, product
        """Delete item matching 'product', raises IndexError
           if no item matches"""
        for i, item in enumerate(self
            __ item.product __ product:
                self._items.pop(i)
                break
        ____
            raise IndexError(f'{product} not in cart')
        self.show()

    ___ search(self, search
        """Filters items matching insensitive 'contains' search, and passes
           them to show for printing"""
        items = [item for item in self __ search.lower()
                 in item.product.lower()]
        self.show(items)

    @property
    ___ due(self
        r_ sum(item.price for item in self)

    ___ __len__(self
        """The le. of cart"""
        r_ le.(self._items)

    ___ __getitem__(self, index
        """Making the class iterable (cart = Groceries() -> cart[1] etc)
           without this dunder I would get 'TypeError: 'Cart' object does
           not support indexing' when trying to index it"""
        r_ self._items[index]


___ create_parser(
    parse = argparse.ArgumentParser(description='')
    group = parse.add_mutually_exclusive_group()
    group.add_argument('-a', '--add', nargs=3, help='add item providing name (str), price (int), and craving (bool)')
    group.add_argument('-d', '--delete', nargs=1, help='delete a product by name (str)')
    group.add_argument('-l', '--list', action='store_true', help='show items in cart')
    group.add_argument('-s', '--search', nargs=1, help='search items by name')
    r_ parse


___ handle_args(args=None, cart=None
    __ args is None:
        parser = create_parser()
        args = parser.parse_args()

    __ cart is None:
        cart = Groceries()

    for op, param in vars(args).items(
        __ op __ 'add' and param:
            cart.add(Item(param[0], int(param[1]), param[2].lower() __ 'true'))
        ____ op __ 'delete' and param:
            cart.delete(param[0])
        ____ op __ 'list' and param:
            cart.show()
        ____ op __ 'search' and param:
            cart.search(param[0])
