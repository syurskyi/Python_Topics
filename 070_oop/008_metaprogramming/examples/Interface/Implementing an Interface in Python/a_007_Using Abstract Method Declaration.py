# Using Abstract Method Declaration
# An abstract method is a method that's declared by the Python interface, but it may not have a useful implementation.
# The abstract method must be overridden by the concrete class that implements the interface in question.
#
# To create abstract methods in Python, you add the @abc.abstractmethod decorator to the interface's methods.
# In the next example, you update the FormalParserInterface to include the abstract methods .load_data_source()
# and .extract_text():

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)

    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError

class PdfParserNew(FormalParserInterface):
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew(FormalParserInterface):
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

# In the above example, you've finally created a formal interface that will raise errors when the abstract
# methods aren't overridden. The PdfParserNew instance, pdf_parser, won't raise any errors, as PdfParserNew
# is correctly overriding the FormalParserInterface abstract methods. However, EmlParserNew will raise an error:


pdf_parser = PdfParserNew()
eml_parser = EmlParserNew()
# Traceback (most recent call last):
#   File "real_python_interfaces.py", line 53, in <module>
#     eml_interface = EmlParserNew()
# TypeError: Can't instantiate abstract class EmlParserNew with abstract methods extract_text

# As you can see, the traceback message tells you that you haven't overridden all the abstract methods.
# This is the behavior you expect when building a formal Python interface.


# Conclusion
# Python offers great flexibility when you're creating interfaces. An informal Python interface is useful
# for small projects where you're less likely to get confused as to what the return types of the methods are.
# As a project grows, the need for a formal Python interface becomes more important as it becomes more difficult
# to infer return types. This ensures that the concrete class, which implements the interface, overwrites
# the abstract methods.
#
# Now you can:
#
# Understand how interfaces work and the caveats of creating a Python interface
# Understand the usefulness of interfaces in a dynamic language like Python
# Implement formal and informal interfaces in Python
# Compare Python interfaces to those in languages like Java, C++, and Go
# Now that you've become familiar with how to create a Python interface, add a Python interface to
# your next project to see its usefulness in action!
