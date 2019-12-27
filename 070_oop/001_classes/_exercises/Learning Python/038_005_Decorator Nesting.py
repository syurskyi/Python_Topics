# # @A
# # @B
# # @C
# # def f(...):
# # ...
# # runs the same as the following:
# # def f(...):
# # ...
# # f = A(B(C(f)))
# #
# # @spam
# # @eggs
# # class C:
# # ...
# # X = C()
# # is equivalent to the following:
# # class C:
# # ...
# # C = spam(eggs(C))
# # X = C()
# #
# #
# 
# ___ d1 F
#     r_ F
# 
# ___ d2 F
#     r_ F
# 
# ___ d3(F):
#     r_ F
# #
# 1
# 2
# 3
# ___ func               # func = d1(d2(d3(func)))
#     print('spam')
# #
# func()                    # Prints "spam"
# 
# 
# 
# 
# ___ _1 F r_ l____ 'X' + F
# ___ _2 F r_ l____ 'Y' + F
# ___ _3 F r_ l____ 'Z' + F
# 
# 1
# 2
# 3
# ___ func               # func = d1(d2(d3(func)))
#     r_ 'spam'
# 
# print(func())             # Prints "XYZspam"
