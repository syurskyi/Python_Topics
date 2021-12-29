def freq_digit(num: int) -> int:
    templist = [int(i) for i in str(num)]
    return max(templist, key = templist.count)




print(freq_digit(994145467))