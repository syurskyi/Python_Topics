___ get_ordinal_suffix(number):
    '''Receives an int and returns it appended with its ordinal suffix,
       so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.'''
    __ 11 <= (number % 100) <= 13:
        ordinal = 'th'
    ____ str(number)[-1] __ '1':
        ordinal = 'st'
    ____ str(number)[-1] __ '2':
        ordinal = 'nd'
    ____ str(number)[-1] __ '3':
        ordinal = 'rd'
    ____:
        ordinal = 'th'
    r.. str(number) + ordinal