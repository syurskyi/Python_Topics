from typing import Generator

VALUES = "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"


def calc_sums(values: str = VALUES) -> Generator[str, None, None]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    values_list = VALUES.strip("[]").split(", ")
    for i in range(1, len(values_list)):
        
        previous, current = float(values_list[i -1]), float(values_list[i])
        if previous < 0.1 and current < 0.1:
            total = previous + current
        else:
            total = round(previous, 2) + round(current, 2)

        yield f"The sum of {values_list[i -1]} and {values_list[i]}, rounded to two decimal places, is {total:.2f}."


# if __name__ == "__main__":
#     test = calc_sums()
#     print(next(test))
#     print(next(test))
#     print(next(test))
#     print(next(test))
#     print(next(test))