from random ______ random

num _ 20
listitem _ [0]*num

___ i __ ra..(num):
    listitem[i] _ in.(random()*50)
print(listitem)

maxi _ 1
mylength _ 1
mycode _ 0

___ i __ ra..(1,num):
    __ listitem[i] > listitem[i-1]:
        mylength +_ 1
    ____
        __ mylength > maxi:
            maxi _ mylength
            mycode _ i
        mylength _ 1
print("The maximum lenght = ",maxi)
print("The ordered values are = ",listitem[mycode-maxi : mycode])