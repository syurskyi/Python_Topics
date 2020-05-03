c_ someClass(object
    y _ 20
    ___  -  
        x _ 10
        # self.y = 100

c _ someClass
print(c.y)
f _ someClass
print(f.y)
# f.y = 100
print(f.y)
f.__class__.y _ 100
print(f.y)
print(c.y)
