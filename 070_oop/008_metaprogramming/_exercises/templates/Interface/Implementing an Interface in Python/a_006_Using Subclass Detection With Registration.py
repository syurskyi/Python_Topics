# # Using Subclass Detection With Registration
# # You must be careful when you're combining .__subclasshook__() with .register(), as .__subclasshook__() takes
# # precedence over virtual subclass registration. To ensure that the registered virtual subclasses are taken into
# # consideration, you must add NotImplemented to the .__subclasshook__() dunder method. The FormalParserInterface
# # would be updated to the following:
#
# _______ a..
#
# c_ FormalParserInterface m..
#     ?c..
#     ___ __subclasshook__ ___ subclass
#         r_ h.. ? 'lo..' an.
#                 ca.. ?.lo.. an.
#                 h.. ? 'ex..' an.
#                 ca.. ?.ex.. o.
#                 N...
#
# c_ PdfParserNew
#     """Extract text from a PDF."""
#     ___ load_data_source path ? file_name ? __ ?
#         """Overrides FormalParserInterface.load_data_source()"""
#         p..
#
#     ___ extract_text(self, full_file_path: ?) __ di..
#         """Overrides FormalParserInterface.extract_text()"""
#         p..
#
# ?F__.re..
# c_ EmlParserNew
#     """Extract text from an email."""
#     ___ load_data_source path ? file_name ? __ ?
#         """Overrides FormalParserInterface.load_data_source()"""
#         p..
#
#     ___ extract_text_from_email full_file_path ? __ di..
#         """A method defined only in EmlParser.
#         Does not override FormalParserInterface.extract_text()
#         """
#         p..
#
# print(iss.. P.. F..  # True
# print(iss.. E.. F..  # True
#
# # Since you've used registration, you can see that EmlParserNew is considered a virtual subclass of your
# # FormalParserInterface interface. This is not what you wanted since EmlParserNew doesn't override .extract_text().
# # Please use caution with virtual subclass registration!
