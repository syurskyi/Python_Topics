___ slices(series, length
    numbers = [int(digit) for digit in series]
    __ not 1 <= length <= le.(numbers
        raise ValueError("Invalid slice length for this series: " + str(
            length))
    r_ [numbers[i:i + length] for i in range(le.(numbers) - length + 1)]
