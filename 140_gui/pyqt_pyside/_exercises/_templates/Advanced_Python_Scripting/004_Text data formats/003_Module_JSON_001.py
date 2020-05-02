_____ json

p _ '/home/sergei/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
    '004_Text data formats/file3.json'

x _ [1, 2, 3, {1:3}]

json.dump(x, open(p, 'w'))


y _json.load(open(p))

print(y)