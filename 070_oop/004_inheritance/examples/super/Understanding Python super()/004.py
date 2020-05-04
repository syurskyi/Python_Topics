class A(object):
    def __init__(self, i, **kwargs):
        super(A, self).__init__(**kwargs)
        self.i = i
    def run(self, value):
        return self.i * value

class B(A):
    def __init__(self, j, **kwargs):
        super(B, self).__init__(**kwargs)
        self.j = j
    def run(self, value):
        return super(B, self).run(value) + self.j

class Logger(object):
    def __init__(self, name, **kwargs):
        super(Logger,self).__init__(**kwargs)
        self.name = name
    def run_logged(self, value):
        print("Running", self.name, "with info", self.info())
        return self.run(value)

class BLogged(B, Logger):
    def __init__(self, **kwargs):
        super(BLogged, self).__init__(name="B", **kwargs)
    def info(self):
        return 42

b = BLogged(i=3, j=4)
print(b)
