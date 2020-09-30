listitem = [6,8,9,-2,0,1,-3,5,8,0,-6]
print(listitem)

___ i __ ra..(len(listitem)):
    if listitem[i] > 0:
        listitem[i] = 1
    elif listitem[i] < 0:
        listitem[i] = -1
    else:
        listitem[i] = 0

print(listitem)