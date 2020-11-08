import glob
import os

text_files = glob.glob("file*.txt")
for text_file in text_files:
    os.rename(text_file, text_file[:4] + "-" + text_file[4:])