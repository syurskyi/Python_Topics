# #Create a program that asks the user to submit text through a GUI
#
# ____ tkinter _______ *
#
# window = Tk()
#
# file = o..("user_gui.txt", "a+")
#
# ___ add():
#     file.w..(user_value.g..() + "\n")
#     entry.delete(0, END)
#
# ___ save():
#     global file
#     file.c..
#     file = o..("user_gui.txt", "a+")
#
# ___ c..:
#     file.close
#     window.destroy()
#
# user_value = StringVar()
# entry = Entry(window, textvariable=user_value)
# entry.grid(row=0, column=0)
#
# button_add = Button(window, t..="Add line", command=add)
# button_add.grid(row=0, column=1)
#
# button_save = Button(window, t..="Save changes", command=save)
# button_save.grid(row=0, column=2)
#
# button_close = Button(window, t..="Save and Close", command=close)
# button_close.grid(row=0,column=3)
#
# window.mainloop()
