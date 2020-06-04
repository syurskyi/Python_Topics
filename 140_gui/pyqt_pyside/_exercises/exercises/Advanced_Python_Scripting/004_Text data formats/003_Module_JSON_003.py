_____ json
_____ vector

p _ 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/004_Text data formats/vector.json'

x _ vector.vector(1, 2, 3)


c_ mySerialize(json.JSONEncoder
    ___ default , o
        __ isinstance(o, vector.vector
            d _ o.__dict__
            d.update({'classType': o.__class__.__name__})
            r_ d
        # return json.JSONEncoder.default(self, o)
        r_ s__(mySerialize, self).default(o)
#
json.dump(x, o..(p, 'w'), indent_4, cls_mySerialize)
#
#
y _json.l..(o..(p))
#
print(y)
