# # Generator States
# # We create an generator object by calling the generator function:
# # At this point the generator object is created, but we have not actually started running it. To do so, we call ne..  ,
# # which then starts running the function body until the first yield is encountered:
# #
# # Now the generator is suspended, waiting ___ us to call ne.. again:
# #
# # Every time we call ne.., the generator function runs, or is i_ a running state until the ne.. yield is encountered,
# # or no more results are yielded and the function actually returns:
#
# # c
# ___ gen s
#     ___ ? __ ?
#         y____ ?
#
# g _ gen 'abc'
#
# ne.. g
#
# ne.. g
#
# ne.. g
#
# # Generator States
# #
# # We can actually request the state of a generator programmatically by using the inspect module's
# # getgeneratorstate   function:
# #
# # We can start running the generator by calling ne..:
# #
# # And the state is now:
# # Once we exhaust the generator:
# # The generator is now in a closed state:
#
# f.. in.. _______ getgeneratorstate
# g _ g.. *abc
# get...... ?
#
# ne.. g
#
# get...... g
#
# ne.. g , ne.. g , ne.. g
#
# # Generator States
# #
# # Now we haven't seen the running state - to do that we just need to print the state from inside the generator -
# # but to do that we need to have a reference to the generator object itself. This is not that easy to do,
# # so I'm going to cheat and assume that the generator object will be referenced by a global variable global_gen:
#
# # c
# ___ gen s
#     ___ ? __ ?
#         print get...... global_gen
#         y____ ?
#
# global_gen _ gen 'abc'
#
# ne.. ?
#
# # Generator States
# #
# # Finally it is really important to understand that when a yield is encountered,
# # the generator is suspended exactly at that point, but not before it has evaluated the expression to the right
# # of the yield statement so it can produce that value i_ the r_ value of the next   function.
# #
# # As you can see square i  was evaluated, then the value was yielded, and the genrator was suspended exactly at
# # the point the yield statement was encountered:
# #
# # As you can see, only now does the right after yield string get printed from our generator.
#
# ___ square i
#     print _*squaring |?|*
#     r_ ? ** 2
#
# # i
# ___ squares n
#     ___ ? __ ra... ?
#         y____ ? ?
#         print  'right after yield'
#
# sq _ ? 5
# ne.. ?
#
# ne.. ?
