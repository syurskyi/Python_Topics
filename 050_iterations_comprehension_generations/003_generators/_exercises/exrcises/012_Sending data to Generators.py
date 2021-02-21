# # Sending data to Generators
#
# # With PEP 342, generators were enhanced to allow not just sending data out  yielding , but also receiving data.
# # The basic idea is that when a generator is suspended after a yield statement,
# # why not allow sending it some data when we resume its execution, exactly at the point where it resumes.
# # i_ other words, immediately after the yield statement.
# # And not on the ne.. line of code, but actually i_ the same line as the yield -
# # we should now think of the yield keyword, not just as a statement, but as an expression that also receives data -
# # and we can assign that received value to a variable using an assignment. We can send data to the suspended generator
# #  and resume running it  by using the send   method of the generator  instead of just using the __next__ method
# #  or, same thing, ne.. )).
# # Note: The same yield keyword is actually used to do both - but make no mistake,
# # these are very different usages of the same keyword.
# #
# # The key difference is that yield is actually an expression, not a simple statement -
# # and of course we can assign expressions to variables.
#
# # Sending data to Generators
# # simple example
# # We now have a generator object, but what is it's state?
# # t will first evaluate the right hand side - at which time it will yield and therefore become suspended!
# # Now that it is waiting to resume, we can send it data, and the generator will received that data as if it were
# # the right hand side of the assignment:
# # And now the generator continued running until it hit a yield again -
# # which it does since we have our yield inside an infinite loop:
# # So, the send method essentially resume the generator just as the __next__ does - but it also sends i_ some data
# # that we can capture if we want to, inside the generator.
# # What happens if we do call ne.. ()  or __next__ instead of send  ?
# # The same as if we had sent the None value:
#
# ___ echo
#     w____ T...
#         received _ y____
#         print 'You said:', r...
#
# e _ e...
#
# f... ins... ______ g_g_s
# g_g_s e
# ne.. e
# g_g_s e
# e.send 'python'
# e.send 'I said'
# ne.. e
# ne.. None
#
# # Sending data to Generators
# #
# # At this point we can see that generators can be used to both send and receive data.
#
# ___ squares n
#     ___ i i_ ra... n
#         received _ y____ i ** 2
#         print 'received:' r....
#
# sq _ squares 5
# ne.. sq
#
# yielded _ sq.send 'hello'
# print 'yielded:' y....
#
# yielded _ sq.send 'hello'
# print 'yielded:' y....
#
# # Sending data to Generators
# # Of course, once the generator no longer yields, but returns we'll get the same StopIteration exception:
# # The ne.. send is going to resume the generator, it will print what we send it, and continue running -
# # but this time the loop is done, so it will print our final that's all, folks, and the function will r_  None
# # and hence cause a StopIteration exception to be raised:
#
# ___ echo max_times
#     ___ i i_ ra... m.._t..
#         received _ y____
#         print 'You said:' r...
#     print "that's all, folks!"
#
# e _ echo 3
# ne.. e
#
# e.send 'python'
# e.send 'is'
#
# e.send 'awesome'
#
# # Sending data to Generators
# #
# # Consider this example where we want a generator/coroutine that maintains  and yields  a running average of values
# # we send it.
# # Let's first see how we would do it without using a coroutine - instead we'll use a closure so we can maintain
# # the state  total and count :
# # And now the same, but using a coroutine:
#
# ___ averager
#     total _ 0
#     count _ 0
#     ___ inner value
#         non____ t...
#         non____ c...
#         tot.. +_ va..
#         count +_ 1
#         r_ total / count
#     r_ inner
#
# ___ running_averages iterable
#     avg _ averager
#     ___ value i_ iterable
#         running_average _ avg value
#         print r.._a..
#
# r._a.  1 2 3 4
#
# ___ running_averager
#     total _ 0
#     count _ 0
#     running_average _ N...
#     w____ T...:
#         value _ y____ r..._a..
#         tot.. +_ value
#         count +_ 1
#         running_average _ total / count
#
# ___ running_averages iterable
#     averager _ running_averager
#     ne.. averager   # prime generator
#     ___ value i_ it...
#         running_average _ averager.send value
#         print running_average
#
# r.._a.. 1 2 3 4
