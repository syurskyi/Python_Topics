# File lister.py
# Collect all three listers in one module for convenience

# NOTE: the following code had a typo in the book, fixes here
# ("retubrn" instead of "return")

### File: lister.py

class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of
    instances via inheritance of __str__, coded here; displays
    instance attrs only; self is the instance of lowest class;
    uses __X names to avoid clashing with client's attrs
    """
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                           self.__class__.__name__,         # My class's name
                           id(self),                        # My address
                           self.__attrnames())              # name=value list

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):                  # Instance attr dict
            result += '\tname %s=%s\n' % (attr, self.__dict__ [attr])
        return result



