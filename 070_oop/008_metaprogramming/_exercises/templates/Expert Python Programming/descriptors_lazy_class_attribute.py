# """
# "Descriptors" section example of descriptor that will allows to
# convert a method of a class into lazily evaluated attribute
# that will be called only once.
# 
# """
# 
# 
# c_ lazy_class_attribute o..
#     ___ - function
#         fget _ ?
# 
#     ___ -g obj cls
#         value _ fget ? o. ?
#         # note: storing in class object not its instance
#         #       no matter if its a class-level or
#         #       instance-level access
#         se... ___ fg__. -n v..
#         r_ v..
# 
# 
# c_ MyComplexClass
# 
#     ??
#     ___ evaluated_only_once
#         print("Evaluation of a method!")
#         return su. x ** 2 ___ ? __ ra.. 200
# 
# 
# __ _______ __ _______
#     instance = ..
# 
#     print("First access to attribute at instance level")
#     print("instance.evaluated_only_once =",
#           ?.e..
#           '\n')
# 
#     print("Next access to attribute at instance level")
#     print("instance.evaluated_only_once =",
#           ?.e...
#           '\n')
# 
#     print("Access to attribute at class level")
#     print("MyComplexClass.evaluated_only_once =",
#           M___.e...
#           '\n')
# 
#     print("Access to attribute from completely new instance")
#     print("MyComplexClass().evaluated_only_once =",
#           M___ .e..
#           '\n')
