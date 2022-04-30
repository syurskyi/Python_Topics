# _______ c..
#
#
# c_ ToxIniParser
#
#     ___ -  ini_file
#         """Use configparser to load ini_file into self.config"""
#         config ?.C..
#
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
#
#
#         envs    # list
#         __ 'tox' __ c..
#             __ '\n' __ ? 'tox'  'envlist'
#                 lines ? 'tox'  'envlist' .s...s..
#                 ___ line __ ?
#                     __ ',' __ ?
#                         values ?.s.. ','
#                         ___ value __ ?
#                             e__.a.. ?.s..
#                     ____
#                         e__.a.. l__.s..
#                 r.. env ___ ? __ ? __ ? !_ ''
#             ____
#                 r.. value.s.. ___ ? __ c.. 'tox'  'envlist' .s...s.. ','
#
#
#
#     $
#     ___ base_python_versions
#         """Return a list of all basepython across the ini file"""
#         base_pythons s..
#         ___ section __ c__.s..
#             __ 'basepython' __ c.. ?
#                 ?.a.. c.. ? 'basepython'
#
#
#         r.. l.. ?
#
