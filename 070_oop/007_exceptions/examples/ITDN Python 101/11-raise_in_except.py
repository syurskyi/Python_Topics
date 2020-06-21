try:
    try:
        raise ValueError('value is incorrect')
    except ValueError as error:
        print('Exception:', error)
        raise
except ValueError:
    print('ValueError detected')
