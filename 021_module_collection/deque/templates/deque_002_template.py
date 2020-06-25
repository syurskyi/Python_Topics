# # The deque
# # The deque is a list optimized for inserting and removing items.
# # Import the deque
# # You have to import deque class from collections module before using it.
#
# f___ c.. ______ d..
#
# # Creating a deque
# # You can create a deque with deque() constructor. You have to pass a list as an argument.
#
# list _ "a" "b" "c"
# deq _ d.. li..
# print de.
#
# # Output:
# # deque(['a', 'b', 'c'])
#
# # Inserting Elements to deque
# # You can easily insert an element to the deq we created at either of the ends. To add an element to the right
# # of the deque, you have to use append() method.
# # If you want to add an element to the start of the deque, you have to use appendleft() method.
#
# de_.a.. "d"
# de_.a..l.. "e"
# print de.  # deque
#
# # Output:
# # deque(['e', 'a', 'b', 'c', 'd'])
#
# # You can notice that d is added at the end of deq and e is added to the start of the deq
# # Removing Elements from the deque
# # Removing elements is similar to inserting elements. You can remove an element the similar way you insert elements.
# # To remove an element from the right end, you can use pop() function and to remove an element from left,
# # you can use popleft().
#
# de_.p..
# de_.p..l.
# print(deq)
#
# # Output:
# # deque(['a', 'b', 'c'])
#
# # You can notice that both the first and last elements are removed from the deq.
# # Clearing a deque
# # If you want to remove all elements from a deque, you can use clear() function.
#
# list _ "a" "b" "c"
# deq _ d.. li..
# print de.
# print d__.cl__
#
# # Output:
# # deque(['a', 'b', 'c'])
# # None
#
# # You can see in the output, at first there is a queue with three elements. Once we applied clear() function,
# # the deque is cleared and you see none in the output.
# # Counting Elements in a deque
# # If you want to find the count of a specific element, use count(x) function. You have to specify the element
# # for which you need to find the count, as the argument.
#
# list _ "a" "b" "c"
# deq _ d.. li..
# print de_.co.. "a"
#
# # Output:
# # 1
#
#
