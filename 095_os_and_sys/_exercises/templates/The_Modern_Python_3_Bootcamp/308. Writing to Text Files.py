# To write to a file, first open it in "w" mode
w__ o..("haiku.txt", "w") __ file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# You can also write to files that don't yet exist
w__ o..("lol.txt", "w") __ file:
    file.write("haha" * 10000)
