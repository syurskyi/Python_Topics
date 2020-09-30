import glob
import re

text_files = glob.glob("*.txt")
lists =  # list
___ text_file __ text_files:
    with open(text_file) as file:
        lists.append(file.readlines())

all_lines = sum(lists,   # list)

matches = [re.compile("[0-9]+\.*[0-9]*").search(line) ___ line __ all_lines]

numbers = [float(match.group(0)) ___ match __ matches if match]
print(sum(numbers)/len(numbers))