from random ______ random
N _ 20
array _   # list
___ x __ ra..(N):
    array.ap..(in.(random()*100))

array.sort()
print(array)

number _ in.(input("Search for any number in the array: "))

mini _ 0
maxi _ N-1

while mini <_ maxi:
    mid _ (mini + maxi) // 2
    __ number < array[mid]:
        maxi _ mid-1
    elif number > array[mid]:
        mini _ mid+1
    ____
        print("The number is located at index: ", mid)
        break
____
    print("There is no number!")
