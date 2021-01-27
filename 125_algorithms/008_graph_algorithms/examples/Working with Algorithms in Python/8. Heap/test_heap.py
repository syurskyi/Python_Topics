# test module and project code

from heap import *
from project_heap import *

x = range(20)
heapsort(x)
a__(range(20) == x)

x = [2]
heapsort(x)
a__([2] == x)

# evaluate projects also

a__(2 == kthSmallest(range(10),3))
a__(0 == kthSmallest(range(10),1))
a__(9 == kthSmallest(range(10),10))
