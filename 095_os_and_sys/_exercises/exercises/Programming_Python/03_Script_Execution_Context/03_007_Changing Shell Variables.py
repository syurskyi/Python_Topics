# ______ __
# print(__.e__ TEMP
# # 'C:\\Users\\mark\\AppData\\Local\\Temp
# __.e__ TEMP _ _'c:\temp'
# print(__.en____ TEMP
# # 'c:\\temp'
#
# # in the shell itself:
# # C:\...\PP4E\System\Environment> set USER=Bob
# # C:\...\PP4E\System\Environment> python echoenv.py
# # echoenv... Hello, Bob
# # ####################################################################################################################
#
# print('#' * 52 + 'setenv.py')
# _______ __
# print('setenv...' e.._' '
# print(__.e__ USER                # show current shell variable value
# #
# # os.environ['USER'] = 'Brian'             # runs os.putenv behind the scenes
# # os.system('python echoenv.py')
# #
# # os.environ['USER'] = 'Arthur'            # changes passed to spawned programs
# # os.system('python echoenv.py')           # and linked-in C library modules
# #
# # os.environ['USER'] = input('?')
# # print(os.popen('python echoenv.py').read())
# #
# # C:\...\PP4E\System\Environment> python setenv.py
# # setenv... Bob
# # echoenv... Hello, Brian
# # echoenv... Hello, Arthur
# # ?Gumby
# # echoenv... Hello, Gumby
# # C:\...\PP4E\System\Environment> echo %USER%
# # Bob
# # ####################################################################################################################
