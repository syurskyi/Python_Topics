#take the input of how many elements you want
data = int(input())
# take the input of the numbers to be sorted
a = [int(num) ___ num in input().split()]

#create a dictionary to store the index of the list
ele = {}
#create the string to store the position of the sorted index
string = ''

#storing the index of the elements
___ x in range(le.(a)):
    ele[a[x]] = x+1
    
#sorting the array using the bubble sort
___ i in range(le.(a)):
    ___ j in range(0,le.(a)-1
        __ a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        ____
            pass
#identifying the elements which are sorted with the dictionary key and printing the original index in sorted form
___ ele_list in a:
    ___ dic in ele.keys(
        __ ele_list __ dic:
            string +=str(ele[dic])
            string +=' '
            
print(string)