# c_ Singleton o..
# 
#     _instance _ N..
# 
#     ___ - name
#         ?  ?
# 
#     ___  -n ___ $
#         __ g.a. ___ "_i.." __ N.. o. ___ !_ ___._?. -c
#             ___._? _ o__. -n ___
#         r_ ___._?
# 
# 
# c_ Child S..
# 
#     ___ childmethod
#         p..
# 
# 
# c_ GrandChild C..
# 
#     ___ grandchildmethod
#         p..
# 
# 
# ___ main
#     # The __new__ method creates a new instance and returns it.
#     # The __init__ method initializes the instance.
#     s1 = S.. "Sam"
#     # The __new__ method does NOT create an instance and returns the first one.
#     # The __init__ method re-initializes the instance (the first one).
#     # The instance is the same, so the effects of the first __init__ are lost.
#     s2 = S.. "Tom"
#     # The __new__ method creates a new instance because it's a different class.
#     c1 = C.. "John"
#     c2 = C.. "Andy"
#     g1 = G.. "Bob"
#     print(s1.name, id(s1), s1)
#     print(s2.name, id(s2), s2)
#     print(c1.name, id(c1), c1)
#     print(c2.name, id(c2), c2)
#     print(g1.name, id(g1), g1)
#     print("s1 is s2?")
#     print(s1 is s2)
#     print("s1 is c1?")
#     print(s1 is c1)
#     print("c1 is c2?")
#     print(c1 is c2)
#     print("c1 is g1?")
#     print(c1 is g1)
# 
# 
# __ ______ __ _____
#     ?
