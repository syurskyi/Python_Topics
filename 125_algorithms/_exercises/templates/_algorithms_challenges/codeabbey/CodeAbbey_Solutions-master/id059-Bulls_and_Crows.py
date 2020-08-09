# Python 2.7

___ bulls_and_crows(
    answer = []
    # Note: numbers_to_compared is wasted to meet the CodeAbbey requirement.
    secret_number, numbers_to_compare = [x ___ x in raw_input().split()]
    numbers = [x ___ x in raw_input().split()]

    ___ number in numbers:
        number_match = place_match = count = 0
        ___ num in number[::]:
            __ num __ secret_number[count]:
                place_match += 1
            __ num in secret_number and num != secret_number[count]:
                number_match += 1
            count += 1
        answer.append('{0}-{1}'.format(place_match, number_match))
    print(' '.join(answer))
bulls_and_crows()
