# -*- coding: utf-8 -*-
#
keys = ["a", "b"]         # Список с ключами
values = [1, 2]           # Список со значениями
print({k: v for (k, v) in zip(keys, values)})
# # {'a': 1, 'b': 2}
print({k: 0 for k in keys})
# # {'a': 0, 'b': 0}
#
#
d = {"a": 1, "b": 2, "c": 3, "d": 4 }
print({k: v for (k, v) in d.items() if v % 2 == 0})
# # {'b': 2, 'd': 4}