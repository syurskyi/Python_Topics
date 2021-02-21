# # Yield From - Throwing Exceptions
# #
# # We have seen that yield from allows us to establish a 2-way communication channel with a subgenerator and we could use
# # ne.., and se.. to se.. a "request" to a delegated subgenerator via the delegator generator.
# # In fact, we can also se.. exceptions by throwing an E.... into the delegator, just like a se..
#
# c_ CloseCoroutine E.... :
#     p___
#
# ___ echo
#      t__
#         w___ T...
#             received _ y____
#             print r...
#     e.... C..C...
#         r_ 'coro was closed'
#     e.... G..E..
#         print 'closed method was called'
#
# e _ echo
# ne.. e
#
# e.th.. CloseCoroutine, 'just closing'
#
# e _ echo
# ne.. e
# e.cl..
#
# # Yield From - Throwing Exceptions
# # As we can see the difference between th.. and close is that although close causes an E.... to be raised in
# # the generator, Python essentially silences it.
# # It works the same way when we delegate to the coroutine in a delegator:
#
# ___ delegator
#     result _ y____ f.. ec..
#     y____ 'subgen closed and returned:' r..
#     print 'delegator closing...'
#
# d _ delegator
# ne.. d
# d.se.. 'hello'
#
# d.th.. C....C....
#
# # Yield From - Throwing Exceptions
# # Now what happens if the th.. in the subgenerator does not cl.. subgenerator but instead silences the E....
# # and yields a value instead?
#
# c_ CloseCoroutine E....
#     p___
#
# c_ IgnoreMe E....
#     p___
#
# ___ echo
#      t__:
#         w___ T...:
#              t__:
#                 received _ y____
#                 print r...
#             e.... IgnoreMe
#                 y____ "I'm ignoring you..."
#     e.... C...C..
#         r_ 'coro was closed'
#     e.... G..E..
#         print 'closed method was called'
#
# d _ d....
# ne.. d
#
# d.se.. 'python'
#
# result _ d.th.. IgnoreMe, 1000
#
# result
#
# d.se.. 'rocks!'
# d.cl..
#
#
# # Yield From - Throwing Exceptions
# # Why did we not get a yielded value back?
# # That's because the subgenerator was paused at the yield that yielded "I'm, ignoring you".
#
# # If we want to coroutine to continue running normally after ignoring that E.... we need to tweak it slightly:
#
# ___ echo
#      t__
#         output _ N...
#         w___ T...:
#              t__:
#                 received _ y____ output
#                 print r...
#             e.... IgnoreMe
#                 output _ "I'm ignoring you..."
#             e____
#                 output _ N...
#     e.... C...C...
#         r_ 'coro was closed'
#     e.... G..E..
#         print 'closed method was called'
#
# d _ d...
# ne.. d
#
# d.se.. 'hello'
# d.th.. IgnoreMe
# d.se.. 'python'
# d.cl..
#
# # Yield From - Throwing Exceptions
# # What happens if we do not handle the error in the subgenerator and simply let the E.... propagate up?
# # Who gets the E...., the delegator, or the caller?
#
# ___ echo
#     w___ T...
#         received _ y____
#         print r...
#
# ___ delegator
#     y____ f.. ec..
#
# d _ d.....
# ne.. d
#
# d.th.. V..E..
#
# # Yield From - Throwing Exceptions
# # OK, so we, the caller see the E..... But did the delegator see it too? i.e.
# # can we catch the E.... in the delegator?
# # As you can see, we were able to catch the E.... in the delegator. Of course, the way we wrote our code,
# # the delegator still closed, and hence we now see a StopIteration E.....
#
# ___ delegator
#      t__:
#         y____ f.. ec..
#     e.... V..E..
#         print 'got the value error'
# d _ d....
# ne.. d
#
# d.th.. V..E..
#
