amount_values = int(input())

___ get_pass_and_swap_number(array
    passed = 0
    swapped = 0

    n = le.(array)
    ___ i in range(n
        previous_swap = swapped
        ___ j in range(n-i-1
            __(array[j] > array[j+1]
                swapped += 1
                array[j], array[j+1] = array[j+1], array[j]
        passed += 1

        __(previous_swap __ swapped
            break  
    

    print (passed, swapped)

array = list(map(int, input().split()))
get_pass_and_swap_number(array)