# Note that the above syntax is for python 3 super function. If you are on python 2.x versions,
# then it's slightly different and you will have to do the following changes:
#
#
# c_ Person o..
# ...
#         super(Student, self).__init__(student_name, student_age)
# The first change is to have object as the base class for Person. Its required to use the super function
# in Python 2.x versions. Otherwise, you will get the following error.
#
#
# Traceback (most recent call last):
#   File "super_example.py", line 40, in <module>
#     student1 = Student("Max", 22, "102")
#   File "super_example.py", line 25, in __init__
#     super(Student, self).__init__(student_name, student_age)
# TypeError: must be type, not classobj
# The second change in the syntax of the super function itself.
#
# As you can see that python 3 super function is a lot easier to use and the syntax is also clean looking.

