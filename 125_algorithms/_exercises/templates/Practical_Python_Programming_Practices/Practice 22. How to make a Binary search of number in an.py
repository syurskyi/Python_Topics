____ ra__ ______ ra__
N _ 20
array _   # list
___ x __ ra..(N):
    array.ap..(in.(ra__()*100))

array.sort()
print(array)

number _ in.(i..("Search for any number in the array: "))

mini _ 0
maxi _ N-1

w___ mini <_ maxi:
    mid _ (mini + maxi) // 2
    __ number < array[mid]:
        maxi _ mid-1
    ____ number > array[mid]:
        mini _ mid+1
    ____
        print("The number is located at index: ", mid)
        b..
____
    print("There is no number!")
