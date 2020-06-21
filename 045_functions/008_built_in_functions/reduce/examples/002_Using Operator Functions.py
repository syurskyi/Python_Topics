# python code to demonstrate working of reduce()
# using operator functions

# importing functools for reduce()
import functools

# importing operator for operator functions
import operator

# initializing list
lis = [ 1 , 3, 5, 6, 2, ]

# using reduce to compute sum of list
# using operator functions
print ("The sum of the list elements is : ",end="")
print (functools.reduce(operator.add,lis))

# using reduce to compute product
# using operator functions
print ("The product of list elements is : ",end="")
print (functools.reduce(operator.mul,lis))

# using reduce to concatenate string
print ("The concatenated product is : ",end="")
print (functools.reduce(operator.add,["geeks","for","geeks"]))

# Output
#
# The sum of the list elements is : 17
# The product of list elements is : 180
# The concatenated product is : geeksforgeeks