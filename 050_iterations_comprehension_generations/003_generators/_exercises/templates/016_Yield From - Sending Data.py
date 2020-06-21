# # Yield From - Sending Data
# #
# # When we use yield from to delegate to a subgenerator, the established communication conduit also carries any data
# # sent to the delegator generator.
# # Let's write a simple coroutine that will receive string data and print the reversed string to the console:
# # We can use this coroutine this way:
# # And we can close the generator:
#
# ___ echo  :
#     w___  T...
#         received _ y____
#         print r.. ::-1
#
# e _ echo
# ne.. e   # prime the coroutine
#
# e.se.. 'stressed'
# e.se.. 'tons'
# e.cl..
#
# # Yield From - Sending Data
# # Now let's write a simple delegator generator:
# # We can create the delegator generator and prime the delegator:
# # Now, calling next on the delegator will establish the connection to the subgenerator and automatically prime
# # it as well.
# # We can easily see this by doing some inspection:
# # We can now send data to the delegator, and it will pass that along to the subgenerator:
#
# ___ delegator
#     e _ echo
#     y____ f... e
#
# d _ delegato
# ne.. d
#
# f... i.... _______ g..g..s  g..g..l
#  g..g..l d
# e _  g..g..l d | e |
# print g..g..s d
# print g..g..s e
#
# # Yield From - Sending Data
# # Let's modify our echo coroutine to both receive and yield a result, instead of just printing to the console:
# # And we can use delegation as follows:
#
# ___ echo
#     output _ N...
#     w___  T...
#         received _ y____ o...
#         output _ r.... ::-1
#
# e _ echo
# ne.. e
# e.send 'stressed'
#
# ___ delegator
#     y____ f... e....
#
# d _ delegator
# ne.. d
#
# d.se.. 'stressed'
