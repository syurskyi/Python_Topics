
___ factorial(n

	#base case: 1!=1 (factorial 1 is 1)
	__ n __ 1:
		r_ 1
        
	#we make a recursive call
	subres1 = factorial(n-1)	
	
	#we do some operations
	subres2 = n*subres1		
	
	r_ subres2
	
___ factorial_accumulator(n,accumulator=1

	#base case: 1!=1
	__ n__1:
		r_ accumulator
		
	#now it is a tail recursion !!!
	r_ factorial_accumulator(n-1,n*accumulator)
	
__ __name__ __ "__main__":

	print(factorial_accumulator(5))