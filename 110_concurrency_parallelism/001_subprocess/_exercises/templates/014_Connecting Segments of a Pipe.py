# # subprocess_pipes.py
#
# _____ ?
#
# cat _ ?.P..
#     'cat' 'index.rst'
#     s_o__?.P..
# )
#
# g__ _ ?.P..
#     'g__' '.. literalinclude::'
#     s_i._cat.s_o_
#     s_o__?.P..
# )
#
# cut _ ?.P..
#     'cut' '-f' '3' '-d:'
#     s_i._g__.s_o_
#     s_o__?.P..
# )
#
# end_of_pipe _ c__.s_o_
#
# print('Included files:')
# ___ line __ ?
#     print ?.d.. 'utf-8' .st..
#
# # $ cat index.rst | g__ ".. literalinclude" | cut -f 3 -d:
#
# # $ python3 -u subprocess_pipes.py
# #
# # Included files:
# # subprocess_os_system.py
# # subprocess_shell_variables.py
# # subprocess_run_check.py
# # subprocess_run_output.py
# # subprocess_run_output_error.py
# # subprocess_run_output_error_trap.py
# # subprocess_check_output_error_trap_output.py
# # subprocess_run_output_error_suppress.py
# # subprocess_popen_read.py
# # subprocess_popen_write.py
# # subprocess_popen2.py
# # subprocess_popen3.py
# # subprocess_popen4.py
# # subprocess_pipes.py
# # repeater.py
# # interaction.py
# # signal_child.py
# # signal_parent.py
# # subprocess_signal_parent_shell.py
# # subprocess_signal_setpgrp.py
