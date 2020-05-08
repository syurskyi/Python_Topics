

c_ MyClass1(object):

    ___  -   a=0, b=1, c=2):
        self.a = a
        self.b = b
        self.c = c

    ___ getMax(self):
        return max([self.a, self.b, self.c])

    ___ getMin(self):
        return min([self.a, self.b, self.c])

    ___ getProduct(self):
        return self.a * self.b * self.c

    ___ getSum(self):
        return self.a + self.b + self.c

    ___ getMean(self):
        return self.getSum() / 3.0
