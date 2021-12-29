s..  "Hello, World, Table, Chair, Cup, Tea"
print(s..)

substr1  input("Choose an old substring to replace: ")
substr2  input("Insert new substring: ")
lensubstr1  l..(substr1)

w___ s...find(substr1) > 0:
    i  s...find(substr1)
    s..  s..[:i] + substr2 + s..[i+lensubstr1:]
print(s..)