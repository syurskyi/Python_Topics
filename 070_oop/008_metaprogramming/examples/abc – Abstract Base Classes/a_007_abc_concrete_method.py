# abc_concrete_method.py

# Concrete Methods in ABCs
# Although a concrete class must provide implementations of all abstract methods, the abstract base class can
# also provide implementations that can be invoked via super(). This allows common logic to be reused by placing it in
# the base class, but forces subclasses to provide an overriding method with (potentially) custom logic.

import abc
import io



class ABCWithConcreteImplementation(abc.ABC):

    @abc.abstractmethod
    def retrieve_values(self, input):
        print('base class reading data')
        return input.read()


class ConcreteOverride(ABCWithConcreteImplementation):

    def retrieve_values(self, input):
        base_data = super(ConcreteOverride,
                          self).retrieve_values(input)
        print('subclass sorting data')
        response = sorted(base_data.splitlines())
        return response


input = io.StringIO("""line one
line two
line three
""")

reader = ConcreteOverride()
print(reader.retrieve_values(input))
print()

# Since ABCWithConcreteImplementation() is an abstract base class, it is not possible to instantiate it
# to use it directly. Subclasses must provide an override for retrieve_values(), and in this case the concrete class
# sorts the data before returning it.

# $ python3 abc_concrete_method.py
#
# base class reading data
# subclass sorting data
# ['line one', 'line three', 'line two']
