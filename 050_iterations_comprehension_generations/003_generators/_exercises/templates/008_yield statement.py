# # yield statement
#
# # The yield statement is used almost like a return statement in a function - but there is a huge difference -
# # when the yield statement is encountered, Python returns whatever value yield specifies,
# # but it "pauses" execution of the function. We can then "call" the same function again and it will "resume"
# # from where the last yield was encountered.
#
# # yield statement simple example
# # And in fact that's exactly what Python generators are - they are iterators.
# # If generators are iterators, they should implement the iterator protocol.
# #
# # And so we just have an iterator, which we can use with the iter   function and the next   function like any other iterator:
#
# ___ my_func
#     print 'line 1'
#     y__ 'Flying'
#     print 'line 2'
#     y__ 'Circus'
#
# my_func
# gen_my_func _ m._f..
# n... g...
# n... g...
# # And let's call it one more time:
# n... g...  # error
#
# gen_my_func _ my_func
# '__iter__' i_ di. gen_my_func
# '__next__' i_ di. gen_my_func
#
# gen_my_func
# it.. g....
