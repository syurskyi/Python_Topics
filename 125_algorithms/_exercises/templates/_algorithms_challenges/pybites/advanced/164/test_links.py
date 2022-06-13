# _______ __
# ____ p.. _______ P..
# _______ p..
# _______ s..
#
# _______ p__
#
# # no need to import make_html_links as we call links.py from CLI!
#
# TMP P.. __.g.. "TMP", "/tmp"
# SCRIPT 'links.py'
# IS_LOCAL p__.s.. __ 'Darwin'
# MY_CODE SCRIPT __ ? ____ T.. / S..
#
#
# # https://docs.pytest.org/en/latest/tmpdir.html#the-tmpdir-factory-fixture
#
# ?p__.f..
# ___ my_file tmp_path
#     f ? / some_file.txt
#     r.. ?
#
#
# ___ _create_and_verify_links my_file lines expected_links
#     ?.w.. _'\n'.j.. ?
#     cmd _* cat ?.r.. | python M..
#     output s__.c.. ? s.._T.. .s..
#     ... a.. link __ ? ___ ? __ ?
#
#
# ___ test_make_html_links_first_data_set my_file
#     lines _"https://www.python.org, Python Homepage",
#              _"bad data,blabla,123",
#              _"https://pybit.es/generators.html , "
#               _"Generators are Awesome "
#              _"more bad data"
#
#     expected_links _'<a href="https://www.python.org" target="_blank">'
#                        _'Python Homepage</a>'),
#                       _'<a href="https://pybit.es/generators.html">'
#                        _'Generators are Awesome</a>'
#
#     ? ? ? ?
#
#
# ___ test_make_html_links_second_data_set my_file
#     lines [b"bogus data, again",
#              _"https://codechalleng.es/bites/ , Bites of Py",
#              _"https://stackoverflow.com/a/12927564,How to capture"
#               b" subprocess.call stdout"),
#              _"https://pybit.es/,Our labor of love",
#              _"https://pybit.es/pages/about.html, About Us",
#              _"https://nu.nl, Dutch news site",
#              _"And some more bad data !!"
#
#     expected_links _'<a href="https://codechalleng.es/bites/">'
#                        _'Bites of Py</a>'),
#                       _'<a href="https://stackoverflow.com/a/12927564" '
#                        _'target="_blank">How to capture subprocess.call '
#                        _'stdout</a>'),
#                       _'<a href="https://pybit.es/">Our labor of love</a>',
#                        _'<a href="https://pybit.es/pages/about.html">'
#                        _'About Us</a>'),
#                       _'<a href="https://nu.nl" target="_blank">'
#                        _'Dutch news site</a>')]
#
#     ? ? ? ?
