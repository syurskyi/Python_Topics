infile = open("prob5.txt")
count = infile.readline()
ans = ""
for i in range(int(count)):
    a,b,c = infile.readline().split(" ")
    __ int(a)>=int(b #take b
        __ int(b)>int(c #take c
            ans += c +" "
        ____
            ans += b+" "
    ____ #take a
        __ int(a)>int(c # take c
            ans += c+" "
        ____
            ans += a+" "
print(ans)
