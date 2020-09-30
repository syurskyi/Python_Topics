______ glob
______ re

text_files _ glob.glob("*.txt")
lists _  # list
___ text_file __ text_files:
    with open(text_file) as file:
        lists.ap..(file.readlines

all_lines _ su.(lists,   # list)

matches _ [re.compile("[0-9]+\.*[0-9]*").search(line) ___ line __ all_lines]

numbers _ [float(match.group(0)) ___ match __ matches __ match]
print(su.(numbers)/le.(numbers))