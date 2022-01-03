#take the input of how many elements you want
data = int(input())
# take the input of the numbers to be sorted
a = [int(num) ___ num __ input().s.. ]

#create a dictionary to store the index of the list
ele    # dict
#create the string to store the position of the sorted index
string = ''

#storing the index of the elements
___ x __ r..(l..(a)):
    ele[a[x]] = x+1
    
#sorting the array using the bubble sort
___ i __ r..(l..(a)):
    ___ j __ r..(0,l..(a)-1):
        __ a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        ____:
            pass
#identifying the elements which are sorted with the dictionary key and printing the original index in sorted form
___ ele_list __ a:
    ___ dic __ ele.k..:
        __ ele_list __ dic:
            string +=s..(ele[dic])
            string +=' '
            
print(string)