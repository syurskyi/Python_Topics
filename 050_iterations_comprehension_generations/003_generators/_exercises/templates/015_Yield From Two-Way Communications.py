# # Yield From - Two-Way Communications
# #
# # in the last section on generators, we started looking at yield f... and how we could delegate iteration to
# # another iterator.
# # Alternatively we could write the same thing this way:
#
# # i
# ___ squares n
#     ___ ? __ ra__ n
#         y____ ? ** 2
#
# # value
# ___ delegator n
#     ___ ? __ sq.. ?
#         y____ ?
#
# gen _ ? 5
# ___ _ __ ra__ 5
#     print ne__ ?
#
# ___ ? n
#     y____ f... sq.. ?
#
#
# gen _ ? 5
# ___ _ __ ra__ 5
#     print ne__ ?
#
#
# # Yield From - Two-Way Communications
# # Let's start by looking at how the delegator works when a subgenerator closes by itself:
# # We'll want to inspect the delegator and the subgenerator, so let's import what we'll need from the inspect module:
# # Here play_song is the delegator, and song is the subgenerator. We, the Jupyter notebook, are the caller.
# # As you can see, no local variables have been created in player yet - that's because it is created,
# # not actually started.
# # We can now get a handle to the subgenerator s:
# # And we can check the state of s:
# # As we can see the subgenerator is suspended.
# # Let's iterate a few more times:
#
# f... i..... _______  g..g..s,  g..g..l
#
# ___ song
#     y____ "I'm a lumberjack and I'm OK"
#     y____ "I sleep all night and I work all day"
#
# ___ play_song
#     count _ 0
#     s _ song
#     y____ f... s
#     y____ 'song finished'
#     print 'player is exiting...'
#
# player _ play_song
# print  g..g..s pl..
# print  g..g..l pl..
#
# ne__ player
#
# print  g..g..s pl..
# print  g..g..l pl..
# s _  g..g..l pl.. |s|
#
# print  g..g..s s
#
# print ne__ pl..
# print  g..g..s pl..
# print  g..g..s s
#
# print ne__ pl..
# print  g..g..s pl..
# print  g..g..s s
#
# # Yield From - Two-Way Communications
# #
# # Important to note here is that when the subgenerator returned, the delegator continued running normally.
# #
# # Let's make a tweak to our player generator to make this even more evident:
#
# ___ player
#     count _ 1
#     w____ T..
#         print 'Run count:' ?
#         y____ f... song
#         ? +_ 1
#
# p _ pl...
# ne__ p , ne__ p
# ne__ p , ne__ p
# ne__ p , ne__ p
