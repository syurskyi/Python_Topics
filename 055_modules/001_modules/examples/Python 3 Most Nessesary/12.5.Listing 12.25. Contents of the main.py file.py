# -*- coding: utf-8 -*-
from folder1.folder2 import module3 as m
print(m.var1)         # Значение из: Модуль folder1.folder2.module2
print(m.var2)         # Значение из: Модуль folder1.folder2.module2
print(m.var3)         # Значение из: Модуль folder1.module1
print(m.var4)         # Значение из: Модуль folder1.module1
input()


# -*- coding: utf-8 -*-
import module2       # Ошибка! Поиск модуля по абсолютному пути
var1 = "Значение из: {0}".format(module2.msg)
var2 = var3 = var4 = 0


from . import module2


import folder1.folder2.module2 as module2