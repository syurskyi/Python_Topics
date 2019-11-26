# # Deque
# # A double-ended queue, or deque, supports adding and removing elements from either end. The more commonly used stacks
# # and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end.
#
# ______ c____
#
# d = c____.d... 'abcdefg'
# print('Deque:'  d
# print('Length:' le. d
# print('Left end:'  d 0
# print('Right end:' d -1
#
# d.re.. 'c'
# print 'remove(c):' d
#
# # Since deques are a type of sequence container, they support some of the same operations that lists support,
# # such as examining the contents with __getitem__(), determining length, and removing elements from the middle
# # by matching identity.
#
# # $ python collections_deque.py
# #
# # Deque: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# # Length: 7
# # Left end: a
# # Right end: g
# # remove(c): deque(['a', 'b', 'd', 'e', 'f', 'g'])
# #
# # Populating
# # A deque can be populated from either end, termed “left” and “right” in the Python implementation.
#
# ______ c____
#
# # Add to the right
# d = c____.d...
# d.ex.. 'abcdefg'
# print('extend    :' d
# d.ap.. 'h'
# print('append    :', d
#
# # Add to the left
# d = c____.d...
# d.e..l.. 'abcdefg'
# print 'extendleft:' d
# d.ap.... 'h'
# print'appendleft:' d
#
# # Notice that extendleft() iterates over its input and performs the equivalent of an appendleft() for each item.
# #     The end result is the deque contains the input sequence in reverse order.
#
# # $ python collections_deque_populating.py
# #
# # extend    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# # append    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# # extendleft: deque(['g', 'f', 'e', 'd', 'c', 'b', 'a'])
# # appendleft: deque(['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])
# #
# # Consuming
# # Similarly, the elements of the deque can be consumed from both or either end, depending on the algorithm being applied.
#
# ______ c____
#
# print 'From the right:'
# d _ c____.d...'abcdefg'
# w___ T..
#     t__:
#         print d.po.
#     e___ I..E..
#         b___
#
# print '\nFrom the left:'
# d = c____.d... 'abcdefg'
# w___ T..
#     t__:
#         print d.p..l.
#     e___ I..E..
#         b___
#
# # Use pop() to remove an item from the “right” end of the deque and popleft() to take from the “left” end.
#
# # $ python collections_deque_consuming.py
# #
# # From the right:
# # g
# # f
# # e
# # d
# # c
# # b
# # a
# #
# # From the left:
# # a
# # b
# # c
# # d
# # e
# # f
# # g
# #
# # Since deques are thread-safe, the contents can even be consumed from both ends at the same time from separate threads.
#
# ______ c____
# ______ thr....
# ______ ti..
#
# candle _ c____.d...(ra.. 11
#
# ___ burn direction nextSource
#     w___ T..
#         t__
#             next _ n..S..
#         e___ I..E..
#             b___
#         e___
#             print('/8_: /_' / (d... n..
#             ti__.sl.. 0.1
#     print('/8_ done' / d..
#     r_
#
# left _ thr___.T.. target_burn args_ 'Left' candle.p..l..
# right = thr___.T.. target_burn args_ 'Right', candle.po.
#
# l__.st..
# r__.st..
#
# l__.jo..
# r__.jo..
#
# # The threads in this example alternate between each end, removing items until the deque is empty.
# #
# # $ python collections_deque_both_ends.py
# #
# #     Left: 0
# #    Right: 10
# #    Right: 9
# #      Left: 1
# #    Right: 8
# #     Left: 2
# #    Right: 7
# #     Left: 3
# #    Right: 6
# #     Left: 4
# #    Right: 5
# #     Left done
# #    Right done
# #
# # Rotating
# # Another useful capability of the deque is to rotate it in either direction, to skip over some items.
#
# ______ c____
#
# d _ c____.d... ra.. 10
# print('Normal        :' d
#
# d _ c____.d... ra..10
# d.ro.. 2
# print 'Right rotation:' d
#
# d _ c____.d... ra.. 10
# d.ro.. -2
# print 'Left rotation :' d
#
# # Rotating the deque to the right (using a positive rotation) takes items from the right end and moves them to the left
# # end. Rotating to the left (with a negative value) takes items from the left end and moves them to the right end.
# # It may help to visualize the items in the deque as being engraved along the edge of a dial.
#
# # $ python collections_deque_rotate.py
# #
# # Normal        : deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# # Right rotation: deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
# # Left rotation : deque([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])
