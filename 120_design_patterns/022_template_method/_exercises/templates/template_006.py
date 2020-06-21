# """
# An example of the Template pattern in Python
#
# *TL;DR
# Defines the skeleton of a base algorithm, deferring definition of exact
# steps to subclasses.
#
# *Examples in Python ecosystem:
# Django class based views: https://docs.djangoproject.com/en/2.1/topics/class-based-views/
# """
#
#
# ___ get_text
#     r_ "plain-text"
#
#
# ___ get_pdf
#     r_ "pdf"
#
#
# ___ get_csv
#     r_ "csv"
#
#
# ___ convert_to_text data
#     print("[CONVERT]")
#     r_ "@ as text".f... ?
#
#
# ___ saver
#     print("[SAVE]")
#
#
# ___ template_function getter converter_F.. to_save_F..
#     data = ?
#     print("Got `@`".f.. ?
#
#     __ le. ? <_ 3 an. c..
#         data _ c.. ?
#     ____
#         print("Skip conversion")
#
#     __ to_save
#         s..
#
#     print("`@` was processed".f... ?
#
#
# ___ main
#
#     ? g_t.. t_s.._T..
#     # Got `plain-text`
#     # Skip conversion
#     # [SAVE]
#     # `plain-text` was processed
#
#     ? g_p.. c..._c_t._t..
#     # Got `pdf`
#     # [CONVERT]
#     # `pdf as text` was processed
#     #
#     ? g_c.. t_s.._T..
#     # Got `csv`
#     # Skip conversion
#     # [SAVE]
#     # `csv` was processed
#
#
#
# __ ________ __ _________
#     ?
