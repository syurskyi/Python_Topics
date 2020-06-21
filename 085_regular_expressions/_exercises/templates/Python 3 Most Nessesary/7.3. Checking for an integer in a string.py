# # -*- coding: utf-8 -*-
#
# _______ __                      # Подключаем модуль
# p = __.c.. _ 1? 2? 3? 4?  __.5? # 1.Starts with | 2. Match any digit; same as [0123456789]
#                                 # 3. One or more occurrences | 4. Ends with |5. Makes a period (dot) match any character, including a newline.
# __ ?.s.. ("245"):
#     print("Число")            # Выведет: Число
# ____
#     print("Не число")
# __ ?.s.. ("Строка245")
#     print("Число")
# ____
#     print("Не число")         # Выведет: Не число
# input()