______ glob
______ os

text_files _ glob.glob("file*.txt")
___ text_file __ text_files:
    os.rename(text_file, text_file[:4] + "-" + text_file[4:])