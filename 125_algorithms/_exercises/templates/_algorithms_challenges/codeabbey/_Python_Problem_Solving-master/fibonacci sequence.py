fib_store = [0,1]
#generating the fibonacci Sequence
___ i __ r..(2,1000):
    fib_store.a..(fib_store[-2] + fib_store[-1])
    
#searching for the index of the given element from Fibonacci Sequence
___ i __ r..(int(input())):
    fib_num = int(input())
    ___ j __ r..(l..(fib_store)):
        __ fib_num __ fib_store[j]:
            break
    print(j,end=' ')