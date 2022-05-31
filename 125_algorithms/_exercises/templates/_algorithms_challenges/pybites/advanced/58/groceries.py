# _______ a__
# ____ c.. _______ n..
#
# Item n..('Item', 'product price craving')
#
#
# c_ Groceries
#
#     ___ -  items_ N..
#         """This cart can be instantiated with a list of namedtuple
#            items, if not provided use an empty list"""
#         _items ? __ ? __ n.. N.. ____    # list
#
#     ___ show  items_ N..
#         """Print a simple table of cart items with total at the end"""
#         items ? __ ? __ n.. N.. ____ ____
#         ___ item __ ?
#             product _* ?.p..
#             __ ?.c..
#                 ? +_ ' (craving)'
#             print _* ?|<30 | ?.p..|>3
#         _? ?
#
#     ___ _print_total  items
#         """Calculate and print total price of cart"""
#         total s.. item.p.. ___ ? __ ?
#         print('-' * 36)
#         print _* "Total":<30 | ?|>3
#
#     ___ add  new_item
#         """Add a new item to cart, exceptions left out for simplicity"""
#         _?.a.. ?
#         s..
#
#     ___ delete  product
#         """Delete item matching 'product', raises IndexError
#            if no item matches"""
#         ___ i item __ e..
#             __ ?.p.. __ p..
#                 _i__.p.. ?
#                 _____
#         ____
#             r.. I.. _* p.. no. __ c..
#         s..
#
#     ___ s..  s..
#         """Filters items matching insensitive 'contains' search, and passes
#            them to show for printing"""
#         items item ___ ? __ ____ __ s...l..
#                  __ ?.p__.l..
#         s.. i..
#
#     $
#     ___ due
#         r.. s.. item.p.. ___ ? __ ____
#
#     ___ -l
#         """The len of cart"""
#         r.. l.. _?
#
#     ___ -g  index
#         """Making the class iterable (cart = Groceries() -> cart[1] etc)
#            without this dunder I would get 'TypeError: 'Cart' object does
#            not support indexing' when trying to index it"""
#         r.. _? ?
#
#
# ___ create_parser
#     """TODO 1
#        Create an ArgumentParser object giving it the required options,
#        note that the options are mutually exclusive.
#        Returns a argparse.ArgumentParser object"""
#
#     ap a__.A..
#     group ?.a..  t.._"Grocery Store",d.._'interface to grocery store'
#     g1 ?.a.. r.._T..
#     ?.a.. "-a","--add",h.._"add item providing name (str), price (int), and craving (bool)" n.._3
#     ?.a.. "-d","--delete",h.._"delete a product by name (str)")
#     ?.a.. "-l","--list",h.._"show items in cart",a.._'store_true')
#     ?.a.. "-s","--search",h.._"search items by name")
#
#     r.. ?
#
#
#
# ___ handle_args args_N.. cart_ N..
#     """TODO 2
#        Receives args and cart and performs the add/delete/list/search
#        operations on cart:
#        - If args not provided create a parser object and retrieve the args
#        - If cart not provided make a Groceries object with 0 or more items
#        Modifies the cart object, no return"""
#     __ ? __ N..
#         parser ?
#         args v.. ?.p..
#
#     __ ? __ N..
#         cart ?
#
#     # different crud operations - please complete ...
#     __ ? 'list'  __ T..
#         ?.s..
#     ____ ? 'add'
#         item price craving args 'add'
#         p.. i.. p..
#         c.. e.. ?
#
#         item ? ? ? ?
#         c__.a.. ?
#     ____ ? 'delete'
#         item ? 'delete'
#         c__.d.. ?
#     ____
#         item ? 'search'
#         c__.s.. ?
#
#
# handle_args()
