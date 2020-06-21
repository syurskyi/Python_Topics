try:
    try:
        raise ValueError('incorrect value')
    except ZeroDivisionError:
        print('division by zero')
except Exception as e:
    print(e)
