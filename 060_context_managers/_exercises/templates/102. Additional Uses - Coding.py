# print('#' * 52 + '  ### Additional Uses')
# # Additional Uses
# # Remember what I said in the last lecture about some common patterns we can implement with context managers:
# #     Open - Close
# #     Change - Reset
# #     Start - Stop
# # The open file context manager is an example of the Open - Close pattern. But we have other ones as well.
# # Decimal Contexts
# # Decimals have a context which can be used to define many things, such as precision, rounding mechanism, etc.
# # By default, Decimals have a "global" context - i.e. one that will apply to any Decimal object by default:
#
# ______ dec..
#
# print(d___.g..t..
# # Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[],
# # traps=[InvalidOperation, DivisionByZero, Overflow])
# # ######################################################################################################################
#
# # If we create a decimal object, then it will use those settings.
# # We can certainly change the properties of that global context:
# print('#' * 52 + '  If we create a decimal object, then it will use those settings.')
# print('#' * 52 + '  We can certainly change the properties of that global context:')
#
# d___.g__c__.pr.._14
# print(d___.g__c__
# # Context(prec=14, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[],
# # traps=[InvalidOperation, DivisionByZero, Overflow])
# # ######################################################################################################################
#
# # And now the default (global) context has a precision set to 14.
# # Let's reset it back to 28:
# print('#' * 52 + '  And now the default (global) context has a precision set to 14.')
# print('#' * 52 + '  Lets reset it back to 28:')
#
# decimal.g..c__.pr.. _ 28
#
# # Suppose now that we just want to temporarily change something in the context - we would have to do something like
# # this:
#
# old_prec _ d___.g__c__ .pr..
# d___.g__c__ .pr.. _ 4
# print(d___.D_ 1 / d___.D_ 3
# d___.g__c__ .pr.. _ old_prec
# print(d___.D_ 1 / d___.D_ 3
# # 0.3333
# # 0.3333333333333333333333333333
# # ######################################################################################################################
#
# # Of course, this is kind of a pain to have to store the current value, set it to something new, and then remember
# # to set it back to it's original value.
# # How about writing a context manager to do that seamlessly for us:
# print('#' * 52 + '  Of course, this is kind of a pain to have to store the current value, set it to something new,'
#                  '  and then remember to set it back to its original value.')
# print('#' * 52 + '  How about writing a context manager to do that seamlessly for us:')
#
#
# c_ precision:
#     ___ __i__ ____  prec
#         ____.pr.. _ p...
#         ____.current_prec _ d___.g..c.. .pr..
#
#     ___ __e__ ____
#         d___.g..c.. pr.. _ ____.pr..
#
#     ___ __e__ ____ exc_type exc_value exc_traceback
#         d___.g..c..().pr.. _ ____.current_prec
#         r_ F..
#
#
# w___ p.... 3
#     print d___.D_ 1 / d___.D_ 3
# print(d___.D_ 1 / d___.D_ 3
# # 0.333
# # 0.3333333333333333333333333333
# # ######################################################################################################################
#
# # And as you can see, the precision was set back to it's original value once the context was exited.
# # In fact, the decimal class already has a context manager, and it's way better than ours, because we can set not only
# # the precision, but anything else we want:
# print('#' * 52 + '  And as you can see, the precision was set back to its original value once the context was exited.')
# print('#' * 52 + '  In fact, the decimal class already has a context manager, and its way better than ours,'
#                  '  because we can set not only the precision, but anything else we want:')
#
# w___ d___.l..c.. a_ ctx
#     ct_.pr.. _ 3
#     print d___.D_ 1 / d___.D_ 3
# print d___.D_ 1 / d___.D_ 3
# # 0.333
# # 0.3333333333333333333333333333
# # ######################################################################################################################
#
# # Timing a with block
# #
# # Here's another example of a Start - Stop type of context manager. We'll create a context manager to time the code
# # inside the with block:
# print('#' * 52 + '  #### Timing a with block')
# print('#' * 52 + '  Here is another example of a **Start - Stop** type of context manager.')
# print('#' * 52 + '  We will create a context manager to time the code inside the `with` block:')
#
# f_ ti__ _______ pe.._co.. sl..
#
#
# c_ Timer
#     ___ __i__ ____
#         ____.elapsed _ 0
#
#     ___ __e__ ____
#         ____.start _ pe.._co..
#         r_ ____
#
#     ___ __e__ ____ exc_type exc_value exc_traceback
#         ____.stop _ pe.._co..
#         ____.elapsed = ____.stop - ____.start
#         r_ F..
#
# # You'll note that this time we are returning the context manager itself from the __enter__ statement.
# # This will allow us to look at the elapsed property of the context manager once the with statement
# # has finished running.
#
#
# w___ T.. a_ timer
#     sl.. 1)
# print ti__.el..
# # 0.9993739623039163
# # ######################################################################################################################
#
# # Redirecting stdout
# # Here we are going to temporarily redirect stdout to a file instead fo the console:
# print('#' * 52 + '  #### Redirecting stdout')
# print('#' * 52 + '  Here we are going to temporarily redirect `stdout` to a file instead fo the console:')
#
# _______ s..
#
#
# c_ OutToFile
#     ___ __i__ ____ fname
#         ____._f.. _ f..
#         ____._current_stdout = s__.s.o.
#
#     ___ __e__ ____
#         ____._file _ o.. ____._f... '_'
#         s__.s.o. _ ____._f..
#
#     ___ __e__ ____ exc_type exc_value exc_tb
#         s__.s.o. _ ____._cu...
#         i_ ____._f..
#             ____._f__.cl..
#         r___ F..
#
#
# w___ O.... test.txt
#     print('Line 1')
#     print('Line 2')
#
# # As you can see, no output happened on the console... Instead the output went to the file we specified.
# # And our print statements will now output to the console again:
#
# print('back to console output')
#
# # back to console output
#
# w___ o.. test.txt a_ f
#     print f.r..l..
#
#
# # HTML Tags
# # In this example, we're going to basically use a context manager to inject opening and closing html tags as
# # we print to the console (of course we could redirect our prints somewhere else as we just saw!):
# print('#' * 52 + '  #### HTML Tags')
#
#
# c_ Tag
#     ___ __i__ ____ tag)
#         ____._t.. _ t..
#
#     ___ __e__ ____
#         print _'<|____._t..|> e.._''
#
#     ___ __e__ ____ exc_type exc_value exc_tb
#         print(_'</|____._t..|> e.._''
#         r_ F..
#
# w___ T.. 'p'
#     print 'some ' e.._''
#     w___ T.. 'b'
#         print 'bold' e.._''
#     print ' text' e.._''
#
# # <p>some <b>bold</b> text</p>
# # ######################################################################################################################
#
# # Re-entrant Context Managers
# # We can also write context managers that can be re-entered in the sense that we can call __enter__ and __exit__
# # more than once on the same context manager.
# # These methods are called when a with statement is used, so we'll need to be able to get our hands on the context
# # manager object itself - but that's easy, we just return ____ from the __enter__ method.
# # Let's write a ListMaker context manager to do see how this works.
# print('#' * 52 + '  #### Re-entrant Context Managers')
# print('#' * 52 + '  Let is write a ListMaker context manager to do see how this works.')
#
#
# c_ ListMaker
#     ___ __i__ ____ title prefix_'- ' indent_3
#         ____._t... _ t..
#         ____._p... _ p...
#         ____._i.. _ i..
#         ____._current_indent _ 0
#         print t..
#
#     ___ __e__ ____
#         ____._current_indent += ____._indent
#         r_ ____
#
#     ___ __e__ ____ exc_type exc_value exc_tb
#         ____._current_indent -_ ____._i..
#         r_ F..
#
#     ___ print ____ a..
#         s _ ' ' * ____._c.._i.. + ____._pr.. + st. ar.
#         print(s)
#
# # Because __enter__ is returning ____, the instance of the context manager, we can call with on that context manager
# # and it will automatically call the __enter__ and __exit__ methods. Each time we run __enter__ we increase
# # the indentation, each time we run __exit__ we decrease the indentation.
# # Our print method then takes that into account when it prints the requested string argument.
#
#
# print('#' * 52 + '  Our `print` method then takes that into account when it prints the requested string argument.')
#
# w___ L.. 'Items' a_ lm
#     __.print Item 1
#     w___ __
#         __.print item 1a
#         __.print item 1b
#     __.printItem 2
#     w___ __
#         __.printitem 2a
#         __.print item 2b
# # Items
# #    - Item 1
# #       - item 1a
# #       - item 1b
# #    - Item 2
# #       - item 2a
# #       - item 2b
# # ######################################################################################################################
#
# # Of course, we can easily redirect the output to a file instead, using the context manager we wrote earlier:
# print('#' * 52 + '  Of course, we can easily redirect the output to a file instead,'
#                  '  using the context manager we wrote earlier:')
#
# w___ O... my_list.txt
#     w___ L..('Items') a_ lm
#         __.print Item 1
#         w___ __
#             __.print item 1a
#             __.print item 1b
#         __.print Item 2
#         w___ __
#             __.print item 2a
#             __.print item 2b
#
# w___ o... my_list.txt a_ f
#     ___ row i_ f
#         print r.. e.._''
# # Items
# #    - Item 1
# #       - item 1a
# #       - item 1b
# #    - Item 2
# #       - item 2a
# #       - item 2b
# # ######################################################################################################################
