from __future__ import print_function
class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):  # Fallback for iteration
        print('get[%s]:' % i, end='')  # Also for index, slice
        return self.data[i]

    def __iter__(self):  # Preferred for iteration
        print('iter=> ', end='')  # Allows only 1 active iterator
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):  # Preferred for 'in'
        print('contains: ', end='')
        return x in self.data


X = Iters([1, 2, 3, 4, 5])  # Make instance
print(3 in X)  # Membership
for i in X:  # For loops
    print(i, end=' | ')

print()
print([i ** 2 for i in X])  # Other iteration contexts
print(list(map(bin, X)))

I = iter(X)  # Manual iteration (what other contexts do)
while True:
    try:
        print(next(I), end=' @ ')
    except StopIteration:
        break

X = Iters('spam')  # Indexing
X[0]  # __getitem__(0)
# get[0]:'s'

'spam'[1:]  # Slice syntax

'spam'[slice(1, None)]  # Slice object


X[1:]  # __getitem__(slice(..))
# get[slice(1, None, None)]:'pam'
X[:-1]
# get[slice(None, -1, None)]:'spa'
