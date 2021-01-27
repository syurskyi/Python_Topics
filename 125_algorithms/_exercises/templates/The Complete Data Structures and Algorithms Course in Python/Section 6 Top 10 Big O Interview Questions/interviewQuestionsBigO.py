#  Created by Elshad Karimov on 3/26/20.
#  Copyright © 2020 Elshad Karimov. All rights reserved.

################ Interview Questions #############
#Question1
___ foo(array
    sum = 0
    product = 1
    ___ i __ array:
        sum += i
    ___ i __ array:
        product *= i
    print("Sum = "+str(sum)+", Product = "+str(product))

ar1 = [1,2,3,4]
foo(ar1)

#Question2

___ printPairs(array
    ___ i __ array:
        ___ j __ array:
            print(str(i)+","+str(j))


#Question3
___ printUnorderedPairs(array
    ___ i __ range(0,le_(array)):
        ___ j __ range(i+1,le_(array)):
            print(array[i] + "," + array[j])





#Question4
___ printUnorderedPairs(arrayA, arrayB
    ___ i __ range(le_(arrayA)):
        ___ j __ range(le_(arrayB)):
            __ arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]



#Question5
___ printUnorderedPairs(arrayA, arrayB
    ___ i __ range(le_(arrayA)):
        ___ j __ range(le_(arrayB)):
            ___ k __ range(0,100000
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# printUnorderedPairss(arrayA,arrayB)


#Question6
___ reverse(array
    ___ i __ range(0,int(le_(array)/2)):
        other = le_(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse(arrayA)

#Question8

___ factorial(n
    __ n < 0:
        r_ -1
    elif n == 0:
        r_ 1
    ____
        r_ n * factorial(n-1)

print(factorial(3))

#Question9
___ allFib(n
    ___ i __ range(n
        print(str(i)+":, " + str(fib(i)))

___ fib(n
    __ n <= 0:
        r_ 0
    elif n == 1:
        r_ 1
    r_ fib(n-1) + fib(n-2)


allFib(4)

#Question10
___ powersOf2(n
    # print("n:"+str(n))
    __ n < 1:
        r_ 0
    elif n == 1:
        print(1)
        r_ 1
    ____
        prev = powersOf2(int(n/2))
        # print("prev:"+str(prev))
        print(prev)
        curr = prev*2
        print(curr)
        r_ curr

powersOf2(50)