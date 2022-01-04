____ r__ _______ r__
N  20
array  []
___ x __ r..(N):
    array.a..(i..(r__()*100))

array.s..()
print(array)

number  i..(input("Search for any number in the array: "))

mini  0
maxi  N-1

w___ mini < maxi:
    mid  (mini + maxi) // 2
    __ number < array[mid]:
        maxi  mid-1
    ____ number > array[mid]:
        mini  mid+1
    ____:
        print("The number is located at index: ", mid)
        _____
____:
    print("There is no number!")
