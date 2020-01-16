# Note: all the code in this chapter is abstract -- it won't run as is


class C2:                       # Make class objects (ovals)
    pass
class C3:
    pass
class C1(C2, C3):               # Linked to superclasses
    pass

I1 = C1()                          # Make instance objects (rectangles)
I2 = C1()                          # Linked to their classes

# C2 and C3 must exist in the following

class C1(C2, C3):                # Make and link class C1
    def setname(self, who):      # Assign name: C1.setname
        self.name = who          # Self is either I1 or I2

I1 = C1()                        # Make two instances
I2 = C1()
I1.setname('bob')                # Sets I1.name to bob
I2.setname('mel')                # Sets I2.name to mel
print(I1.name)                   # Prints bob
print(I2.name)

class C1(C2, C3):
    def __init__(self, who):     # Set name when constructed
        self.name = who          # Self is either I1 or I2

I1 = C1('bob')                   # Sets I1.name to bob
I2 = C1('mel')                   # Sets I2.name to mel
print(I1.name)                   # Prints bob