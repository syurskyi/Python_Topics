# Using Metaclasses
# Ideally, you would want issubclass(EmlParser, InformalParserInterface to return False when the implementing
# class doesn't define all of the interface's abstract methods. To do this, you'll create a metaclass called ParserMeta.
# You'll be overriding two dunder methods:
#
# .__instancecheck__()
# .__subclasscheck__()
# In the code block below, you create a class called UpdatedInformalParserInterface that builds from the ParserMeta
# metaclass:

class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))

class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass

# Now that ParserMeta and UpdatedInformalParserInterface have been created, you can create your concrete
# implementations.
# First, create a new class for parsing PDFs called PdfParserNew:


class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides UpdatedInformalParserInterface.extract_text()"""
        pass


# Here, PdfParserNew overrides .load_data_source() and .extract_text(), so issubclass(PdfParserNew,
# UpdatedInformalParserInterface) should return True.
# In this next code block, you have a new implementation of the email parser called EmlParserNew:


class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override UpdatedInformalParserInterface.extract_text()
        """
        pass


# Here, you have a metaclass that's used to create UpdatedInformalParserInterface. By using a metaclass,
# you don't need to explicitly define the subclasses. Instead, the subclass must define the required methods.
# If it doesn't, then issubclass(EmlParserNew, UpdatedInformalParserInterface) will return False.
#
# Running issubclass() on your concrete classes will produce the following:

issubclass(PdfParserNew, UpdatedInformalParserInterface)
# True

issubclass(EmlParserNew, UpdatedInformalParserInterface)
# False

# As expected, EmlParserNew is not a subclass of UpdatedInformalParserInterface since .extract_text() wasn't defined
# in EmlParserNew.
#
# Now, let's have a look at the MRO:

print(PdfParserNew.__mro__)
# (<class '__main__.PdfParserNew'>, <class 'object'>)

# As you can see, UpdatedInformalParserInterface is a superclass of PdfParserNew, but it doesn't appear in the MRO.
# This unusual behavior is caused by the fact that UpdatedInformalParserInterface is a virtual base
# class of PdfParserNew.
