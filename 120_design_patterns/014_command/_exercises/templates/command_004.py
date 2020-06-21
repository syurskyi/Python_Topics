# """Command pattern
#
# The Command pattern is handy when we want to isolate the portion of the code
# that executes an action, from the one that requests the execution. Command can
# be useful when we want to create a batch of operations and execute them later.
# """
# ______ d_t_
# ____ co.. ______ d_c_
#
#
# ___ rename_command x y $ $$
#     undo _ kw__.ge. *u.., F..
#     __ no. ?
#         print("rename @ into @".f.. x, y
#     ____
#         print("rename @ into @".f.. y x
#
#
# ___ move_command x source dest $ $$
#     undo _ kw__.ge. *u.. F..
#     __ no. ?
#         print("move @ from @ to @".f.. ?  ?  ?
#     ____
#         print("move @ from @ to @".f.. ? d.. s..
#
#
# c_ Queue o..
#
#     ___ -
#         _commands _ li..
#         _history _ li..
#
#     ___ add_command func $ $$
#         timestamp _ d_t_.d_t_.n__.i_f..
#         _c___.ap..|
#             |*timestamp t.. *func ? *args ? *kwargs ?
#         |
#
#     ___ execute commands_N..
#         __ commands __ N..
#             ? _ _c..
#         ___ cmd __ ?
#             func _ cmd["func"]
#             args, kwargs _ cmd|*args, cmd|*kwargs
#             func $ $$
#         u_h.. c..
#         c_q..
#
#     ___ redo
#         commands _ _h..|-1
#         execute ?
#
#     ___ undo
#         original_commands _ _h..|-1
#         commands _ d_c_ o_c..
#         ___ cmd __ ?
#             func _ ?|*func
#             args, kwargs _ c..|*args , cmd|*kwargs
#             # we need to store the "undo" within the command (for history)
#             kw__.up..||*undo T..
#             func $ $$
#         u_h.. c..
#
#     ___ clear_queue
#         _commands _ li..
#
#     ___ update_history commands
#         _h___.ap.. ?
#
#     ___ history
#         ___ i, commands __ en... _h..
#             print("Set of commands @".f.. i
#             ___ cmd in c...
#                 t _ ?|*timestamp
#                 f _ ?|*func . -n
#                 ar, kw _ ?|*args,  ?|*kwargs
#                 print(" @ - f: @ args: @ kwargs: @".f.. ?  ?  ?  ?
#
#
# ___ main
#     queue _ Q..
#
#     ?.a... r_c.. "test.py", "hello.py")
#     ?.a... m_c.. "hello.py", source_"/lib", dest_"/home")
#     ?.a... r_c.. x_"readme.txt", y_"README.txt")
#
#     print("Execute all commands as a single operation")
#     ?.ex..
#
#     print("\nRedo last operation")
#     ?.r..
#
#     print("\nUndo last operation")
#     ?.u..
#
#     print("\nExecute a single command")
#     ?.a... m_c.. "hello.py", source_"/lib", dest_"/home")
#     ?.ex..
#
#     print("\nUndo last operation")
#     ?.u..
#
#     print("\nShow history")
#     ?.h..
#
#
# __ _______ __ ______
#     ?
