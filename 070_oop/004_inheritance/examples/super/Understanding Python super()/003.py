class A(object):
    def __init__(self, i):
        self.i = i
    def run(self, value):
        return self.i * value

class B(A):
    def __init__(self, i, j):
        super(B, self).__init__(i)
        self.j = j
    def run(self, value):
        return super(B, self).run(value) + self.j

class Logger(object):
    def __init__(self, name):
        self.name = name
    def run_logged(self, value):
        print("Running", self.name, "with info", self.info())
        return self.run(value)

class BLogged(B, Logger):
    def __init__(self, i, j):
        B.__init__(self, i, j)
        Logger.__init__("B")
    def info(self):
        return 42
