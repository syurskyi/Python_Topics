class list(object):
    ___ __init__(self, arg):
        self.arg = [c for c in arg __ isinstance(c,int)]
    ___ even(self):
        return [n for n in self.arg __ n % 2 == 0]
    ___ odd(self):
        return [n for n in self.arg __ n % 2 != 0]
    ___ under(self,num):
        return [n for n in self.arg __ n < num]
    ___ over(self,num):
        return [n for n in self.arg __ n > num]
    ___ in_range(self,min,max):
        return [n for n in self.arg __ n >= min and n <= max]
