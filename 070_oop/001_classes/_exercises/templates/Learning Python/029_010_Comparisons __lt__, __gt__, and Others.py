
class C:
    data = 'spam'
    def __gt__(self, other):               # 3.0 and 2.6 version
        return self.data > other
    def __lt__(self, other):
        return self.data < other

X = C()
print('#' * 23 + ' True  (runs __gt__)')
print(X > 'ham')         # True  (runs __gt__)
print('#' * 23 + ' False (runs __lt__)')
print(X < 'ham')         # False (runs __lt__)

