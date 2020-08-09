# Python 2.7
___ check_sum(data
    result = 0
    
    ___ number in data:
        result += number
        result *= 113
        result %= 10000007
    r_(result)

___ bubble_in_array(data
    numbers = [int(x) ___ x in data[:-1]]
    swap_count = 0

    ___ x in xrange(le.(numbers)-1
        __ numbers[x] > numbers[x+1]:
            numbers[x+1], numbers[x] = numbers[x], numbers[x+1]
            swap_count += 1
    print('%d %d') % (swap_count, check_sum(numbers))
    
bubble_in_array(raw_input().split())
