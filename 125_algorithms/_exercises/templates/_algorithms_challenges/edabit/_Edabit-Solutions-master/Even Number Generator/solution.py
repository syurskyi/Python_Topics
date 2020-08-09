___ find_even_nums(num
    __ num < 2:
        r_ []
    index = 2
    output = []
    w___ index <= num:
        __ index % 2 __ 0:
            output.append(index)
        index = index + 1

    r_ output
