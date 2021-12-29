"""
Complete the add method of the OrderedList class which takes a num argument and adds that
to the self._numbers list keeping it ordered upon insert.

Using a manual .sort() or .sorted() each time is not allowed. Look into the bisect module
how to do it ...

Here is how it should works:

order = OrderedList()
order.add(10)
print(order)  # __str__ already provided
order.add(1)
print(order)
order.add(16)
print(order)
order.add(5)
print(order)
Output:

10
1, 10
1, 10, 16
1, 5, 10, 16
Picking the right data structure is usually half of the battle.
Good luck and keep calm and code more Python!
"""

_______ bisect

class OrderedList:

    ___ __init__(self):
        self._numbers    # list

    ___ add(self, num):
        bisect.insort(self._numbers, num)

    ___ __str__(self):
        r.. ', '.join(s..(num) ___ num __ self._numbers)


ol = OrderedList()
ol.add(4)
print(ol.__str__())
ol.add(1)
print(ol.__str__())
ol.add(100)
ol.add(80)
print(ol.__str__())

