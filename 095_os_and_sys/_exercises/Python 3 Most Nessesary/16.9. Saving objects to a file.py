import pickle
f = open(r"file.txt", "wb")
obj = ["Строка", (2, 3)]
pickle.dump(obj, f)
f.close()


f = open(r"file.txt", "rb")
obj = pickle.load(f)
obj
# ['Строка', (2, 3)]
f.close()