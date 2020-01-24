def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all_nums(4, 6, 9, 4, 10))
print(sum_all_nums(4, 6))
