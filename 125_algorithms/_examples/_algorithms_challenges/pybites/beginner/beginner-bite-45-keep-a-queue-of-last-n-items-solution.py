import collections

def my_queue(n=5):
    d = collections.deque('', n)
    return d

mq = my_queue()
for i in range(10):
    mq.append(i)
print((i, list(mq)))