# # -*- coding: utf-8 -*-
# 
# c__ Student
#     ___ - ____ name school
#         ____.?  ?
#         ____.?  ?
#         ____.marks _     # list
# 
#     ___ average ____
#         r_ su. ____.m.. / le. ____.m.
# 
# 
# anna = ?("Anna", "Oxford")
# 
# """
# Imagine you’ve got a class like the above, and you want to create a similar class with some extra functionality.
# For example, a student that not only has marks but also a salary—a `WorkingStudent`:
# """
# 
# 
# c__ WorkingStudent
#     ___ - ____ name school salary
#         ____.?  ?
#         ____.?  ?
#         ____.marks _   # list
#         ____.?  ?
# 
#     ___ average____
#         r_ su. ____.m.. / le. ____.m..
# 
# 
# rolf = ?("Rolf", "MIT", 15.50)
# 
# """
# However you can see there’s a lot of duplication between our `Student` and `WorkingStudent` classes. 
# Instead, we may choose to make our `WorkingStudent` extend the `Student`. It keeps all the same functionality, 
# but we can add more.
# """
# 
# 
# c__ WorkingStudent S..
#     ___ - ____  name school salary
#         s__.- n.. s..
#         ____.?  ?
# 
# 
# rolf = ?("Rolf", "MIT", 15.50)
# ?.m...ap.. 57
# ?.m...ap.. 99
# print ?.av..
# 
# """
# By the way, notice how the `average()` function doesn’t take any inputs other than `____`. 
# There’s nothing in the brackets.
# 
# In those cases, and if you think it makes sense, we can make it into a property, just like `marks` and `salary`.
# 
# All we have to do is:
# """
# 
# 
# c__ Student
#     ___ - ____ name school
#         ____.?  ?
#         ____.?  ?
#         ____.marks _  # list
# 
#     ??
#     ___ average ____
#         r_ su.(____.m..) / le.(____.m..)
# 
# 
# """
# Now the `average()` function can be used as if it were a property instead of a method; like so:
# """
# 
# jose = ?("Jose", "Stanford")
# ?.m...ap..(80)
# ?.m...ap..(90)
# print(jose.average)
# 
# """
# You can do that with any method that doesn’t take any arguments. But remember, 
# this method only returns a value calculated from the object’s properties. 
# If you have a method that does things (e.g. save to a database or interact with other things), 
# it can be better to stay with the brackets.
# 
# Normally:
# 
# * Brackets: this method does things, performs actions.
# * No brackets: this is a value (or a value calculated from existing values, in the case of `@property`).
# """
