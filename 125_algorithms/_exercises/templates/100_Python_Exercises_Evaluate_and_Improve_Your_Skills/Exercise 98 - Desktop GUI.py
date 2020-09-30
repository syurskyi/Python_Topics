#Create a program that asks the user to submit text through a GUI

from tkinter ______ *

window _ Tk()

file _ open("user_gui.txt", "a+")

___ add
    file.write(user_value.get() + "\n")
    entry.delete(0, END)

___ save
    global file
    file.close()
    file _ open("user_gui.txt", "a+")

___ close
    file.close
    window.destroy()

user_value _ StringVar()
entry _ Entry(window, textvariable_user_value)
entry.grid(row_0, column_0)

button_add _ Button(window, text_"Add line", command_add)
button_add.grid(row_0, column_1)

button_save _ Button(window, text_"Save changes", command_save)
button_save.grid(row_0, column_2)

button_close _ Button(window, text_"Save and Close", command_close)
button_close.grid(row_0,column_3)

window.mainloop()
