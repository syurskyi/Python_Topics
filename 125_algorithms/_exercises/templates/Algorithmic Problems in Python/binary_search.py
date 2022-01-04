
#we can achieve O(logN) but the array must be sorted
___ binary_search(array,item,left,right):

	#base case for recursive function calls
	#this is the search miss (array does not contain the item)
	__ right < left:
		r.. -1

	#let's generate the middle item's index	
	middle  left + (right-left)//2
	print("Middle index: ",middle)
	
	#the middle item is the item we are looking for
	__ array[middle] __ item:
		r.. middle

	#the item we are looking for is smaller than the middle item
	#so we have to consider the left subarray
	____ array[middle] > item:
		print("Checking items on the left...")
		r.. binary_search(array,item,left,middle-1)
	
	#the item we are looking for is greater than the middle item
	#so we have to consider the right subarray	
	____ array[middle] < item:
		print("Checking items on the right...")
		r.. binary_search(array,item,middle+1,right)
        
__ _______ __ _______

	array  [1,4,7,8,9,10,11,20,22,25]
	
	print(binary_search(array,111,0,l..(array)-1))