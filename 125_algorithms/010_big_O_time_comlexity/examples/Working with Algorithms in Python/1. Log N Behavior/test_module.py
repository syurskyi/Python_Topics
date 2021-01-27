# test code from module

from binary import *
from bst import *
import random

sample = [1,2]
a__(contains(sample, 1))
a__(contains(sample, 2))
a__(not contains(sample, 3))

sample = [1,2,3,4]
a__(bs_contains(sample,1) == 0)
a__(bs_contains(sample,2) == 1)
a__(bs_contains(sample,3) == 2)
a__(bs_contains(sample,4) == 3)

a__(bs_contains([],1) == -1)

x = [1, 2, 3]
insertInPlace(x, 4)
a__([1,2,3,4] == x)
insertInPlace(x, 0)
a__([0,1,2,3,4] == x)
insertInPlace(x, 2.5)
a__([0,1,2,2.5,3,4] == x)


# binary tree tests
bt = BinaryTree()
a__(bt.root == None)

# check ranomd insertion and validate presence
x = range(128)
random.shuffle(x)
for i in x:
    bt.add(i)

for i in range(128):
    a__(bt.contains(i))

# delete one by one, and validate remaining ones are present
# Note: this test case caught misnamed attributed 'val'
for i in range(128):
    bt.remove(i)
    a__(not bt.contains(i))
    for j in range(i+1, 128):
        a__(bt.contains(j))

        


