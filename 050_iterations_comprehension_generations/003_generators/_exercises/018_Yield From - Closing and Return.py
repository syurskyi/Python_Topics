# # Yield From - Closing and Return
# # Just as we can se.. ne.. and se.. through a delegator, we can also se.. close.
# # How does this affect the delegator and the subgenerator?
# # At this point, both the delegator and the subgenerator are primed and suspended:
# # We can se.. data to the delegator:
# # We can even se.. data directly to the subgenerator since we now have a handle on it:
# # In fact, we can close it too:
# # So, what is the state of the delegator now?
# # But the subgenerator closed, so let's see what happens when we call ne.. on d:
# # As you can see, the generator code resume right after the yield from,
# # and we can do this one more time to close the delegator:
#
# ___ subgen
#     t__:
#         w___ T...
#             received _ y____
#             print received
#     f_____
#         print 'subgen: closing...'
#
# ___ delegator
#     s _ subgen
#     y____ f..
#     y____ 'delegator: subgen closed'
#     print 'delegator: closing...'
#
# d _ d......
# ne.. d
#
# f__ in... _______ g..g..s, g..g..l
#
# g..g..l d
#
# s _ g..g..l d | s |
# print g..g..s d
# print g..g..s s
#
# d.se.. 'hello'
# s.se.. 'python'
# s.close
#
# g..g..s d
#
# ne.. d
#
# # Yield From - Closing and Return
# # so this is what happens when the subgenerator closes  directly or indirectly  - the delegator simply resumes running
# # right after the yield from when we call ne...
# # But what happens if we close the delegator instead of just closing the subgenerator?
# # As you can see the subgenerator also closed. Is the delegator closed too?
#
# d _ d....
# ne.. d
# s _ g..g..l d | s |
# print g..g..s d
# print g..g..s s
#
# d.close
#
# print g..g..s d
# print g..g..s s
#
# # Yield From - Closing and Return
# # Yes. So closing the delegator will close not only the delegator itself,
# # but also close the currently active subgenerator  if any .
# # We should notice that when we closed the subgenerator directly no apparent exception was raised in our context.
# # What happens if the subgenerator returns something when it closes?
# # Hmmm, the StopIteration exception was silenced. Let's do this a different way,
# # since we know the StopIteration exception should contain the return value:
#
# ___ subgen
#     t__:
#         w___ T...
#             received _ y____
#             print r...
#     f_____:
#         print 'subgen: closing...'
#         r_ 'subgen: return value'
#
# s _ s.....
# ne.. s
# s.se.. 'hello'
# s.cl..
# s _ s...
# ne.. s
# s.se.. 'hello'
# s.th.. G...E.. 'force exit'
#
# # Yield From - Closing and Return
# # OK, so now we can see that the StopIteration exception contains the return value.
# # The yield from actually captures that value as it's return value - in other words yield from is not just a statement,
# # it is in fact, like yield, also an expression.
# # Let's see how that works:
# # As you can see the return value of the subgenerator ended up as the result of the yield from expression.
#
# ___ subgen
#     t__:
#         y____ 1
#         y____ 2
#     f_____:
#         print 'subgen: closing...'
#         r_ 100
#
# ___ delegator
#     s _ subgen
#     result _ y____ f... s
#     print 'subgen returned:' r...
#     y____ 'delegator suspended'
#     print 'delegator closing'
#
# d _ d.......
# ne.. d
# ne.. d
# ne.. d
