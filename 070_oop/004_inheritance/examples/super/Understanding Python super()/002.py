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
