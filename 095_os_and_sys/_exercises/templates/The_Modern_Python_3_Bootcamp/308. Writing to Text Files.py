# To write to a file, first open it in "w" mode
w__ o..("haiku.txt", "w") __ file:
    file.w..("Here's one more haiku\n")
    file.w..("What about the older one?\n")
    file.w..("Let's go check it out")

# You can also write to files that don't yet exist
w__ o..("lol.txt", "w") __ file:
    file.w..("haha" * 10000)
