import json
import vector

p = 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/004_Text data formats/vector.json'

x = vector.vector(1, 2, 3)


class mySerialize(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, vector.vector):
            d = o.__dict__
            d.update({'classType': o.__class__.__name__})
            return d
        # return json.JSONEncoder.default(self, o)
        return super(mySerialize, self).default(o)
#
json.dump(x, open(p, 'w'), indent=4, cls=mySerialize)
#
#
y =json.load(open(p))
#
print(y)
