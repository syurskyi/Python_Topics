def __getattr__(self, name):        # On undefined attribute fetch [obj.name]
    pass


def __getattribute__(self, name):   # On all attribute fetch [obj.name]
    pass

def __setattr__(self, name, value): # On all attribute assignment [obj.name=value]
    pass


def __delattr__(self, name):        # On all attribute deletion [del obj.name]
    pass


class Catcher:
    def __getattr__(self, name):
        print('Get:', name)

    def __setattr__(self, name, value):
        print('Set:', name, value)


X = Catcher()
X.job                               # Prints "Get: job"
X.pay                               # Prints "Get: pay"
X.pay = 99                          # Prints "Set: pay 99"


class Wrapper:
    def __init__(self, object):
        self.wrapped = object                    # Save object

    def __getattr__(self, attrname):
        print('Trace:', attrname)                # Trace fetch
        return getattr(self.wrapped, attrname)   # Delegate fetch

    def __getattribute__(self, name):
        x = self.other                                # LOOPS!

    def __getattribute__(self, name):
        x = object.__getattribute__(self, 'other')    # Force higher to avoid me

    def __setattr__(self, name, value):
        self.other = value                            # LOOPS!

    def __setattr__(self, name, value):
        self.__dict__['other'] = value                # Use atttr dict to avoid me

    def __setattr__(self, name, value):
        object.__setattr__(self, 'other', value)      # Force higher to avoid me

    def __getattribute__(self, name):
        x = self.__dict__['other']                    # LOOPS!

