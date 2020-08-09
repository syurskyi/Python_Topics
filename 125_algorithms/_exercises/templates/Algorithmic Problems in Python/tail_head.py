
#tail recursion
___ tail(n

	#base case
	__ n__0:
		r_
		
	#do some operation before the recursive call
	print(n)
	
	#recursive call
	tail(n-1)

___ head(n

	#base case 
	__ n__0:
		r_
	
	#recursive call
	head(n-1)
	
	#do some operation after the recursive call
	print(n)
	
__ __name__ __ "__main__":

	print("Tail recursion:\n")
	tail(5)
	print("\nHead recursion:\n")
	head(5)