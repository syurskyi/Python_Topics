class Wrapper:
    def __init__(self, object):
        self.wrapped = object                    # Save object

    def __getattr__(self, attrname):
        print('Trace:', attrname)                # Trace fetch
        return getattr(self.wrapped, attrname)   # Delegate fetch

# NOTE: in the following, use list(x.keys()) for Python 3.X
# (list() was not used in the first printing of the book

# from trace import Wrapper
x = Wrapper([1, 2, 3])                         # Wrap a list
x.append(4)                                  # Delegate to list method
#
print(x.wrapped)                                   # Print my member
#
x = Wrapper({'a': 1, 'b': 2})
print(list(x.keys()))                         # Delegate to dictionary method

