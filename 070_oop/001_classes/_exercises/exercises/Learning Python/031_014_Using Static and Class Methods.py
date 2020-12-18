# c_ Methods
#     ___ imeth ____ x           # Normal instance method: passed a self
#         print ____ ?
# 
#     ___ smeth x                 # Static: no instance passed
#         print(x)
# 
#     ___ cmeth ___ x             # Class: gets class, not instance
#         print ___ ?
# 
#     smeth = s... s..    # Make smeth a static method
#     cmeth = c... c..     # Make cmeth a class method
# 
# 
# 
# obj = ?               # Make an instance
# 
# ?.i.. 1                  # Normal method, call through instance
# # <__main__.Methods object...> 1     # Becomes imeth(obj, 1)
# 
# M__.i.. ? 2          # Normal method, call through class
# # <__main__.Methods object...> 2     # Instance passed explicitly
# 
# M__.s.. 3               # Static method, call through class
#                                   # No instance passed or expected
# 
# ?.s.. 4                   # Static method, call through instance
#                                   # Instance not passed
# 
# M__.c.. 5               # Class method, call through class
# # <class '__main__.Methods'> 5       # Becomes cmeth(Methods, 5)
# 
# ?.c.. 6                   # Class method, call through instance
# # <class '__main__.Methods'> 6       # Becomes cmeth(Methods, 6)
