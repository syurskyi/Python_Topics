def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

# sum_all_values(1,30,2,5,6)


nums = [1,2,3,4,5,6]
sum_all_values(*nums)


