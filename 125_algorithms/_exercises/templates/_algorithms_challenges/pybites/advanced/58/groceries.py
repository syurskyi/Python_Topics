import argparse
from collections import namedtuple

Item = namedtuple('Item', 'product price craving')


class Groceries:

    ___ __init__(self, items_ N..
        """This cart can be instantiated with a list of namedtuple
           items, if not provided use an empty list"""
        self._items = items __ items is not None else []

    ___ show(self, items_ N..
        """Print a simple table of cart items with total at the end"""
        items = items __ items is not None else self
        for item in items:
            product = f'{item.product}'
            __ item.craving:
                product += ' (craving)'
            print(f'{product:<30} | {item.price:>3}')
        self._print_total(items)

    ___ _print_total(self, items):
        """Calculate and print total price of cart"""
        total = sum(item.price for item in items)
        print('-' * 36)
        print(f'{"Total":<30} | {total:>3}')

    ___ add(self, new_item):
        """Add a new item to cart, exceptions left out for simplicity"""
        self._items.append(new_item)
        self.show()

    ___ delete(self, product):
        """Delete item matching 'product', raises IndexError
           if no item matches"""
        for i, item in enumerate(self):
            __ item.product == product:
                self._items.pop(i)
                break
        else:
            raise IndexError(f'{product} not in cart')
        self.show()

    ___ search(self, search):
        """Filters items matching insensitive 'contains' search, and passes
           them to show for printing"""
        items = [item for item in self __ search.lower()
                 in item.product.lower()]
        self.show(items)

    @property
    ___ due(self):
        return sum(item.price for item in self)

    ___ __len__(self):
        """The len of cart"""
        return len(self._items)

    ___ __getitem__(self, index):
        """Making the class iterable (cart = Groceries() -> cart[1] etc)
           without this dunder I would get 'TypeError: 'Cart' object does
           not support indexing' when trying to index it"""
        return self._items[index]


___ create_parser():
    """TODO 1
       Create an ArgumentParser object giving it the required options,
       note that the options are mutually exclusive. 
       Returns a argparse.ArgumentParser object"""

    ap = argparse.ArgumentParser()
    group = ap.add_argument_group(title="Grocery Store",description='interface to grocery store')
    g1 = group.add_mutually_exclusive_group(required=True)
    g1.add_argument("-a","--add",help="add item providing name (str), price (int), and craving (bool)",nargs=3)
    g1.add_argument("-d","--delete",help="delete a product by name (str)")
    g1.add_argument("-l","--list",help="show items in cart",action='store_true')
    g1.add_argument("-s","--search",help="search items by name")

    return ap



___ handle_args(args=None, cart_ N..
    """TODO 2
       Receives args and cart and performs the add/delete/list/search
       operations on cart:
       - If args not provided create a parser object and retrieve the args
       - If cart not provided make a Groceries object with 0 or more items
       Modifies the cart object, no return"""
    __ args is None:
        parser = create_parser()
        args = vars(parser.parse_args())

    __ cart is None:
        cart = Groceries()

    # different crud operations - please complete ...
    __ args['list'] == True:
        cart.show()
    elif args['add']:
        item,price,craving = args['add']
        price = int(price)
        craving = eval(craving)

        item = Item(item,price,craving)
        cart.add(item)
    elif args['delete']:
        item = args['delete']
        cart.delete(item)
    else:
        item = args['search']
        cart.search(item)





        






handle_args()
