import requests
try:
    response = requests.get('https://httpbin.org/status/500')
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print('Oops. HTTP Error occured')
    print('Response is: {content}'.format(content=err.response.content))

# Oops. HTTP Error occured
# Response is: b''