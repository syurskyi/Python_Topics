import json

a = 123
a = [1,2,'value','name']

filePath = 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/004_Text data formats/picFile2.json'
a = [1,2,3,4,5]
a = {'name':'Nik', 'value':1234, 'content':['obj1','obj2','obj3']}
json.dump(a, open(filePath, 'w'), indent=4)

b = json.load(open(filePath, 'r'))



class serializer(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, myClass):
            return {obj.name:obj.x}
        return json.JSONEncoder.default(self, obj)

class myClass():
    def __init__(self):
        self.name = 'someName'
        self.x = 100


a = myClass()
b = {'cls':a}
json.dump(b, open(filePath, 'w'), indent=4, cls=serializer)

b = json.load(open(filePath, 'r'))

print(b)