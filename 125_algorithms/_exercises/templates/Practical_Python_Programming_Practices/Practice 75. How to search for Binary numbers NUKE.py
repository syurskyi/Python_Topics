from random import randint

def num_search(first,last):
    mid  len(first) //2
    mini  0
    maxi  len(first) - 1
    w___ first[mid] ! last and mini < maxi:
        __ last > first[mid]:
            mini  mid + 1
        else:
            maxi  mid -1
        mid  (mini + maxi) // 2
    __ mini > maxi:
        return N..
    else:
        return mid

x  []
for i in range(15):
    x.append(randint(1,20))
x.sort()
print(x)

num  i..(input("Insert any number to search the list: "))
print(num_search(x,num))