# # Yield From - Two-Way Communications
# #
# # i_ the last section on generators, we started looking at yield f... and how we could delegate iteration to
# # another iterator.
# # Alternatively we could write the same thing this way:
#
# ___ squares n
#     ___ i i_ ra__ n
#         y____ i ** 2
#
# ___ delegator n
#     ___ value i_ sq.. n
#         y____ va..
#
# gen _ delegator 5
# ___ _ i_ ra__ 5 :
#     print ne__ gen
#
# ___ delegator n
#     y____ f... sq.. n
#
#
# gen _ delegator 5
# ___ _ i_ ra__ 5 :
#     print ne__ gen
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
#         print 'Run count:' c...
#         y____ f... song
#         count +_ 1
#
# p _ pl...
# ne__ p , ne__ p
# ne__ p , ne__ p
# ne__ p , ne__ p
