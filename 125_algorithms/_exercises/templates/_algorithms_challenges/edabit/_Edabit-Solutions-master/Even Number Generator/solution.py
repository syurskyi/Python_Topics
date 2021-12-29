___ find_even_nums(num):
    __ num < 2:
        return []
    index = 2
    output = []
    while index <= num:
        __ index % 2 == 0:
            output.append(index)
        index = index + 1

    return output
