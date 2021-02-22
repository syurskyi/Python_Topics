#
# # Sending Exceptions to Generators
# # In fact we can also raise any E.... inside a generator by using the throw   method
#
# ___ gen
#     t__
#         w___ T..
#             received _ y___
#             print ?
#     f.....
#         print 'E.... must have happened...'
#
# g _ ?
# ne.. ?
# ?.s.. 'hello' g.throw ValueError, 'custom message'
#
# # Sending Exceptions to Generators
# # a_ you can see, the E.... occurred inside the generator, and then propagated up to the caller
# #  we did not intercept and silence the E.... . Of course we can do that if we want to:
#
# ___ gen
#     t__
#         w___ T..
#             received _ y___
#             print ?
#     e.... V...E..
#         print 'received the value error...'
#     f....
#         print 'generator exiting and closing'
#
# g _ ?
# ne.. ?
# ?.send 'hello'
# ?.throw V...E... 'stop it!'
#
# # Sending Exceptions to Generators
# #
# # if the generator catches the E.... and yields a value, that is the return value of the throw   method
# #
# # And the generator is now in a suspended state, waiting for our next call:
#
# f_ ins___ _______ g..g..s__
#
# ___ gen
#     w___ T..
#         t__
#             received _ y___
#             print ?
#         e.... V..E.. __ ex
#             print 'ValueError received...' ?
#
# g _ ?
# ne.. ?
# ?.s.. *hello
# ?.t.. V..E.. 'custom message'
# ?.s.. *hello
# ?..g..s__ g
#
#
# # Sending Exceptions to Generators
# #
# # if the generator does not catch the E...., the E.... is propagated back to the caller
# #
# # And the generator is now in a closed state:
#
# ___ gen
#     w___ T..
#         received _ y___
#         print ?
#
# g _ ?
# ne.. ?
# ?.s.. 'hello'
#
#
# # Sending Exceptions to Generators
# #
# # if the generator catches the E...., and exits  returns , the StopIteration E.... is propagated to the caller
#
# ___ gen
#     t__
#         w___ T..
#             received _ y___
#             print ?
#     e.... V...E.. __ ex
#         print 'ValueError received' ?
#         r_ N...
#
# g _ ?
# ne.. ?
# ?.s.. 'hello'
#
# g.th.. V...E.. 'custom message'
#
# # Sending Exceptions to Generators
# #
# # if the generator catches the E...., and raises another E...., that E.... is propagated to the caller
# #
# # And out generator is, once again, in a closed state:
#
# ___ gen
#     t__
#         w___ T..
#             received _ y___
#             print ?
#     e.... V..E.. __ ex
#         print 'ValueError received...' ?
#         r... Z..D..E.. 'not really...'
#
# g _ gen
# ne.. g
# g.send 'hello'
#
# g.th.. V..E.. 'custom message'
#
# g..g..s__ g
#
# # Sending Exceptions to Generators
# #
# # __ you can see our traceback includes both the ZeroDivisionError and the ValueError that caused the ZeroDivisionError
# # to happen in the first place. If you don't want to have that traceback you can easily remove it and only display
# # the ZeroDivisionError  I will cover this and exceptions in detail in a later part of this series :
#
# ___ gen
#     t__
#         w___ T..
#             received _ y___
#             print r....
#     e.... V..E.. __ ex
#         print 'ValueError received...' ?
#         r... Z..D..E... 'not really...'  fr.. N...
#
# g _ ?
# ne.. ?
# ?.s.. 'hello'
#
# ?.th.. V...E.. 'custom message'
#
# # Sending Exceptions to Generators
# #
# # Suppose we have a coroutine that handles writing data to a database. We have seen in some previous examples where
# # we could use a coroutine to start and either commit or abort a transaction - based on closing the generator or
# # forcing an E.... to happen in the body of the generator.
# #
# # Let's revisit this example, but now we'll want to use exceptions to indicate to our generator whether to commit or
# # abort a transaction, without necessarily exiting the generator:
#
# c_ CommitException E....
#     p_
#
# c_ RollbackException E....
#     p_
#
# ___ write_to_db
#     print 'opening database connection...'
#     print 'start transaction...'
#     t__
#         w___ T..
#             t__
#                 data _ y___
#                 print 'writing data to database...' ?
#             e.... C...E...
#                 print 'committing transaction...'
#                 print 'opening next transaction...'
#             e.... R...Ex..
#                 print 'aborting transaction...'
#                 print 'opening next transaction...'
#     f.....
#         print 'generator closing...'
#         print 'aborting transaction...'
#         print 'closing database connection...'
#
# sql _ write_to_db
# ne.. ?
# ?.se.. 100
# ?.th.. C..E..
# ?.se.. 200
# ?.th.. R..E..
# ?.se.. 200
# ?.th.. C..E..
# ?.cl..
#
# # Sending Exceptions to Generators
# #
# # throw   and close
# #
# # The close   method does essentially the same thing a_ throw GeneratorExit  e.... that when that E.... is thrown
# # using throw  , Python does not silence the E.... for the caller:
#
# ___ gen
#     t__
#         w___ T..
#             received _ y___
#             print ?
#     f..
#         print 'closing down...'
#
# g _ ?
# ne.. ?
# ?.se.. 'hello'
# ?.cl..
#
# g _ ?
# ne.. ?
# ?.se.. 'hello'
# ?.th.. G..E
#
# # Sending Exceptions to Generators
# # throw   and close
# # Even if we catch the E...., we are still exiting the generator, so using throw will result in the caller
# # receiving a StopIteration E.....
# #
# # So, we can use throw to close the generator, but a_ the caller we now have to handle the E.... that
# # propagates up to us:
#
# ___ gen
#     t__
#         w___ T..
#             received _ y___
#             print ?
#     e... G.E..
#         print 'received generator exit...'
#     f...
#         print 'closing down...'
#
# g _ ?
# ne.. ?
# ?.cl..
#
# g _ ?
# ne.. ?
# ?.th.. G...E...
#
# g _ ?
# ne.. ?
# t__
#     ?.th.. G..E..
# e.... S...I..
#     print 'silencing GeneratorExit...'
#     p_
