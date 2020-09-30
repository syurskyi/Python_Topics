import glob
import os

text_files = glob.glob("*.txt")

sizes = {text_file:os.path.getsize(text_file) for text_file in text_files}
print(min(sizes, key=sizes.get))
