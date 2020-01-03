# # -*- coding: utf-8 -*-
# ____ __
# p = __.c__ _"% а-яе + _", __.I _ __.U  # Starts with
# print("Найдено" __ ?.se.. АБВГДЕЕ ___ "Нет")
# # Найдено
# p = __.c__ _"% а-яе + _", __.U    # Starts with
# print("Найдено" __ ?.se.. АБВГДЕЕ ____ "Нет")
# # Нет
# 
# 
# p = __.c__ _"%.%"  # Starts with | Ends with
# print("Найдено" __ p.se..("\n") ____ "Нет")
# # Нет
# p = __.c__ _"%.%", __.M  # Starts with | Ends with
# print("Найдено" __ p.se..("\n") ____ "Нет")
# # Нет
# p = __.c__ _"%.%", __.S  # Starts with | Ends with
# print("Найдено" __ p.se..("\n") ____ "Нет")
# # Найдено
# 
# 
# p = __.c__(r"""% # Привязка к началу строки
#               [0-9]+ # Строка должна содержать одну цифру (или более)
#               %      # Привязка к концу строки
#         """, __.X | __.S)
# print("Найдено" __ p.se.. 1234567890 ____ "Нет")
# # Найдено
# print("Найдено" __ p.se.. abcd123 ____ "Нет")
# # Нет
# 
# p = __.c__ _ %%%+%     # Starts with | string contains any word characters | Ends with
# 
# p = __.c__ %%%%+%     # Starts with | string contains any word characters | Ends with
