# # File devtools_test.py
# # Comment lines raise TypeError unless "python -O" used on shell command line
# from devtools_new import rangetest
# 
# 
# # Test functions, positional and keyword
# 
# _r.. age_(0, 120))  # persinfo = rangetest(..)(persinfo)
# ___ persinfo name age
#     print('@ is @ years old' @  n.. a..
# 
# 
# _r.. M_(1, 12), D_(1, 31), Y_(0, 2009))
# ___ birthday M, D, Y
#     print('birthday = 0 / 1 / 2'.f... M, D, Y
# 
# 
# p.. ('Bob', 40)
# p.. (age=40, name='Bob')
# b...(5, D=1, Y=1963)
# 
# 
# # persinfo('Bob', 150)
# # persinfo(age=150, name='Bob')
# # birthday(5, D=40, Y=1963)
# 
# 
# # Test methods, positional and keyword
# 
# c_ Person
#     ___ - ____ name job pay
#         ____.j.. _ j..
#         ____.p.. _ p..
#         # giveRaise = rangetest(..)(giveRaise)
# 
#     _r.. percent_ 0.0, 1.0  # percent passed by name or position
#     ___ giveRaise ____ p..
#         ____.p.. _ in. ____.p.. * (1 + p...
# 
# 
# bob = Person('Bob Smith', 'dev', 100000)
# sue = Person('Sue Jones', 'dev', 100000)
# bob.giveRaise(.10)
# sue.giveRaise(percent=.20)
# print(bob.pay, sue.pay)
# 
# 
# # bob.giveRaise(1.10)
# # bob.giveRaise(percent=1.20)
# 
# 
# # Test omitted defaults: skipped
# 
# _r..(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
# ___ omitargs(a, b=7, c=8, d=9):
#     print(a, b, c, d)
# 
# 
# omitargs(1, 2, 3, 4)
# omitargs(1, 2, 3)
# omitargs(1, 2, 3, d=4)
# omitargs(1, d=4)
# omitargs(d=4, a=1)
# omitargs(1, b=2, d=4)
# omitargs(d=8, c=7, a=1)
# 
# # omitargs(1, 2, 3, 11)        # Bad d
# # omitargs(1, 2, 11)           # Bad c
# # omitargs(1, 2, 3, d=11)      # Bad d
# # omitargs(11, d=4)            # Bad a
# # omitargs(d=4, a=11)          # Bad a
# # omitargs(1, b=11, d=4)       # Bad b
# # omitargs(d=8, c=7, a=11)     # Bad a
# 
# #
# # C:\misc > C:\python30\python
# # devtools_test.py
