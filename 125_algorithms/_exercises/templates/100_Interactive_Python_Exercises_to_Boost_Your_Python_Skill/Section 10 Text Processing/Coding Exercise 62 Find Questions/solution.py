______ re
with open("file2.txt") as file:
    content _ file.read()
    print(re.findall("[A-Z][a-z ',]*\?", content))