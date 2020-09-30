from random ______ r_i..

___ num_search(first,last):
    mid _ le.(first) //2
    mini _ 0
    maxi _ le.(first) - 1
    while first[mid] !_ last an. mini <_ maxi:
        __ last > first[mid]:
            mini _ mid + 1
        ____
            maxi _ mid -1
        mid _ (mini + maxi) // 2
    __ mini > maxi:
        r_ None
    ____
        r_ mid

x _   # list
___ i __ ra..(15):
    x.ap..(r_i..(1,20))
x.sort()
print(x)

num _ in.(input("Insert any number to search the list: "))
print(num_search(x,num))