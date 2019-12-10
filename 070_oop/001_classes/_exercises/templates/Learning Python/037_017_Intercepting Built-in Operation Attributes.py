# ### file: getattr.py
#
# c_ GetAttr
#     eggs _ 88  # eggs stored on class, spam on instance
#
#     ___  - ____
#         ____.spam _ 77
#
#     ___ -l  ____  # len here, else __getattr__ called with __len__
#         print('__len__: 42')
#         r_ 42
#
#     ___ -g ____ attr  # Provide __str__ if asked, else dummy func
#         print('getattr: ' + a...
#         i_ attr __ '__str__'
#             r_ l____ $ '[Getattr str]'
#         e____
#             r_ l____ $ N..
#
#
# c_ GetAttribute o...  # object required in 2.6, implied in 3.0
#     eggs _ 88  # In 2.6 all are isinstance(object) auto
#
#     ___ - ____  # But must derive to get new-style tools,
#         ____.spam _ 77  # incl __getattribute__, some __X__ defaults
#
#     ___ -l ____
#         print('__len__: 42')
#         r_ 42
#
#     ___ -g ____ attr
#         print('getattribute: ' + a..
#         i_ a.. __ '__str__'
#             r_ l____ $ '[GetAttribute str]'
#         e___
#             r_ l____ $ N..
#
#
# ___ c_ i_ GetAttr, GetAttribute:
#     print('\n' + C___. -n.lj... (50, '_'
#
#     X _ C...
#     ?.eggs  # Class attr
#     ?.spam  # Instance attr
#     ?.other  # Missing attr
#     len(X)  # __len__ defined explicitly
#
#     t__  # New-styles must support [], +, call directly: redefine
#         X[0]  # __getitem__?
#     e____
#         print('fail []')
#
#     t__
#         X + 99  # __add__?
#     e____
#         print('fail +')
#
#     t__
#         ?  # __call__?  (implicit via built-in)
#     e____
#         print('fail ()')
#     ?. -c  # __call__?  (explicit, not inherited)
#
#     print(?. -s)  # __str__?   (explicit, inherited from type)
#     print(X)  # __str__?   (implicit via built-in)
#
#
