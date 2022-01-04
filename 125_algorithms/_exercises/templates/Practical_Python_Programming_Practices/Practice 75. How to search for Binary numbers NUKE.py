____ r__ _______ randint

___ num_search(first,last):
    mid  l..(first) //2
    mini  0
    maxi  l..(first) - 1
    w___ first[mid] ! last a.. mini < maxi:
        __ last > first[mid]:
            mini  mid + 1
        ____:
            maxi  mid -1
        mid  (mini + maxi) // 2
    __ mini > maxi:
        r.. N..
    ____:
        r.. mid

x  []
___ i __ r..(15):
    x.a..(randint(1,20))
x.s..()
print(x)

num  i..(input("Insert any number to search the list: "))
print(num_search(x,num))