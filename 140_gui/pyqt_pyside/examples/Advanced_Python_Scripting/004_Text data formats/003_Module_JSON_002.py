import json

p = 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/004_Text data formats/file4.json'

x = [1, 2, 3, {1:3}]

json.dump(x, open(p, 'w'), indent=4)


y =json.load(open(p))

print(y)

