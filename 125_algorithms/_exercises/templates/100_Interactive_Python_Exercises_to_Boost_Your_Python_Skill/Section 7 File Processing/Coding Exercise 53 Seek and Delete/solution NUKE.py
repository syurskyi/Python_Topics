import glob
import os

text_files  glob.glob("*.txt")

for text_file in text_files:
    with open(text_file) as file:
        content  file.read().l..

    __ "xxx" in content:
        os.remove(text_file)