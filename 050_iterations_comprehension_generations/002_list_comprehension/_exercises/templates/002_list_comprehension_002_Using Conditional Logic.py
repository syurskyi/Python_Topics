# # Using Conditional Logic
# # Earlier, you saw this formula for how to create list comprehensions:
# # new_list = [expression for member in iterable]
# # While this formula is accurate, it’s also a bit incomplete. A more complete description of the comprehension formula
# # adds support for optional conditionals. The most common way to add conditional logic to a list comprehension is
# # to add a conditional to the end of the expression:
# # new_list = [expression for member in iterable (if conditional)]
# # Here, your conditional statement comes just before the closing bracket.
# # ditionals are important because they allow list comprehensions to filter out unwanted values, which would
# # normally require a call to filter():
#
# sentence _ 'the rocket came back from mars'
# vowels _ i ___ i __ ? __ ? __ 'aeiou'
# print v..
# # ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']
#
# # In this code block, the conditional statement filters out any characters in sentence that aren’t a vowel.
# # The conditional can test any valid expression. If you need a more complex filter, then you can even move
# # the conditional logic to a separate function:
#
# sentence _ 'The rocket, who was named Ted, came back \
# from Mars because he missed his friends.'
#
#
# ___ is_consonant letter
#     vowels _ 'aeiou'
#     r_ le__.isa.. an. le___.lo.. no. i. vo..
#
#
# consonants _ i ___ ? __ se.. __ i._c. i
# # ['T', 'h', 'r', 'c', 'k', 't', 'w', 'h', 'w', 's', 'n', 'm', 'd', \
# # 'T', 'd', 'c', 'm', 'b', 'c', 'k', 'f', 'r', 'm', 'M', 'r', 's', 'b', \
# # 'c', 's', 'h', 'm', 's', 's', 'd', 'h', 's', 'f', 'r', 'n', 'd', 's']
#
# # Here, you create a complex filter is_consonant() and pass this function as the conditional statement for
# # your list comprehension. Note that the member value i is also passed as an argument to your function.
# # You can place the conditional at the end of the statement for simple filtering, but what if you want to change
# # a member value instead of filtering it out? In this case, it’s useful to place the conditional
# # near the beginning of the expression:
# # new_list = [expression (if conditional) for member in iterable]
# # With this formula, you can use conditional logic to select from multiple possible output options.
# # For example, if you have a list of prices, then you may want to replace negative prices with 0 and leave
# # the positive values unchanged:
# #
# original_prices _ 1.25, -9.45, 10.22, 3.78, -5.92, 1.16
# prices _  i __ ? > 0 e___ 0 ___ ? __ o.._p..
# print p...
# # [1.25, 0, 10.22, 3.78, 0, 1.16]
#
# # Here, your expression i contains a conditional statement, if i > 0 else 0. This tells Python to output the value
# # of i if the number is positive, but to change i to 0 if the number is negative. If this seems overwhelming,
# # then it may be helpful to view the conditional logic as its own function:
#
#
# ___ get_price price
#     r__ p... i_ ? > 0 e___ 0
#
#
# prices _ ? i ___ ? __ o._p.
# print ?
# # [1.25, 0, 10.22, 3.78, 0, 1.16]
#
# # Now, your conditional statement is contained within get_price(), and you can use it as part of
# # your list comprehension expression.
