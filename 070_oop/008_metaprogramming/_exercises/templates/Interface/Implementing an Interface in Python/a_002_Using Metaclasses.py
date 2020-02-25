# # Using Metaclasses
# # Ideally, you would want issubclass(EmlParser, InformalParserInterface to r_ False when the implementing
# # class doesn't define all of the interface's abstract methods. To do this, you'll create a metaclass called ParserMeta.
# # You'll be overriding two dunder methods:
# #
# # .__instancecheck__()
# # .__subclasscheck__()
# # In the code block below, you create a class called UpdatedInformalParserInterface that builds from the ParserMeta
# # metaclass:
#
# c_ ParserMeta ty..
#     """A Parser metaclass that will be used for parser class creation.
#     """
#     ___ -ins... ___ instance
#         r_ ___. -su.. ty.. ?
#
#     ___ -su.. ___ subclass
#         r_ h.. ? 'lo...') an.
#                 ca.. ?.l_d_s.) an.
#                 h.. ?, 'ex..') an.
#                 ca.. ?.ex..
#
# c_ UpdatedInformalParserInterface m..
#     """This interface is used for concrete classes to inherit from.
#     There is no need to define the ParserMeta methods as any class
#     as they are implicitly made available via .__subclasscheck__().
#     """
#     p..
#
# # Now that ParserMeta and UpdatedInformalParserInterface have been created, you can create your concrete
# # implementations.
# # First, create a new class for parsing PDFs called PdfParserNew:
#
#
# c_ PdfParserNew
#     """Extract text from a PDF."""
#     ___ load_data_source  path st. file_name st.) __ st.
#         """Overrides UpdatedInformalParserInterface.load_data_source()"""
#         p..
#
#     ___ extract_text full_file_path st. __ di..
#         """Overrides UpdatedInformalParserInterface.extract_text()"""
#         p..
#
#
# # Here, PdfParserNew overrides .load_data_source() and .extract_text(), so issubclass(PdfParserNew,
# # UpdatedInformalParserInterface) should r_ True.
# # In this next code block, you have a new implementation of the email parser called EmlParserNew:
#
#
# c_ EmlParserNew
#     """Extract text from an email."""
#     ___ load_data_source  path st. file_name st. __ st.
#         """Overrides UpdatedInformalParserInterface.load_data_source()"""
#         p..
#
#     ___ extract_text_from_email  full_file_path st. __ di..
#         """A method defined only in EmlParser.
#         Does not override UpdatedInformalParserInterface.extract_text()
#         """
#         p..
#
#
# # Here, you have a metaclass that's used to create UpdatedInformalParserInterface. By using a metaclass,
# # you don't need to explicitly define the subclasses. Instead, the subclass must define the required methods.
# # If it doesn't, then issubclass(EmlParserNew, UpdatedInformalParserInterface) will r_ False.
# #
# # Running issubclass() on your concrete classes will produce the following:
#
# iss..(P.. U..
# # True
#
# iss..(E.. U..
# # False
#
# # As expected, EmlParserNew is not a subclass of UpdatedInformalParserInterface since .extract_text() wasn't defined
# # in EmlParserNew.
# #
# # Now, let's have a look at the MRO:
#
# print(P__. -m
# # (<class '__main__.PdfParserNew'>, <class 'object'>)
#
# # As you can see, UpdatedInformalParserInterface is a superclass of PdfParserNew, but it doesn't appear in the MRO.
# # This unusual behavior is caused by the fact that UpdatedInformalParserInterface is a virtual base
# # class of PdfParserNew.
