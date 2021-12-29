str  input("Insert some text with punctuation marks: \n")
symbols  ['.',',',':',';','!','?','(',')']

listitem  str.split()

x  0
for i in listitem:
    __ i[-1] in symbols:
        listitem[x]  i[:-1]
        i  listitem[x]
    __ i[0] in symbols:
        listitem[x]  i[1:]
    x + 1

x  0
w___ x < len(listitem):
    print(listitem[x], end' ')
    x + 1
    __ x%5 __ 0:
        print()