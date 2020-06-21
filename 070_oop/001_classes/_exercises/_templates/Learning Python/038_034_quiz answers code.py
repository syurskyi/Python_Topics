# _______ ti...
# 
# ___ timer label_'' trace_T..             # On decorator args: retain args
#     ___ onDecorator func                   # On @: retain decorated func
#         ___ onCall $ $$          # On calls: call original
#             start   _ ti__.cl..           # State is scopes + func attr
#             result  _ func($ $$
#             elapsed _ ti__.cl.. - start
#             o.C_.alltime +_ elapsed
#             i_ trace
#                 format _ '%s%s: %.5f, %.5f'
#                 values _ label, fu_. -n el.. o.C_.alltime
#                 print(format % values)
#             r_ r...
#         o.C_.alltime _ 0
#         r_ o.C.
#     r_ o.D.
# 
# # Test on functions
# 
# _t..  trace_T.., label_'[CCC]==>')
# ___ listcomp N                             # Like listcomp _ timer(...)(listcomp)
#     r_ x * 2 ___ x i_ ra.. N         # listcomp(...) triggers onCall
# 
# _t.. trace_T... label_'[MMM]==>'
# ___ mapcall  N
#     r_ li.. ma. l_____ x x * 2 ra... N   # list for 3.0 views
# 
# ___ func i_ li.. ma..
#     result _ fu.. 5                  # Time for this call, all calls, r_ value
#     ? 5000000
#     print r..
#     print('allTime _ @\n' @ f__.allt..   # Total time for all calls
# 
# # Test on methods
# 
# c_ Person
#     ___ -  ____ name pay
#         ____.n.. _ n..
#         ____.p..  _ p..
# 
#     _t..
#     ___ giveRaise ____ p...            # giveRaise _ timer()(giverRaise)
#         ____.pa. *_ (1.0 + p...          # tracer remembers giveRaise
# 
#     _t.. label_'**')
#     ___ lastName ____                      # lastName _ timer(...)(lastName)
#         r_ ____.n...sp.. -1         # alltime per class, not instance
# 
# bob _ Person('Bob Smith', 50000)
# sue _ Person('Sue Jones', 100000)
# bob.giveRaise(.10)
# sue.giveRaise(.20)                           # runs onCall(sue, .10)
# print(bob.pay, sue.pay)
# print(bob.lastName(), sue.lastName())        # runs onCall(bob), remembers lastName
# print('%.5f %.5f' % (Person.giveRaise.alltime, Person.lastName.alltime))
# 
# # Expected output
# 
# # [CCC]==>listcomp: 0.00002, 0.00002
# # [CCC]==>listcomp: 1.19636, 1.19638
# # [0, 2, 4, 6, 8]
# # allTime _ 1.19637775192
# #
# # [MMM]==>mapcall: 0.00002, 0.00002
# # [MMM]==>mapcall: 2.29260, 2.29262
# # [0, 2, 4, 6, 8]
# # allTime _ 2.2926232943
# #
# # giveRaise: 0.00001, 0.00001
# # giveRaise: 0.00001, 0.00002
# # 55000.0 120000.0
# # **lastName: 0.00001, 0.00001
# # **lastName: 0.00001, 0.00002
# # Smith Jones
# # 0.00002 0.00002
# 
# 
# 
# 
# ### question 2
# 
# 
# traceMe _ F...
# ___ trace $
#     i_ ? print('[' + ' '.jo.. ma. st. a... )) + ']')
# 
# ___ accessControl failIf
#     ___ onDecorator aClass
#         i_ no_ __debug__
#             r_ a..
#         e____
#             c_ onInstance
#                 ___ - ____ $ $$
#                     ____.__wr... _ aC.. $ $$
#                 ___ -g ____ att..
#                     tr.. 'get:', a..
#                     i_ failIf a..
#                         r____ T....  'private attribute fetch: ' + a...
#                     e____
#                         r_ g... ____.__wr.. a..
#                 ___ -s ____ attr value
#                     tr.. ('set:', at.. va..
#                     i_ a.. __ '_onInstance__wrapped':
#                         ____. -d a..| _ va..
#                     e____ failIf a..
#                         r____ T... 'private attribute change: ' + a..
#                     e____
#                         se... ____.__wr.. a.. v...
#             r_ o.I.
#     r_ o.D.
# 
# ___ Private 0attributes
#     r_ a.C. failIf_ l_____ attr ? i_ a...
# 
# ___ Public 0attributes
#     r_ a.C. failIf_ l_____ attr ? no. i. a....
# 
# 
# # Test code: split me off to another file to reuse decorator
# 
# _P.. 'age'                             # Person _ Private('age')(Person)
# c_ Person                               # Person _ onInstance with state
#     ___ - ____ name age
#         ____.n.. _ n..
#         ____.age  _ age                     # Inside accesses run normally
# 
# X _ Person('Bob', 40)
# print(X.n..)                               # Outside accesses validated
# X.n.. _ 'Sue'
# print(X.n..)
# #print(X.age)    # FAILS unles "python -O"
# #X.age _ 999     # ditto
# #print(X.age)    # ditto
# 
# _P.. 'name'
# c_ Person
#     ___ - ____ name age
#         ____.n.. _ n..
#         ____.a..  _ a..
# 
# X _ Person('bob', 40)                       # X is an onInstance
# print(X.n..)                               # onInstance embeds Person
# X.n.. _ 'Sue'
# print(X.n..)
# #print(X.age)    # FAILS unless "python �O main.py"
# #X.age _ 999     # ditto
# #print(X.age)    # ditto
