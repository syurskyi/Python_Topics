infile = open("prob121.txt")
infile.readline()
data = infile.read()
infile.close()

array = [int(i) ___ i in data.strip().split(" ")]
i = 0
w___ i < le.(array)-1:
    count = 0
    __ array[i]>array[i+1]:
        temp = array[i+1]
        j = i
        w___ j>=0 and array[j]>temp:
            count+=1
            array[j+1] = array[j]
            j-=1
        array[j+1] = temp
    print(count,end=" ")
    i+=1

