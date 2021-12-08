def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)

my_nums = square_numbers(1,2,3,4,5)

for num in my_nums:
    print(num)