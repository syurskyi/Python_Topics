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
# ___ gen s
#     ___ c i_ s
#         y____ c
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
# g _ gen 'abc'
# get...... g
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
# ___ gen s :
#     ___ c i_ s:
#         print get...... global_gen
#         y____ c
#
# global_gen _ gen 'abc'
#
# ne.. global_gen
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
#     print _*squaring |i|*
#     r_ i ** 2
#
# ___ squares n
#     ___ i i_ ra... n
#         y____ square i
#         print  'right after yield'
#
# sq _ squares 5
# ne.. sq
#
# ne.. sq
