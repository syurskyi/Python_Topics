str  "Hello, World, Table, Chair, Cup, Tea"
print(str)

substr1  input("Choose an old substring to replace: ")
substr2  input("Insert new substring: ")
lensubstr1  l..(substr1)

w___ str.find(substr1) > 0:
    i  str.find(substr1)
    str  str[:i] + substr2 + str[i+lensubstr1:]
print(str)