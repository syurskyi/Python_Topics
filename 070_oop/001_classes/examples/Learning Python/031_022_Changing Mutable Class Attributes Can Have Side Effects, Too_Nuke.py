class C:
    shared = []                 # Class attribute
    def __init__(self):
        self.perobj = []        # Instance attribute

x = C()                         # Two instances
y = C()                         # Implicitly share class attrs
y.shared, y.perobj

x.shared.append('spam')         # Impacts y's view too!
x.perobj.append('spam')         # Impacts x's data only
x.shared, x.perobj

y.shared, y.perobj              # y sees change made through x
C.shared                        # Stored on class and shared

x.shared.append('spam')    # Changes shared object attached to class in-place
x.shared = 'spam'          # Changed or creates instance attribute attached to x
