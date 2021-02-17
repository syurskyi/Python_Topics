# LIST COMPREHENSIONS
myList = []
for item in range(0,20):
    myList.append(item)

print myList

myListComp = [item for item in range(0,20)]
print myListComp

myList = []
for item in range(0,20):
    if item % 2 == 1:
        myList.append(item)
print myList

myListComp = [item for item in range(0,20) if item % 2 == 1]
print myListComp

myList = []
for item in range(0,20):
    if item % 2 == 1:
        myList.append((item + 21) // 7)
print myList

myListComp = [(item + 21) // 7 for item in range(0,20) if item % 2 == 1]
print myListComp