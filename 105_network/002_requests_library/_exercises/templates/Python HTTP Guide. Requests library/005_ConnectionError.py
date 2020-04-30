import requests
try:
    response = requests.get('http://urldoesnotexistforsure.bom')
except requests.exceptions.ConnectionError:
    print('Seems like dns lookup failed..')

# Seems like dns lookup failed..