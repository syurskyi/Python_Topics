c_ someClass(object
    count = 0
    ___  -
        __class__.count += 1


c = someClass()
print(c.count)
f = someClass()
print(f.count)
