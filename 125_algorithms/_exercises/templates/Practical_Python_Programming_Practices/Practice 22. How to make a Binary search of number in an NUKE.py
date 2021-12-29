from random import random
N  20
array  []
for x in range(N):
    array.append(i..(random()*100))

array.sort()
print(array)

number  i..(input("Search for any number in the array: "))

mini  0
maxi  N-1

w___ mini < maxi:
    mid  (mini + maxi) // 2
    __ number < array[mid]:
        maxi  mid-1
    elif number > array[mid]:
        mini  mid+1
    else:
        print("The number is located at index: ", mid)
        _____
else:
    print("There is no number!")
