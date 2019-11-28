f = open(r"file.txt", "rb")
obj1 = pickle.load(f)        # Восстанавливаем первый объект
obj2 = pickle.load(f)        # Восстанавливаем второй объект
obj1, obj2
# (['Строка', (2, 3)], (1, 2))
f.close()


f = open(r"file.txt", "wb")
obj = ["Строка", (2, 3)]
pkl = pickle.Pickler(f)
pkl.dump(obj)
f.close()


f = open(r"file.txt", "rb")
obj = pickle.Unpickler(f).load()
obj
# ['Строка', (2, 3)]
f.close()


obj1 = [1, 2, 3, 4, 5]      # Список
obj2 = (6, 7, 8, 9, 10)     # Кортеж
pickle.dumps(obj1)
# b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04K\x05e.'
pickle.dumps(obj2)
# b'\x80\x03(K\x06K\x07K\x08K\tK\ntq\x00.'


pickle.loads(b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04K\x05e.')
# [1, 2, 3, 4, 5]
pickle.loads(b'\x80\x03(K\x06K\x07K\x08K\tK\ntq\x00.')
# (6, 7, 8, 9, 10)


import shelve                    # Подключаем модуль
db = shelve.open("db1")          # Открываем файл
db["obj1"] = [1, 2, 3, 4, 5]     # Сохраняем список
db["obj2"] = (6, 7, 8, 9, 10)    # Сохраняем кортеж
db["obj1"], db["obj2"]           # Вывод значений
# ([1, 2, 3, 4, 5], (6, 7, 8, 9, 10))
db.close()                       # Закрываем файл


db = shelve.open("db1")
db.keys(), db.values()
# (KeysView(<shelve.DbfilenameShelf object at 0x00FE81B0>),
#  ValuesView(<shelve.DbfilenameShelf object at 0x00FE81B0>))
list(db.keys()), list(db.values())
# (['obj1', 'obj2'], [[1, 2, 3, 4, 5], (6, 7, 8, 9, 10)])
db.items()
# ItemsView(<shelve.DbfilenameShelf object at 0x00FE81B0>)
list(db.items())
# [('obj1', [1, 2, 3, 4, 5]), ('obj2', (6, 7, 8, 9, 10))]
db.close()


db = shelve.open("db1")
len(db)            # Количество элементов
# 2
"obj1" in db
# True
del db["obj1"]     # Удаление элемента
"obj1" in db
# False
"obj1" not in db
# True
db.close()