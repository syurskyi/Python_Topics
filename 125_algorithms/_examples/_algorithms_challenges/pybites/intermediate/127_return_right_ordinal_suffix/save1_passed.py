def get_ordinal_suffix(number):
    '''Receives an int and returns it appended with its ordinal suffix,
       so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.'''
    if 11 <= (number % 100) <= 13:
        ordinal = 'th'
    elif str(number)[-1] == '1':
        ordinal = 'st'
    elif str(number)[-1] == '2':
        ordinal = 'nd'
    elif str(number)[-1] == '3':
        ordinal = 'rd'
    else:
        ordinal = 'th'
    return str(number) + ordinal