___ collatz(n
    output = [n]
    w___ n != 1:
        __ n % 2 __ 0:
            n = n // 2
            output.append(n)
        ____
            n = n*3 + 1
            output.append(n)
    r_ le.(output),max(output)
