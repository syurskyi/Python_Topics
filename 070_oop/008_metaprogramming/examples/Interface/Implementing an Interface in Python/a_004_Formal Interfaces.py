# Formal Interfaces
# Informal interfaces can be useful for projects with a small code base and a limited number of programmers.
# However, informal interfaces would be the wrong approach for larger applications. In order to create
# a formal Python interface, you'll need a few more tools from Python's abc module.
#
# Using abc.ABCMeta
# To enforce the subclass instantiation of abstract methods, you'll utilize Python's builtin ABCMeta
# from the abc module. Going back to your UpdatedInformalParserInterface interface, you created your own metaclass,
# ParserMeta, with the overridden dunder methods .__instancecheck__() and .__subclasscheck__().
#
# Rather than create your own metaclass, you'll use abc.ABCMeta as the metaclass.
# Then, you'll overwrite .__subclasshook__() in place of .__instancecheck__() and .__subclasscheck__(),
# as it creates a more reliable implementation of these dunder methods.
#
# Using .__subclasshook__()
# Here's the implementation of FormalParserInterface using abc.ABCMeta as your metaclass:

# Using .__subclasshook__()
# Here's the implementation of FormalParserInterface using abc.ABCMeta as your metaclass:

import abc

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))

class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

# If you run issubclass() on PdfParserNew and EmlParserNew, then issubclass() will return True and False, respectively.

