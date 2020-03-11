import pickle

p = '/Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
    '004_Text data formats/file2.txt'

x = 123

pickle.dump(x, open(p, 'wb'))

f = open('file2.txt', 'rb')
y = pickle.load(f)
print(y)