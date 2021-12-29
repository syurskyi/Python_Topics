
def bs(numbers,value):



    low,high = 0,len(numbers) - 1


    while low <= high:
        mid = (low + high)//2

        if numbers[mid] == value:
            return mid


        if value < numbers[mid]:
            high = mid - 1
        else:
            low = mid + 1








def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    


    mapping = {}

    
    result = None
    for i,number in enumerate(numbers):
        value = target - number
        if value < number and  value in mapping:
            index_1 = mapping[value]
            if not result or value < numbers[result[0]]:
                result = (index_1,i)
        

        if number not in mapping:
            mapping[number] = i



    return result






















