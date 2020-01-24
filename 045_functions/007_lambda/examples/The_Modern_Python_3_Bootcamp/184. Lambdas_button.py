import tkinter as tk
# DON'T WORRY ABOUT ANY OF THIS CODE
root = tk.Tk()  # =====================
frame = tk.Frame(root)  # =============
frame.pack()  # =======================
# DON'T WORRY ABOUT ANY OF THIS CODE

# Don't need this function if we use a lambda
# def say_hi():
#     print("HELLO!")

button = tk.Button(frame,
                   text="CLICK ME",
                   fg="red",
                   command=lambda: print("Hello"))


# DON'T WORRY ABOUT ANY OF THIS CODE
button.pack(side=tk.LEFT)  # =========
root.mainloop()  # ===================
# DON'T WORRY ABOUT ANY OF THIS CODE



