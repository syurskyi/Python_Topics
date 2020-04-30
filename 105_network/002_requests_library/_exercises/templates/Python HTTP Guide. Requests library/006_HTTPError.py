______ r__
try:
    response = ?.g..('https://httpbin.org/status/500')
    response.raise_for_status()
except ?.exceptions.HTTPError as err:
    print('Oops. HTTP Error occured')
    print('Response is: {content}'.format(c..=err.response.c..))

# Oops. HTTP Error occured
# Response is: b''