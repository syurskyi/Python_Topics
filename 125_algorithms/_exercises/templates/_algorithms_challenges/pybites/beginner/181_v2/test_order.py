_______ i___

_______ p__

____ order _______ OrderedList


?p__.f..(scope='module')
___ order
    r.. OrderedList()


?p__.m__.p.("num, expected", [
    (10, '10'),
    (9, '9, 10'),
    (16, '9, 10, 16'),
    (2, '2, 9, 10, 16'),
    (7, '2, 7, 9, 10, 16'),
    (1, '1, 2, 7, 9, 10, 16'),
    (5, '1, 2, 5, 7, 9, 10, 16'),
])
___ test_order(order, num, expected
    order.add(num)
    ... s..(order) __ expected


___ test_does_not_use_manual_sort
    ... '.sorted' n.. __ i___.getsource(OrderedList)
    ... '.sort(' n.. __ i___.getsource(OrderedList)