____ random _______ random

num  20
listitem  [0]*num

___ i __ r..(num):
    listitem[i]  i..(random()*50)
print(listitem)

maxi  1
mylength  1
mycode  0

___ i __ r..(1,num):
    __ listitem[i] > listitem[i-1]:
        mylength + 1
    ____:
        __ mylength > maxi:
            maxi  mylength
            mycode  i
        mylength  1
print("The maximum lenght = ",maxi)
print("The ordered values are = ",listitem[mycode-maxi : mycode])