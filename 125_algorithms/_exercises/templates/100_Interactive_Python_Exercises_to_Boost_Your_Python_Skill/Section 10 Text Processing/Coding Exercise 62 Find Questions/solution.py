import re
with open("file2.txt") as file:
    content = file.read()
    print(re.findall("[A-Z][a-z ',]*\?", content))