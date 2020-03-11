class Farm(object):
   def __init__(self): pass

class Barn(Farm):
   def __init__(self):
       super(Barn, self).__init__()
