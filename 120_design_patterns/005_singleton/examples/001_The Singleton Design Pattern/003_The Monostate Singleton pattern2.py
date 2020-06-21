class Borg:
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b' : ", b)  ## b and b1 are distinct objects
print("Borg Object 'b1 ", b1)
print("Borg Object 'b' ", b.__dict__) ## b and b1 share same state
print("Borg Object 'b1' ", b1.__dict__)