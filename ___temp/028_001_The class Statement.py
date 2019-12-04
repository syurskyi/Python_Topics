# c_ SharedData
#     spam _ 42          # Generates a class data attribute
#
# x = ?     # Make two instances
# y = ?
# print('#' * 23 + ' They inherit and share spam')
# print(x.s. y.s.)         # They inherit and share 'spam'
#
# ?.s. = 99
# print(x.spam, y.spam, SharedData.spam)
#
# x.s.. = 88
# print(x.spam, y.spam, SharedData.spam)
#
#
# c_ MixedNames                            # Define class
#     data = 'spam'                            # Assign class attr
#
#     ___ - ____ value              # Assign method name
#         self.data = v..                   # Assign instance attr
#
#     ___ display ____
#         # print('#' * 23 + '  Instance attr, class attr')
#         print(self.d.. M__.d..    # Instance attr, class attr
#
# x = MixedNames(1)          # Make two instance objects
# y = MixedNames(2)          # Each has its own data
# print('#' * 23 + '  self.data differs, MixedNames.data is the same')
# x.display(); y.display()   # self.data differs, MixedNames.data is the same
#
#
