# # How to Create Lists in Python
# # There are a few different ways you can create lists in Python. To better understand the trade-offs of using
# # a list comprehension in Python, let’s first see how to create lists with these approaches.
# # Using for Loops
# #
# # The most common type of loop is the for loop. You can use a for loop to create a list of elements in three steps:
# #
# #     Instantiate an empty list.
# #     Loop over an iterable or range of elements.
# #     Append each element to the end of the list.
# #
# # If you want to create a list containing the first ten perfect squares, then you can complete these steps
# # in three lines of code:
#
# squares _    # list
# ___ i __ ra.. 10
#     ?.ap.. i * i
# print ?
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# # Here, you instantiate an empty list, squares. Then, you use a for loop to iterate over range(10). Finally,
# # you multiply each number by itself and append the result to the end of the list.
# # Using map() Objects
# # map() provides an alternative approach that’s based in functional programming. You pass in a function and an iterable,
# # and map() will create an object. This object contains the output you would get from running each iterable element
# # through the supplied function.
# # As an example, consider a situation in which you need to calculate the price after tax for a list of transactions:
#
# txns _  1.09, 23.56, 57.84, 4.56, 6.78  # List
# TAX_RATE _ .08
#
#
# ___ get_price_with_tax txn
#     r_ t.. *  1 + T..
#
#
# final_prices _ ma. ? t...
# l.. ?
# # [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]
#
# # Here, you have an iterable txns and a function get_price_with_tax(). You pass both of these arguments to map(),
# # and store the resulting object in final_prices. You can easily convert this map object into a list using list().
# # Using List Comprehensions
# # List comprehensions are a third way of making lists. With this elegant approach, you could rewrite the
# # for loop from the first example in just a single line of code:
#
# squares _ i * i ___ ? __ ra.. 10
# print ?
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# # Rather than creating an empty list and adding each element to the end, you simply define the list and its contents
# # at the same time by following this format:
# # new_list = [expression for member in iterable]
#
# # Every list comprehension in Python includes three elements:
# #     expression is the member itself, a call to a method, or any other valid expression that returns a value.
# #     In the example above, the expression i * i is the square of the member value.
# #     member is the object or value in the list or iterable. In the example above, the member value is i.
# #     iterable is a list, set, sequence, generator, or any other object that can return its elements one at a time.
# #     In the example above, the iterable is range(10).
# # Because the expression requirement is so flexible, a list comprehension in Python works well in many places where
# # you would use map(). You can rewrite the pricing example with its own list comprehension:
#
# txns _ 1.09, 23.56, 57.84, 4.56, 6.78   # List
# TAX_RATE _ .08
#
#
# ___ get_price_with_tax txn
#     r_ t.. *  1 + T..
#
#
# final_prices _ ? i ___ ? __ t..
# print ?
# # [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]
#
# # The only distinction between this implementation and map() is that the list comprehension in Python returns
# # a list, not a map object.
