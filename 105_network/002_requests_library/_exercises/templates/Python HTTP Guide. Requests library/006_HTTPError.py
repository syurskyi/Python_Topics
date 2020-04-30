______ r__
___
    response = ?.g..('https://httpbin.org/status/500')
    response.raise_for_status()
_____ ?.e__.HTTPError as err:
    print('Oops. HTTP Error occured')
    print('Response is: {content}'.format(c..=err.response.c..))

# Oops. HTTP Error occured
# Response is: b''