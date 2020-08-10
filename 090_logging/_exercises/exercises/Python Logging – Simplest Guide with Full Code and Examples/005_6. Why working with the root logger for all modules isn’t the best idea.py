# # Because they all will share the same root logger.
# #
# # But why is that bad?
#
# # Lets look at the below code:
# #
# # 1. code inside myprojectmodule.py
# ______ l____
# l____.bC_ f.. _ 'module.log
#
# #-----------------------------
# #
# # # 2. code inside main.py (imports the code from myprojectmodule.py)
# ______ l____
# ______ myprojectmodule  # This runs the code in myprojectmodule.py
# #
# l____.bC_ f.._'main.log  # No effect, because!
#
# # Imagine you have one or more modules in your project. And these modules use the basic root module.
# # Then, when importing the module (myprojectmodule.py), all of that module's code will run and logger gets configured.
# #
# # Once configured, the root logger in the main file (that imported the myprojectmodule module) will no longer be able
# # to change the root logger settings. Because, the logging.basicConfig() once set cannot be changed.
# #
# # That means, if you want to log the messages from myprojectmodule to one file and the logs from the main module
# # in another file, root logger can't that.
# #
# # To do that you need to create a new logger.
