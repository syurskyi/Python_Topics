class Spam:
    def __init__(self):                   # No __repr__ or __str__
        self.data1 = "food"

X = Spam()
print(X)                                  # Default: class, address
# <__main__.Spam object at 0x00864818>          # Displays "instance" in Python 2.6

