class someClass(object):
    count = 0
    def __init__(self):
        self.__class__.count += 1


c = someClass()
print(c.count)
f = someClass()
print(f.count)
