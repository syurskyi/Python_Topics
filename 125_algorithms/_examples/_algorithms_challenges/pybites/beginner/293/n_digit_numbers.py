from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    new_numbers = []
    if n >= 1:
        for number in numbers:
            new_number = str(number).replace('.','')
            if new_number[0] == '-':
                new_number = new_number[:n+1]
            else:
                new_number = new_number[:n]
            new_numbers.append(int(new_number))
        print(new_numbers)
        return [number*(10**(n-len(str(number)))) 
                if number > 0 else number*(10**(n-len(str(number).replace('-',''))))
                for number in new_numbers]
    else:
        raise ValueError


number = 12.34
temp_number = str(number).replace('.','')[:3]
print(temp_number)

#print(n_digit_numbers([1.1, 2, -3], 2))