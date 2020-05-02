c_ someClass(object
    y = 20
    ___  -  
        x = 10
        # self.y = 100

c = someClass()
print(c.y)
f = someClass()
print(f.y)
# f.y = 100
print(f.y)
f.__class__.y = 100
print(f.y)
print(c.y)
