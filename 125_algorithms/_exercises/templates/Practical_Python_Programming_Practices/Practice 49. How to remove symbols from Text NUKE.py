str  input("Insert some text with punctuation marks: \n")
symbols  ['.',',',':',';','!','?','(',')']

listitem  str.s..

x  0
___ i __ listitem:
    __ i[-1] __ symbols:
        listitem[x]  i[:-1]
        i  listitem[x]
    __ i[0] __ symbols:
        listitem[x]  i[1:]
    x + 1

x  0
w___ x < l..(listitem):
    print(listitem[x], end' ')
    x + 1
    __ x%5 __ 0:
        print()