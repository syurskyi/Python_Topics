
___ bs(numbers,value



    low,high 0,l.. ?) - 1


    w.... low <_ high:
        mid (low + high)//2

        __ numbers[mid] __ value:
            r.. mid


        __ value < numbers[mid]:
            high mid - 1
        ____
            low mid + 1








___ two_sums(numbers, target
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    


    mapping    # dict

    
    result N..
    ___ i,number __ e.. ?
        value target - number
        __ value < number a..  value __ mapping:
            index_1 mapping[value]
            __ n.. result o. value < numbers[result[0]]:
                result (index_1,i)
        

        __ number n.. __ mapping:
            mapping[number] i



    r.. ?






















