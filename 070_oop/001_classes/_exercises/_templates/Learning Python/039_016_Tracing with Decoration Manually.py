# from mytools2 import tracer
# 
# c_ Person
#     _t..
#     ___ - ____ name pay
#         ____.n.. _ n..
#         ____.p..  _ p..
# 
#     _t..
#     ___ giveRaise ____ percent         # giveRaise = tracer(giverRaise)
#         ____.pay *_ (1.0 + p..      # onCall remembers giveRaise
# 
#     _t..
#     ___ lastName ____                   # lastName = tracer(lastName)
#         r_ ____.n__.sp.. -1
# 
# bob = ?('Bob Smith', 50000)
# sue = ?('Sue Jones', 100000)
# print(bob.name, sue.name)
# sue.giveRaise(.10)                        # Runs onCall(sue, .10)
# print(sue.pay)
# print(bob.lastName(), sue.lastName())     # Runs onCall(bob), remembers lastName
# 
