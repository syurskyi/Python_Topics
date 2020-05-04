# ______ ___
# ____ __.W.. ______ ?A.. ?W..
#
#
# ___ main
#     app _ ?
#
#     w _ ?W..
#     ?.r.. 250, 150
#     ?.m.. 300, 300
#     ?.sWT.. *Simple
#     ?.s..
#
#     ___.e.. ?.e.._
#
#
# __ ______ __ ______
#     ?

#  Finally, we enter the mainloop of the application. The event handling starts from this point.
#  The mainloop receives events from the window system and dispatches them to the application widgets.
#  The mainloop ends if we call the exit() method or the main widget is destroyed.
#  The sys.exit() method ensures a clean exit. The environment will be informed how the application ended.
#
# The exec_() method has an underscore. It is because the exec is a Python keyword. And thus, exec_() was used instead.