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
#         items ? __ ? __ n.. N.. ____ self
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
#         print _* "Total"|<30 | ?|>3
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
#             __ ?.p.. __ ?
#                 _?.p.. ?
#                 _____
#         ____
#             r.. I.. _* ? no. __ c..
#         s..
#
#     ___ s..  s..
#         """Filters items matching insensitive 'contains' search, and passes
#            them to show for printing"""
#         items item ___ ? __ ____ __ s...l..
#                  __ ?.p__.l..
#         s.. ?
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
#     p.. a__.A.. d.._''
#     group p...a..
#     ?.a.. '-a', '--add', n.._3, h.._'add item providing name (str), price (int), and craving (bool)'
#     ?.a.. '-d', '--delete', n.._1, h.._'delete a product by name (str)'
#     ?.a.. '-l', '--list', a.._'store_true', h.._'show items in cart'
#     ?.a.. '-s', '--search', n.._1, h.._'search items by name'
#     r.. p..
#
#
# ___ handle_args args_N.. cart_ N..
#     __ args __ N..
#         parser ?
#         a.. ?.p..
#
#     __ cart __ N..
#         c.. ?
#
#     ___ op, param __ v.. a__.i..
#         __ ? __ 'add' a.. ?
#             c__.a.. ? p.. 0 i.. p.. 1 p.. 2 .l.. __ 'true'
#         ____ ? __ 'delete' a.. p..
#             c__.d.. p.. 0
#         ____ ? __ 'list' a.. ?
#             c__.s..
#         ____ ? __ 'search' a.. ?
#             c__.s.. p.. 0
