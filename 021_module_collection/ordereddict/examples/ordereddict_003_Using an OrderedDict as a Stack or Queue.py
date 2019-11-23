# Using an OrderedDict as a Stack or Queue
# If you are familiar with stacks and queues, you are probably wondering if the popitem method means we can effectively
# use an OrderedDict as such data structures.
# Well yes, we can, but the real question is whether it is as efficient as using a deque for example.
# Let's try it out and do some timings:

from timeit import timeit
from collections import deque
def create_ordereddict(n=100):
    d = OrderedDict()
    for i in range(n):
        d[str(i)] = i
    return d

def create_deque(n=100):
    return deque(range(n))

# Now let's time how log it takes to pop off the last element of each data structure repeatedely until the structure
# is empty.
# Instead of testing each time if the structure is empty, I'm going to simply pop items until I get an exception -
# since I only expect one exception and many many more succesful pop attempts, this will be more efficient:
# A deque will raise an IndexError exception if we attempt to pop an item from an empty deque. The OrderedDict
# will raise a KeyError exception.

def pop_all_ordered_dict(n=1000, last=True):
    d = create_ordereddict(n)
    while True:
        try:
            d.popitem(last=last)
        except KeyError:
            # done popping
            break

def pop_all_deque(n=1000, last=True):
    dq = create_deque(n)
    if last:
        pop = dq.pop
    else:
        pop = dq.popleft
    while True:
        try:
            pop()
        except IndexError:
            break

# Now let's go ahead and time these operations, both the creations and the pops:

timeit('create_ordereddict(10_000)', globals=globals(), number=1_000)
# 2.2906384040252306

timeit('create_deque(10_000)', globals=globals(), number=1_000)
# 0.1509137399843894

# Now let's time popping elements - keep in mind that we are also timing the recreation of the data structures every
# time as well - so our timings are going to be biased because of that. A very rough way of rectifying that will be to
# subtract how much time we measured above for creating the structures by themselves:

n = 10_000
number = 1_000
results = dict()

results['dict_create'] = timeit('create_ordereddict(n)', globals=globals(), number=number)
results['deque_create'] = timeit('create_deque(n)',  globals=globals(), number=number)
results['dict_create_pop_last'] = timeit('pop_all_ordered_dict(n, last=True)', globals=globals(), number=number)
results['dict_create_pop_first'] = timeit('pop_all_ordered_dict(n, last=False)',globals=globals(), number=number)
results['deque_create_pop_last'] = timeit('pop_all_deque(n, last=True)',globals=globals(), number=number)
results['deque_create_pop_first'] = timeit('pop_all_deque(n, last=False)',globals=globals(), number=number)
results['dict_pop_last'] = (results['dict_create_pop_last'] - results['dict_create'])
results['dict_pop_first'] = (results['dict_create_pop_first'] - results['dict_create'])
results['deque_pop_last'] = (results['deque_create_pop_last'] - results['deque_create'])
results['deque_pop_first'] = (results['deque_create_pop_first'] - results['deque_create'])
for key, result in results.items():
    print(f'{key}: {result}')


# dict_create: 2.3447022930486128
# deque_create: 0.15744277997873724
# dict_create_pop_last: 4.827248840010725
# dict_create_pop_first: 4.72704964800505
# deque_create_pop_last: 0.3677212379989214
# deque_create_pop_first: 0.3731844759895466
# dict_pop_last: 2.482546546962112
# dict_pop_first: 2.382347354956437
# deque_pop_last: 0.2102784580201842
# deque_pop_first: 0.2157416960108094

# As you can see, even though we can certainly use an OrderedDict as a stack or queue (and there might be good reasons
# why we want to use a dictionary for such structures), if you can use a deque you will get much faster performance.
# One good reason might be if you both need a stack/queue and also need to check for the existence of items frequently
# - searching a list is very inefficient compared to a dictionary, so depending on your use case the cost of
# looking up items in a deque might be worth the cost of popping/inserting items in an OrderedDict instead.
