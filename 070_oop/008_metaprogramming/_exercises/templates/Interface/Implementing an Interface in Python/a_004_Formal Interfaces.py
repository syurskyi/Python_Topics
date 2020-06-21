# # Formal Interfaces
# # Informal interfaces can be useful for projects with a small code base and a limited number of programmers.
# # However, informal interfaces would be the wrong approach for larger applications. In order to create
# # a formal Python interface, you'll need a few more tools from Python's abc module.
# #
# # Using abc.ABCMeta
# # To enforce the subclass instantiation of abstract methods, you'll utilize Python's builtin ABCMeta
# # from the abc module. Going back to your UpdatedInformalParserInterface interface, you created your own metaclass,
# # ParserMeta, with the overridden dunder methods .__instancecheck__() and .__subclasscheck__().
# #
# # Rather than create your own metaclass, you'll use abc.ABCMeta as the metaclass.
# # Then, you'll overwrite .__subclasshook__() in place of .__instancecheck__() and .__subclasscheck__(),
# # as it creates a more reliable implementation of these dunder methods.
# #
# # Using .__subclasshook__()
# # Here's the implementation of FormalParserInterface using abc.ABCMeta as your metaclass:
#
# # Using .__subclasshook__()
# # Here's the implementation of FormalParserInterface using abc.ABCMeta as your metaclass:
#
# _______ a..
#
# c_ FormalParserInterface m..
#     ?c..
#     ___ -su.. ___ subclass
#         r_ h..  ? 'lo..' an.
#                 ca.. ?.lo.. an.
#                 h.. ?, 'ex..' an.
#                 ca.. ?.ex..
#
# c_ PdfParserNew
#     """Extract text from a PDF."""
#     ___ load_data_source  path st. file_name st. __ st.
#         """Overrides FormalParserInterface.load_data_source()"""
#         p..
#
#     ___ extract_text full_file_path st. __ di..
#         """Overrides FormalParserInterface.extract_text()"""
#         p..
#
# c_ EmlParserNew
#     """Extract text from an email."""
#     ___ load_data_source path st. file_name st. __ st.
#         """Overrides FormalParserInterface.load_data_source()"""
#         p..
#
#     ___ extract_text_from_email full_file_path st. __ di..
#         """A method defined only in EmlParser.
#         Does not override FormalParserInterface.extract_text()
#         """
#         p..
#
# # If you run issubclass() on PdfParserNew and EmlParserNew, then issubclass() will return True and False, respectively.
#
