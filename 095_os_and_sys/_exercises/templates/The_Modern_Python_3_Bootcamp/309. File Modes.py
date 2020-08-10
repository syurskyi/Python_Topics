# w - writes and erases existing contents
w__ o..("haiku.txt", "w") __ file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# a - appends to end, preserving original contents
# NO CONTROL OVER CURSOR

w__ o..("haiku.txt", "a") __ file:
    file.seek(0)
    file.write(":)\n")

# r+ read and write
w__ o..("haiku.txt", "r+") __ file:
    file.write(":)")
    file.seek(10)
    file.write(":(")
# r+ will not create a file if it doesn't exist
w__ o..("hello.txt", "a") __ file:
    file.write("HELLO!!!")
