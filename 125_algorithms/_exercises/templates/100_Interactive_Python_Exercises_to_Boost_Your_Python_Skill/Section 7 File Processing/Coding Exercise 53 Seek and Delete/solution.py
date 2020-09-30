import glob
import os

text_files = glob.glob("*.txt")

___ text_file __ text_files:
    with open(text_file) as file:
        content = file.read().lower()

    if "xxx" __ content:
        os.remove(text_file)