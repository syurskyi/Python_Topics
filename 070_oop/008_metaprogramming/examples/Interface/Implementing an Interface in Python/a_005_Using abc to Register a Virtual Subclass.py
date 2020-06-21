# Using abc to Register a Virtual Subclass
# Once you've imported the abc module, you can directly register a virtual subclass by using the .register() metamethod.
# In the next example, you register the interface Double as a virtual base class of the built-in __float__ class:

class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""
    pass

Double.register(float)

# You can check out the effect of using .register():

issubclass(float, Double)
# True

isinstance(1.2345, Double)
# True

# By using the .register() meta method, you've successfully registered Double as a virtual subclass of float.
# Once you've registered Double, you can use it as class decorator to set the decorated class as a virtual subclass:

@Double.register
class Double64:
    """A 64-bit double-precision floating-point number."""
    pass

print(issubclass(Double64, Double))  # True

# The decorator register method helps you to create a hierarchy of custom virtual class inheritance.
