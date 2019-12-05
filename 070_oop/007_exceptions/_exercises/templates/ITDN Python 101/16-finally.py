def function_that_may_fail():
    response = None
    while response != 'y' and response != 'n':
        response = input('Raise an exception? (y/n) ')
    if response == 'y':
        raise Exception


try:
    function_that_may_fail()
except:
    print('Exception handler')
finally:
    print('Finally block')