def find_number_pairs(numbers, N=10):

    seen = set()

    result = []
    for i in range(len(numbers) - 1):
        number_1 = numbers[i]
        for j in range(i + 1,len(numbers)):
            number_2 = numbers[j]

            if number_1 + number_2 == N:
                result.append((number_1,number_2))


    return result






