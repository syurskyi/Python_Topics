import module1
#
print(module1.value)
#
# import pack1
#
# print(module1.__file__)
#
# print(module1.__package__)
#
# # print(module1.__path__)  Atribute path only for packages
#
# print(pack1.__package__)
#
# print(pack1.__path__)
#
# print(pack1.__file__)
#
# # import pack1_1 # No module name
#
# print('#' * 52 + ' import sys ')
# import sys
# print(sys.path)

# #######################################################################################

# print('#' * 52 + ' import pack1.pack1_1 ')
# import pack1.pack1_1
#
# import sys
# print(sys.modules)

# print('#' * 52 + ' check pack1 in globals')
# print('pack1' in globals())
#
# print('#' * 52 + ' check pack1.pack1_1 in globals')
# print('pack1.pack1_1' in globals())
# # print(pack1.pack1_1 in sys.modules)

# print('#' * 52 + ' from pack1 import pack1_1')
# from pack1 import pack1_1
# print('pack1_1' in globals())
# print(id(pack1_1) == id(sys.modules['pack1.pack1_1']))

# #######################################################################################

# print('#' * 52 + ' import pack1.pack1_1.module1_1a')
# import pack1.pack1_1.module1_1a
#
# import sys
# print('pack1' in sys.modules)
# print('pack1.pack1_1' in sys.modules)
# print('pack1.pack1_1.module1_1a' in sys.modules)
# print('pack1.pack1_1' in globals())
# print('pack1.pack1_1.module1_1a' in globals())
# print(pack1.pack1_1.module1_1a.value)

# #######################################################################################

# print('#' * 52 + ' import pack1.pack1_1')
# import pack1.pack1_1
# import sys
# print('pack1.pack1_1.module1_1a' in sys.modules)
# print('pack1.pack1_1.module1_1b' in sys.modules)
#
# print('pack1' in globals())
# print(pack1.pack1_1.__file__)
# # print(pack1.pack1_1.module1_1a.__file__) # no attribute
#
# import pack1.pack1_1.module1_1a
# print(pack1.pack1_1.module1_1a.__file__)
# print(globals())

# #######################################################################################

import pack1
