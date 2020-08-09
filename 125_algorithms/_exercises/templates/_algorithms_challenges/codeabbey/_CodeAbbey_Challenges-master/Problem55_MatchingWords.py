infile = open("prob55.txt")
data =infile.read()
infile.close()

data = data.strip().split(" ")

i=0
latins = dict()
w___ data[i] != "end":
    latins[data[i]]= latins.get(data[i],0)+1
    i+=1

code = list(latins.items())

# INSERTION SORT
i = 0
w___ i<le.(code)-1:
    __ code[i]>code[i+1]:
        temp= code[i+1]
        j=i
        w___ j>0 and code[j]>temp:
            code[j],code[j+1]=code[j+1],code[j]
            j-=1
        code[j+1] = temp
    i+=1

___ i in code:
    __ i[1]>=2:
        print(i[0],end=" ")
        

