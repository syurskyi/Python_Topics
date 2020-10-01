st. _ "Hello, World, Table, Chair, Cup, Tea"
print(st.)

substr1 _ i..("Choose an old substring to replace: ")
substr2 _ i..("Insert new substring: ")
lensubstr1 _ le.(substr1)

w___ st..find(substr1) > 0:
    i _ st..find(substr1)
    st. _ st.[:i] + substr2 + st.[i+lensubstr1:]
print(st.)