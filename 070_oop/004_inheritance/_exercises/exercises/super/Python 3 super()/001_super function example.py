# # At first, just look at the following code we used in our Python Inheritance tutorial. In that example code,
# # the superclass was Person and the subclass was Student. So the code is shown below.
#
# c_ Person
#     # initializing the variables
#     name _ ""
#     age _ 0
#
#     # defining constructor
#     ___ - person_name person_age
#         _n.. _ ?
#         _a.. _ ?
#
#         # defining class methods
#
#     ___ show_name
#         print _?
#
#     ___ show_age
#         print _?
#
#
# # # definition of subclass starts here
#
# c_ Student P..
#     studentId _ ""
#
#     ___ - student_name student_age student_id
#         ?. -  ? ?
#         _? _ ?
#
#     ___ get_id
#         r_ _s..  # returns the value of student id
#
#
# # # end of subclass definition
# #
# #
# # # Create an object of the superclass
# person1 _ P.. "Richard", 23
#
# # # call member methods of the objects
# ?.s_a..
#
# # # Create an object of the subclass
# student1 _ S.. "Max", 22, "102"
#
# print _1.g_i.
# _1.s_n..
#
# # In the above example, we have called parent class function as:
#
# # Person.__init__(self, student_name, student_age)
# # We can replace this with python super function call as below.
# #
# #
# # super().__init__(student_name, student_age)
# # The output will remain the same in both the cases, as shown in the below image.
#
