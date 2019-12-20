# -*- coding: utf-8 -*-

import random # Подключаем модуль random
random.choice(["s", "t", "r"]) # Список
's'


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.sample(arr, 2))
# [7, 10]
print(arr)                         # Сам список не изменяется
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]