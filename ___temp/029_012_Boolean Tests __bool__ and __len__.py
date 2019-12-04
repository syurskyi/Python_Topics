#
class Truth:
   def __bool__(self): return True

X = Truth()
if X: print('yes!')

class Truth:
   def __bool__(self): return False

X = Truth()
print(bool(X))

class Truth:
   def __len__(self): return 0
#
X = Truth()
if not X: print('no!')

class Truth:
   def __bool__(self): return True            # 3.0 tries __bool__ first
   def __len__(self): return 0                # 2.6 tries __len__ first

X = Truth()
if X: print('yes!')

class Truth:
    pass

X = Truth()
bool(X)

class C:
    def __bool__(self):
        print('in bool')
        return False

X = C()
bool(X)

# in bool

if X: print(99)

# in bool

class C:
    def __bool__(self):
        print('in bool')
        return False

X = C()
bool(X)

if X: print(99)

class C:
    def __nonzero__(self):
        print('in nonzero')
        return False

X = C()
bool(X)
# in nonzero

if X: print(99)

# in nonzero
