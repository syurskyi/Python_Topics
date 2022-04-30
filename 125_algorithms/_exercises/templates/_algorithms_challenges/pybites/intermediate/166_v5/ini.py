# _______ c..
# _______ __
#
#
# c_ ToxIniParser
#
#     ___ -  ini_file
#         """Use configparser to load ini_file into self.config"""
#         config ?.C..
#         ?.r.. ?
#
#     $
#     ___ number_of_sections
#         """Return the number of sections in the ini file.
#            New to properties? -> https://pybit.es/property-decorator.html
#         """
#         r.. l.. ?.s..
#
#     $
#     ___ environments
#         """Return a list of environments
#            (= "envlist" attribute of [tox] section)"""
#         r.. l.. x ___ ? __ __.f.. _ [-\w]+ ? 'tox'  'envlist'
#
#     $
#     ___ base_python_versions
#         """Return a list of all basepython across the ini file"""
#         r.. l.. ? s i
#                      ___ ? __ ?.s..
#                      ___ ? __ ? ? .k.. __ 'basepython' __ ?
