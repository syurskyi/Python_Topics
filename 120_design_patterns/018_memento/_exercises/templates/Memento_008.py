# #=======================================================================================================================
# c_ Engineer
#     """engineer"""
#
#     ___ - name
#         __?  ?
#         __workItems _    # list
#
#     ___ addWorkItem item
#         __w....ap.. ?
#
#     ___ forget
#         __w....cl..
#         print(__n.. + "I'm too busy at work, I've forgotten what to do!")
#
#     ___ writeTodoList
#         """Record work items in TodoList"""
#         todoList _ ?
#         ___ item __ __w...
#             ?.wWI.. ?
#         r_ ?
#
#     ___ retrospect todoList
#         """Recall work items"""
#         __w... _ ?.gWI..
#         print(__n.. + "Think of what to do!")
#
#     ___ showWorkItem
#         __ le. __w...
#             print(__n.. + "Work item:")
#             ___ idx __ ra.. 0, le. __w...
#                 print(st. ? + 1) + ". " + __w...|? + ";")
#         ___
#             print(__n.. + "No work items!")
#
#
# c_ TodoList
#     """Work item"""
#
#     ___ -
#         __workItems _    # list
#
#     ___ writeWorkItem item
#         __w....ap.. ?
#
#     ___ getWorkItems
#         r_ __w...
#
#
# c_ TodoListCaretaker
#     """TodoList Management Class"""
#
#     ___ -
#         __todoList _ N..
#
#     ___ setTodoList todoList
#         __?  ?
#
#     ___ getTodoList
#         r_ __?
#
#
# # Version 2.0
# #=======================================================================================================================
# # Code framework
# #==============================
# ____ co__ ______ d_c_
#
# c_ Memento
#     """memorandum"""
#
#     ___ setAttributes dict
#         """Deep copy all attributes __ dictionary dict"""
#         -d _ d_c_ ?
#
#     ___ getAttributes
#         """Get attribute dictionary"""
#         r_ -d
#
#
# c_ Caretaker
#     """Memo Management"""
#
#     ___
#         _mementos _    # dict
#
#     ___ addMemento name memento
#         _mementos|? _ ?
#
#     ___ getMemento name
#         r_ _m...|?
#
# c_ Originator
#     """Backup initiator"""
#
#     ___ createMemento
#         memento _ M..
#         ?.sA.. -d
#         r_ ?
#
#     ___ restoreFromMemento memento
#         -d.up.. ?.gA..
#
#
# # Framework-based implementation
# #==============================
#
# # Test
# #=======================================================================================================================
#
# ___ Engineer
#     tony _ E.. "Tony"
#     ?.a... "Solve the problem that some users online cannot display the full name because the nickname is too long")
#     ?.a... "Complete the parsing of the PDF")
#     ?.a... "Display the contents of the first page of a PDF __ a reader")
#     ?.sWI..
#     caretaker _ TLC..
#     ?.sTL.. ?.wTL..
#
#     print()
#     ?.f..
#     ?.sWI..
#
#     print()
#     ?.re.... c___.gTL..
#     ?.sWI..
#
# # testEngineer()