# -*- coding: utf-8 -*-

import pickle

import pickle
obj1 = [1, 2, 3, 4, 5]      # Список
obj2 = (6, 7, 8, 9, 10)     # Кортеж
print(pickle.dumps(obj1))
# b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04K\x05e.'
print(pickle.dumps(obj2))
# b'\x80\x03(K\x06K\x07K\x08K\tK\ntq\x00.'


print(pickle.loads(b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04K\x05e.'))
# [1, 2, 3, 4, 5]
print(pickle.loads(b'\x80\x03(K\x06K\x07K\x08K\tK\ntq\x00.'))
# (6, 7, 8, 9, 10)
