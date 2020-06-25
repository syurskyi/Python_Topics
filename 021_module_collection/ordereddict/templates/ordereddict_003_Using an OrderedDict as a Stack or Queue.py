# # Using an OrderedDict as a Stack or Queue
# # If you are familiar with stacks and queues, you are probably wondering if the popitem method means we can effectively
# # use an OrderedDict as such data structures.
# # Well yes, we can, but the real question is whether it is as efficient as using a deque for example.
# # Let's try it out and do some timings:
#
# f.. t.i. ____ t.i.
# f.. c.. ____ d..
# ___ create_ordereddict n_100
#     d _ O..
#     ___ i i_ ra.. n
#         d st. i _ i
#     r_ d
#
# ___ create_deque(n_100):
#     r_ d.. ra..n
#
# # Now let's time how log it takes to pop off the last element of each data structure repeatedely until the structure
# # is empty.
# # Instead of testing each time if the structure is empty, I'm going to simply pop items until I get an exception -
# # since I only expect one exception and many many more succesful pop attempts, this will be more efficient:
# # A deque will raise an IndexError exception if we attempt to pop an item from an empty deque. The OrderedDict
# # will raise a KeyError exception.
#
# ___ pop_all_ordered_dict n_1000 last_T..
#     d _ create_ordereddict n
#     w___ T..
#         t__
#             d.popitem(l.._l..
#         e____ K..E..
#             # done popping
#             b..
#
# ___ pop_all_deque n_1000 last_T..
#     dq _ create_deque n
#     i_ la..
#         pop _ d_.po.
#     e___
#         pop _ d_.p..l..
#     w___ T..
#         t__
#             po.
#         e.. I..E..
#             b..
#
# # Now let's go ahead and time these operations, both the creations and the pops:
#
# t.i. 'create_ordereddict 10_000 ' globals_gl..  number_1_000)
# # 2.2906384040252306
#
# t.i. 'create_deque(10_000 ' globals_g... number_1_000
# # 0.1509137399843894
#
# # Now let's time popping elements - keep in mind that we are also timing the recreation of the data structures every
# # time as well - so our timings are going to be biased because of that. A very rough way of rectifying that will be to
# # subtract how much time we measured above for creating the structures by themselves:
#
# n _ 10_000
# number _ 1_000
# r___ _ di..
#
# r__ 'dict_create' _ t.i. 'create_ordereddict(n)' gl.._gl... number_nu..
# r__ 'deque_create' _ t.i ('create_deque(n)'  gl.._gl... number_nu..
# r__ 'dict_create_pop_last' _ t.i.'pop_all_ordered_dict(n, last_True)' gl.._gl... number_nu..
# r__ 'dict_create_pop_first' _ t.i. 'pop_all_ordered_dict(n, last_False)' gl.._gl... number_nu..
# r__ 'deque_create_pop_last' _ t.i. 'pop_all_deque(n, last_True)' gl.._gl... number_nu..
# r__ 'deque_create_pop_first' _ t.i. 'pop_all_deque(n, last_False)' gl.._gl... number_nu..
# r__ 'dict_pop_last' _ r___ 'dict_create_pop_last'] - r___ 'dict_create'
# r__ 'dict_pop_first' _ r___ 'dict_create_pop_first'] - r___ 'dict_create'
# r__ 'deque_pop_last' _ r___ 'deque_create_pop_last'] - r___ 'deque_create'
# r__ 'deque_pop_first' _ r___ 'deque_create_pop_first'] - r___ 'deque_create'
# ___  result i_ r___.it..
#     print(_ 'key result
#
#
# # dict_create: 2.3447022930486128
# # deque_create: 0.15744277997873724
# # dict_create_pop_last: 4.827248840010725
# # dict_create_pop_first: 4.72704964800505
# # deque_create_pop_last: 0.3677212379989214
# # deque_create_pop_first: 0.3731844759895466
# # dict_pop_last: 2.482546546962112
# # dict_pop_first: 2.382347354956437
# # deque_pop_last: 0.2102784580201842
# # deque_pop_first: 0.2157416960108094
#
# # As you can see, even though we can certainly use an OrderedDict as a stack or queue (and there might be good reasons
# # why we want to use a dictionary for such structures), if you can use a deque you will get much faster performance.
# # One good reason might be if you both need a stack/queue and also need to check for the existence of items frequently
# # - searching a list is very inefficient compared to a dictionary, so depending on your use case the cost of
# # looking up items in a deque might be worth the cost of popping/inserting items in an OrderedDict instead.
