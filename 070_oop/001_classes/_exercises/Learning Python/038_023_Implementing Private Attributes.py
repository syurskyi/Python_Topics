# """
# Privacy for attributes fetched from class instances.
# See self-test code at end of file for a usage example.
# Decorator same as: Doubler = Private('data', 'size')(Doubler).
# Private returns onDecorator, onDecorator returns onInstance,
# and each onInstance instance embeds a Doubler instance.
# """
# 
# traceMe _ F..
# 
# 
# ___ trace $
#     i_ t.M. print('[' + ' '.jo.. ma. st., a..)) + ']')
# 
# 
# ___ Private *privates  # privates in enclosing scope
#     ___ onDecorator aClass  # aClass in enclosing scope
#         c_ onInstance  # wrapped in instance attribute
#             ___ - ____ $ $$
#                 ____.wrapped _ aC.. $ $$
# 
#             ___ -g ____ attr  # My attrs don't call getattr
#                 tr.. ('get:', a..  # Others assumed in wrapped
#                 i_ a.. i_ privates
#                     r____ T... 'private attribute fetch: ' + a..
#                 e___
#                     r_ ge... ____.w... a..
# 
#             ___ -s ____ attr value  # Outside accesses
#                 tr.. 'set:', a.. v..  # Others run normally
#                 i_ a.. __ 'wrapped'  # Allow my attrs
#                     ____. -d a..| _ v...  # Avoid looping
#                 e____ a.. i_ privates
#                     r____ T... ('private attribute change: ' + a...
#                 e___
#                     s... ____.w... a... v..  # Wrapped obj attrs
# 
#         r_ o.I.  # Or use __dict__
# 
#     r_ o.D.
# 
# 
# __ ______ __ ______
#     traceMe _ T..
# 
# 
#     _P.. 'data', 'size')  # Doubler = Private(..)(Doubler)
#     c_ Doubler
#         ___ - ____, label, start
#             ____.l... _ l...  # Accesses inside the subject class
#             ____.data _ s...  # Not intercepted: run normally
# 
#         ___ size ____
#             r_ le. ____.da..  # Methods run with no checking
# 
#         ___ double ____  # Because privacy not inherited
#             ___ i i_ ra.. ____.s..
#                 ____.da.. i _ ____.da.. i * 2
# 
#         ___ display ____
#             print('@ => @' @ ____.la.. ____.da..
# 
# 
#     X = D... ('X is', [1, 2, 3])
#     Y = D... ('Y is', [-10, -20, -30])
# 
#     # The followng all succeed
#     print(X.label)  # Accesses outside subject class
#     X.display();
#     X.double();
#     X.display()  # Intercepted: validated, delegated
#     print(Y.label)
#     Y.display();
#     Y.double()
#     Y.label = 'Spam'
#     Y.display()
# 
#     # The following all fail properly
#     """
#     print(X.size())          # prints "TypeError: private attribute fetch: size"
#     print(X.data)
#     X.data = [1, 1, 1]
#     X.size = lambda S: 0
#     print(Y.data)
#     print(Y.size())
#     """
