_______ glob
_______ re

text_files  glob.glob("*.txt")
lists []
___ text_file __ text_files:
    with open(text_file) as file:
        lists.a..(file.readlines())

all_lines  s..(lists, [])

matches  [re.compile("[0-9]+\.*[0-9]*").search(line) ___ line __ all_lines]

numbers  [float(match.group(0)) ___ match __ matches __ match]
print(s..(numbers)/l..(numbers))