# # subprocess_run_output_error_trap.py
#
# _____ ?
#
# ___
#     completed _ ?.r..
#         'echo to stdout; echo to s_e.. 1>&2; exit 1',
#         s.._T..
#         s_o__?.P..
#         s_e.._?.P..
#     )
# _____ ?.C.. __ err
#     print('ERROR:' ?
# ____
#     print('returncode:' ?.r_c..
#     print('Have @ bytes in stdout: @'.f..
#         le. ?.s_o_
#         ?.s_o_.d.. 'utf-8'
#     )
#     print('Have @ bytes in s_e..: @'.f..
#         le.(?.s_e..
#         ?.s_e...d.. 'utf-8'
#
#
# # $ python3 subprocess_run_output_error_trap.py
# #
# # returncode: 1
# # Have 10 bytes in stdout: 'to stdout\n'
# # Have 10 bytes in s_e..: 'to s_e..\n'
#
