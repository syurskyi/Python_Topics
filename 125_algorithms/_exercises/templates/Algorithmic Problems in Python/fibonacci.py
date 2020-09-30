
___ fibonacci(n

	#we have to define the base cases
	#F(0)=1 and F(1)=1
	__ n__0: r_ 0
	__ n__1: r_ 1

	#head recursion: first we call the function recursively
	#overlapping subproblems so better approach would be to use dynamic programming
	fib1 _ fibonacci(n-1)
	fib2 _ fibonacci(n-2)
	
	#do some operation after recursion
	result _ fib1+fib2
	
	r_ result

	
__  -n __ "__main__":

	print(fibonacci(10))