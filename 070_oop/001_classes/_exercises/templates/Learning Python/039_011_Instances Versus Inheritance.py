# c_ MetaOne ty..
#     ___ -n meta classname supers classdict  # Redefine type method
#         print('In MetaOne.new:', cl..
#         r_ ty__. -n m... c... s... cl...
# 
#     ___ toast ____
#         print('toast')
# 
# 
# c_ Super m.. _ M..  # Metaclass inherited by subs too
#     ___ spam ____  # MetaOne run twice for two classes
#         print('spam')
# 
# 
# c_ C S..  # Superclass: inheritance versus instance
#     ___ eggs ____  # Classes inherit from superclasses
#         print('eggs')  # But not from metclasses
# 
# 
# X = C()
# X.eggs()  # Inherited from C
# X.spam()  # Inherited from Super
# X.toast()  # Not inherited from metaclass
# 
