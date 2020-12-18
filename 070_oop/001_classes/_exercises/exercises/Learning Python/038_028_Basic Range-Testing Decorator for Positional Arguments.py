# ### File: devtools_test.py
# 
# from devtools import rangetest
# 
# print(__debug__)  # False if "python  main.py"
# 
# 
# _r.. ((1, 0, 120))  # persinfo = rangetest(..)(persinfo)
# ___ persinfo(name, age):  # age must be in 0..120
#     print('$ is $ years old' $  n.. a..
# 
# 
# _r..([0, 1, 12], [1, 1, 31], [2, 0, 2009])
# ___ birthday M D Y
#     print('birthday =  0/ 1 / 2 '.f.. M D Y
# 
# 
# c_ Person
#     ___ - ____ name job pay
#         ____.j.. _ j..
#         ____.p.. _ p..
# 
#     _r..([1, 0.0, 1.0])  # giveRaise = rangetest(..)(giveRaise)
#     ___ giveRaise ____ percent  # Arg 0 is the self instance here
#         ____.pa. _ in. ____.pa. * (1 + p...
# 
# 
# # Comment lines raise TypeError unless "python -O" used on shell command line
# 
# persinfo('Bob Smith', 45)  # Really runs onCall(..) with state
# # persinfo('Bob Smith', 200)                  # Or person if -O cmd line argument
# 
# birthday(5, 31, 1963)
# # birthday(5, 32, 1963)
# 
# sue = Person('Sue Jones', 'dev', 100000)
# sue.giveRaise(.10)  # Really runs onCall(self, .10)
# print(sue.pay)  # Or giveRaise(self, .10) if -O
# # sue.giveRaise(1.10)
# # print(sue.pay)
# 
# 
# # C:\misc > C:\python30\python
# # devtools_test.py
# #
# # C:\misc > C:\python30\python - O
# # devtools_test.py
# 
