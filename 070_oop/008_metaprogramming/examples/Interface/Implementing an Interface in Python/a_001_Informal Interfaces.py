# In certain circumstances, you may not need the strict rules of a formal Python interface. Python's dynamic nature
# allows you to implement an informal interface. An informal Python interface is a class that defines methods that
# can be overridden, but there's no strict enforcement.
#
# In the following example, you will take the perspective of a data engineer who needs to extract text from various
# different unstructured file types, like PDFs and emails. You will create an informal interface that defines the methods
# that will be in both the PdfParser and EmlParser concrete classes:

class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass

# InformalParserInterface defines the two methods .load_data_source() and .extract_text(). These methods are defined
# but not implemented. The implementation will occur once you create concrete classes that inherit from
# InformalParserInterface.
# you define two classes that implement the InformalParserInterface. To use your interface, you must create
# a concrete class. A concrete class is a subclass of the interface that provides an implementation of the interface's
# methods. You'll create two concrete classes to implement your interface. The first is PdfParser, which you'll use
# to parse the text from PDF files:


class PdfParser(InformalParserInterface):
    """Extract text from a PDF"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass


# The concrete implementation of InformalParserInterface now allows you to extract text from PDF files.
# The second concrete class is EmlParser, which you'll use to parse the text from emails:

class EmlParser(InformalParserInterface):
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass

# The concrete implementation of InformalParserInterface now allows you to extract text from email files.
#
# So far, you've defined two concrete implementations of the InformalPythonInterface. However, note that EmlParser
# fails to properly define .extract_text(). If you were to check whether EmlParser implements InformalParserInterface,
# then you'd get the following result:

# Check if both PdfParser and EmlParser implement InformalParserInterface
issubclass(PdfParser, InformalParserInterface)
# True

issubclass(EmlParser, InformalParserInterface)
# True


# Now check the method resolution order (MRO) of PdfParser and EmlParser. This tells you the superclasses of
# the class in question, as well as the order in which they're searched for executing a method. You can view
# a class's MRO by using the dunder method cls.__mro__:

print(PdfParser.__mro__)
# (__main__.PdfParser, __main__.InformalParserInterface, object)

print(EmlParser.__mro__)
# (__main__.EmlParser, __main__.InformalParserInterface, object)

# Such informal interfaces are fine for small projects where only a few developers are working on the source code.
# However, as projects get larger and teams grow, this could lead to developers spending countless hours looking for
# hard-to-find logic errors in the codebase!
