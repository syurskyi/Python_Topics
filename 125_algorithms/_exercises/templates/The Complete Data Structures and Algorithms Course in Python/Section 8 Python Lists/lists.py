#   Created by Elshad Karimov on 10/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Accessing/Traversing the list

shoppingList = ['Milk', 'Cheese', 'Butter']

___ i __ ra__(le_(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    # print(shoppingList[i])
empty = []
___ i __ empty:
    print("I am empty")


# Update/Insert - List 

myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)

myList.ap..(55)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)


#  Searching for an element in the List
myList =  [10,20,30,40,50,60,70,80,90]

___ searchinList(li__, value
    ___ i __ li__:
        __ i __ value:
            r_ li__.index(value)
    r_ 'The value does not exist in the list'

print(searchinList(myList, 100))


#  List operations / functions
total = 0 
count = 0
w__ (T..
    inp = input('Enter a number: ') 
    __ inp __ 'done': break
    value = float(inp)
    total = total + value
    count = count + 1 
    average = total / count
					
print('Average:', average)



numlist = li__() 
w__ (T..
    inp = input('Enter a number: ') 
    __ inp __ 'done': break
    value = float(inp)
    numlist.ap..(value)
					
average = sum(numlist) / le_(numlist) 
print('Average:', average)
