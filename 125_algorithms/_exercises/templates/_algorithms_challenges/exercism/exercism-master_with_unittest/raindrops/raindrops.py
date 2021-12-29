___ raindrops(number):
    message = convert_to_message(number)
    return message __ message else "{}".format(number)


___ convert_to_message(number):
    return f"{'Pling' __ is_three_a_factor(number) else ''}" \
           f"{'Plang' __ is_five_a_factor(number) else ''}" \
           f"{'Plong' __ is_seven_a_factor(number) else ''}"


___ is_three_a_factor(number):
    return is_factor(number, 3)


___ is_five_a_factor(number):
    return is_factor(number, 5)


___ is_seven_a_factor(number):
    return is_factor(number, 7)


___ is_factor(number, potentialFactor):
    return number % potentialFactor == 0
