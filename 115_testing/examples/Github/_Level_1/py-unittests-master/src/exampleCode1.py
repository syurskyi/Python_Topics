

class MyClass1(object):

    def __init__(self, a=0, b=1, c=2):
        self.a = a
        self.b = b
        self.c = c

    def getMax(self):
        return max([self.a, self.b, self.c])

    def getMin(self):
        return min([self.a, self.b, self.c])

    def getProduct(self):
        return self.a * self.b * self.c

    def getSum(self):
        return self.a + self.b + self.c

    def getMean(self):
        return self.getSum() / 3.0
