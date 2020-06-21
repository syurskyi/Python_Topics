# -*- coding: utf-8 -*-
from folder1.folder2 import *
print(module2.msg)         # Выведет: Модуль folder1.folder2.module2
print(module3.msg)         # Выведет: Модуль folder1.folder2.module3
input()


from .module import *


from ..module import *


from ...module import *


from .. import module