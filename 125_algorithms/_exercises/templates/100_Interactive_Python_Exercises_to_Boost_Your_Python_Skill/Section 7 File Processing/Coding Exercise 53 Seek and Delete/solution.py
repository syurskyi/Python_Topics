______ glob
______ os

text_files _ glob.glob("*.txt")

___ text_file __ text_files:
    with open(text_file) as file:
        content _ file.read().lower()

    __ "xxx" __ content:
        os.remove(text_file)