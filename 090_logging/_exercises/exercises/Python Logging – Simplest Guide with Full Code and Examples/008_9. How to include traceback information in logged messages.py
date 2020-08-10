# # Besides debug, info, warning, error, and critical messages, you can log exceptions that will include any
# # associated traceback information.
# # With logger.exception, you can log traceback information should the code encounter any error. logger.exception will log
# # the message provided in its arguments as well as the error message traceback info.
# #
# # Below is a nice example.
#
# ______ l____
#
# # Create or get the logger
# logger _ l____.gL_ -n
#
# # set log level
# ?.sL_ l____.I..
#
# ___ divide x y
#     t_
#         out = x / y
#     e___ Z...
#         ?.e.. "Division by zero problem"
#     e___
#         r___ o..
#
# # Logs
# ?.e... "Divide x / y = c".f... x_10 y_0 c_d.. 10,0
#
# #> ERROR:__main__:Division by zero problem
# #> Traceback (most recent call last):
# #>   File "<ipython-input-16-a010a44fdc0a>", line 12, in divide
# #>     out = x / y
# #> ZeroDivisionError: division by zero
# #> ERROR:__main__:None
