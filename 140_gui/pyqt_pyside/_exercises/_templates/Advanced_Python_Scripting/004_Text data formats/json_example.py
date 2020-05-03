_____ json

a _ 123
a _ [1,2,'value','name']

filePath _ 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/004_Text data formats//picFile.json'
a _ [1,2,3,4,5]
a _ {'name':'Nik', 'value':1234, 'content':['obj1','obj2','obj3']}
json.dump(a, o..(filePath, 'w'), indent_4)

b _ json.l..(o..(filePath, 'r'))



c_ serializer(json.JSONEncoder
    ___ default , obj
        __ isinstance(obj, myClass
            r_ {obj.name:obj.x}
        r_ json.JSONEncoder.default , obj)

c_ myClass(
    ___  -  
        name _ 'someName'
        x _ 100


a _ myClass
b _ {'cls':a}
json.dump(b, o..(filePath, 'w'), indent_4, cls_serializer)

b _ json.l..(o..(filePath, 'r'))

print(b)