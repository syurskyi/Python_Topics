obj1 = ["Строка", (2, 3)]
obj2 = (1, 2)
f = open(r"file.txt", "wb")
pickle.dump(obj1, f)          # Сохраняем первый объект
pickle.dump(obj2, f)          # Сохраняем второй объект
f.close()