# -*- coding: utf-8 -*-
from module1 import *
from module2 import *
import module1, module2
print(s)                  # Выведет: "Значение из модуля module2"
print(module1.s)          # Выведет: "Значение из модуля module1"
print(module2.s)          # Выведет: "Значение из модуля module2"
input()