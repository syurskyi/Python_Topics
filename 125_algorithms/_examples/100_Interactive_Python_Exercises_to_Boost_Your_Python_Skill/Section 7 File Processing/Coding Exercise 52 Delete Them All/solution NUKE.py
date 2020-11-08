import glob
import os

text_files = glob.glob("*.txt")
for text_file in text_files:
    os.remove(text_file)