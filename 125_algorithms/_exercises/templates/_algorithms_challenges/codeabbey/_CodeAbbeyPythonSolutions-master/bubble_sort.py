amount_values = int(input())

___ get_pass_and_swap_number(array):
    passed = 0
    swapped = 0

    n = l..(array)
    ___ i __ r..(n):
        previous_swap = swapped
        ___ j __ r..(n-i-1):
            __(array[j] > array[j+1]):
                swapped += 1
                array[j], array[j+1] = array[j+1], array[j]
        passed += 1

        __(previous_swap __ swapped):
            break  
    

    print (passed, swapped)

array = l..(map(int, input().split()))
get_pass_and_swap_number(array)