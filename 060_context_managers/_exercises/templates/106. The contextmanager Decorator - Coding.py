# # Using Decorators to Create Context Managers using Generator Functions
# # In the last video we saw how we could create a generic class that could take a generator function that
# # had a specific structure and turn it into a context manager.
# # Let's see if we can do one step better, using a decorator instead.
# # Recall the basic structure our generator function needs to have:
# # def gen(args):
# #     # set up happens here, or inside try
# #     try:
# #         yield obj # whatever normally gets returned by __enter__
# #     finally:
# #         # perform clean up code here
# # First let's define a generator function to open a file, yield it, and then close it - same as the example we saw
# # in the previous video:
#
#
# print('#' * 52 + '  ### Using Decorators to Create Context Managers using Generator Functions')
#
#
# ___ open_file fname m.._'_'
#     print('opening file...')
#     f _ o.. f.. m..
#     t__
#         y___ f
#     f_____
#         print('closing file...')
#         f.c..
#
# # Next, let's re-create the context manager wrapper we did in the last video, but this time, I'm going to pass it a
# # generator object, instead of a generator function. But basically the same idea:
#
#
# c_ GenContextManager
#     ___ __i__ ____ gen
#         ____.g.. _ g..
#
#     ___ __e__ ____
#         r__ n.. ____.g..
#
#     ___ __e__ ____ exc_type, exc_value exc_tb
#         print('calling next to perform cleanup in generator')
#         t__
#             n.. ____.g..
#         e_____ S..I.
#             p___
#         r_ F..
#
# # At this point we can use this with our generator function as follows:
#
# file_gen _ open_file test.txt' '_'
#
# w_ G.... f.. a_ f
#     f.w.l. Sir Spamalot
# # opening file...
# # calling next to perform cleanup in generator
# # closing file...
# # ######################################################################################################################
#
# # And we can read back from the file too:
# print('#' * 52 + '  And we can read back from the file too:')
#
# file_gen _ open_file test.txt
# w_ C.. f.. a_ f
#     print f.r.l.
# # opening file...
# # ['Sir Spamalot']
# # calling next to perform cleanup in generator
# # closing file...
# # ######################################################################################################################
#
# # Of course, our context manager object is not very robust - there is no exception handling for example.
# # But let's leave that "minor detail" aside for now :-)
# # We still have to create the generator object from the generator function before we can use the context manager class.
# # We can simplify things even more by using a decorator:
#
# print('#' * 52 + '  We still have to create the generator object from the generator function before'
#                  '  we can use the context manager class.')
# print('#' * 52 + '  We can simplify things even more by using a decorator:')
#
#
# ___ context_manager_dec gen_fn
#     ___ helper 0a.. 00k..
#         gen _ g._f. 0a.. 00k..
#         ctx _ G... g..
#         r_ c..
#     r_ h...
#
# # Notice what this decorator does.
# # It decorates a generator function and returns helper. When we invoke helper it will create an instance
# # of the generator, and create and return an instance of the context manager.
# # Let's try it out:
#
#
# 0c_____
# ___ open_file fnamw m.._'_':
#     print('opening file...')
#     f _ o... f... m..
#     t__
#         y__ ?
#     f____
#         print('closing file...')
#         ?.cl..
#
#
# w.. o.._f.. test.txt a_ f
#     print ?.r..l..
# # opening file...
# # ['Sir Spamalot']
# # calling next to perform cleanup in generator
# # closing file...
# # ######################################################################################################################
#
#
# # So now we have an approach to using a decorator to turn any generator function (that has the structure we mentioned
# # earlier) into a context manager!
# # Our code was not very robust, either in the context manager class or in the decorator - and it would take quite
# # a bit more work to make it so.
# # Fortunately the standard library has already though of this - in fact that was one of the critical goals of Python's
# # context managers - the ability to create context managers using generator functions (see PEP 343).
#
# print('#' * 52 + '  So now we have an approach to using a decorator to turn any generator function'
#                  '  (that has the structure we mentioned earlier) into a context manager!')
#
# f____ c..l.. ________ c..m..
#
#
# 0c..m..
# ___ open_file fname m.._'_'
#     print('opening file...')
#     f _ o.. f.. m..
#     t__
#         y__ ?
#     f___
#         print('closing file...')
#         ?.c..
#
# w___ o... test.txt a_ f
#     print ?.r..l..
# # opening file...
# # ['Sir Spamalot']
# # closing file...
# # ######################################################################################################################
#
#
# # And of course, this works for more than just opening and closing files.
# # Here are some more examples:
# # Example 1
# # Let's implement a timer
#
# print('#' * 52 + '  Lets implement a timer.')
#
# f__ ti.. _______ pe.._co.. sl..
#
#
# @c...m..
# ___ timer:
#     stats _ di..
#     start _ pe.._co..
#     s... 'start' _ start
#     t__
#         y___ s..
#     f___
#         end _ p.._co..
#         s.. 'end' _ e..
#         s.. 'elapsed' _ e.. - s..
#
#
# w___ t.. a_ stats:
#     sl.. 1
#
# print s..
# # {'start': 5.417897319468211e-07, 'end': 1.005228270913287, 'elapsed': 1.005227729123555}
# # ######################################################################################################################
#
# # Example 2
# # In this example, let's redirect stdout.
#
# print('#' * 52 + '  In this example, lets redirect `stdout`.')
#
# ________ sy.
#
#
# 0c..m..
# ___ out_to_file fname
#     current_stdout _ sy_.s..o..
#     file _ o.. f... '_'
#     sy_.s..o.. _ f...
#     t__
#         y____ N...
#     f___
#         ?.cl..
#         sy_.s..do.. _ c...
#
#
# w___ out_to_file test.txt
#     print('line 1')
#     print('line 2')
#
# w___ o... test.txt a_ f
#     print ?.r..l..
# # ['line 1\n', 'line 2\n']
# # ######################################################################################################################
#
# # And of course, stdout is back to "normal":
# print('#' * 52 + '  And of course, `stdout` is back to "normal":')
#
# print('line 1')
# # line 1
# # ######################################################################################################################
#
#
# # The contextlib module actually implements a stdout redirect context manager, so we technically don't
# # have to write one ourselves.
# # The difference from thge one we wrote is that it needs an open file object, not just a file name.
# # So we would have to open the file, then redirect stdout. We can do this easily by nesting two context managers
# # as follows:
#
# print('#' * 52 + '  The `contextlib` module actually implements a `stdout` redirect context manager,'
#                  '  so we technically dont have to write one ourselves.')
#
# f__ c..l.. ______ r..._s..o..
#
# w___ o.. 'test.txt' '_' a_ f
#     w___ r.._s..o. f
#         print('Look on the bright side of life')
#
# # And we can check that this worked:
#
# with o... test.txt a_ f
#     print ?.r..l..
# # ['Look on the bright side of life\n']
# # ######################################################################################################################
