

___ linear_search(array,item

	#simple linear search in O(N) running time complexity
	___ i __ ra..(le.(array)):
		
		#we have found the given item so return with the index
		__ array[i] __ item:
			r_ i

	#search miss: item not found
	r_ -1 
        
__  -n __ "__main__":

	array = [1,4,7,3,6,8,10,11,20,22]
	print(linear_search(array,111))