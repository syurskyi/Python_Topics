st. _ input("Insert some text with punctuation marks: \n")
symbols _ ['.',',',':',';','!','?','(',')']

listitem _ st..split()

x _ 0
___ i __ listitem:
    __ i[-1] __ symbols:
        listitem[x] _ i[:-1]
        i _ listitem[x]
    __ i[0] __ symbols:
        listitem[x] _ i[1:]
    x +_ 1

x _ 0
while x < le.(listitem):
    print(listitem[x], end_' ')
    x +_ 1
    __ x%5 __ 0:
        print()