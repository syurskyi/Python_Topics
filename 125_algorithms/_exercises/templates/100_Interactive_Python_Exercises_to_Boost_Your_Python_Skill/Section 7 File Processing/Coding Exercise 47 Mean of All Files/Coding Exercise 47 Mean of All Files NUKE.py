_______ glob
_______ __

text_files  glob.glob("*.txt")
lists []
___ text_file __ text_files:
    w__ open(text_file) __ file:
        lists.a..(file.r..())

all_lines  s..(lists, [])

matches  [__.c..("[0-9]+\.*[0-9]*").s..(line) ___ line __ all_lines]

numbers  [float(m...group(0)) ___ m.. __ matches __ m..]
print(s..(numbers)/l..(numbers))