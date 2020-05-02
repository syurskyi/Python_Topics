import requests

#r = requests.get('https://requestb.in/wpo4xjwp')

'''
r = requests.get('https://reqres.in/api/users/2')
print(r.text)
json_data = r.json()
print(json_data['data']['first_name'])
'''

#r = requests.get('https://requestb.in/wpo4xjwp?key1=value1&key2=value2')

'''
payload = {'first' : 'one', 'second' : 'two'}
r = requests.get('https://requestb.in/wpo4xjwp', params=payload)
'''

'''
headers = {'my-token' : '329uljsdf9f84oijrljfwe908u23orijdsk09asuioijr4ufeswijf39', 'User-Agent' : 'fake agent'}
r = requests.get('https://requestb.in/wpo4xjwp', headers=headers)
'''

#r = requests.post('https://requestb.in/wpo4xjwp')

#r = requests.delete('https://requestb.in/wpo4xjwp')

#r = requests.put('https://requestb.in/wpo4xjwp')

#r = requests.patch('https://requestb.in/wpo4xjwp')

'''
payload = {'name' : 'Anthony', 'job' : 'Programmer'}
r = requests.post('https://reqres.in/api/users', json=payload)
print(r)
print(r.text)
'''

'''
payload = {'name' : 'Anthony', 'location' : 'Las Vegas'}
#r = requests.post('https://requestb.in/wpo4xjwp', data=payload)
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
'''

'''
files = {'file' : open('cat.jpg', 'rb')}
r = requests.post('https://requestb.in/wpo4xjwp', files=files)
'''

'''
files = {'file' : ('cat.jpg', open('cat.jpg', 'rb'), 'image/jpeg')}
r = requests.post('https://requestb.in/wpo4xjwp', files=files)
'''

'''
r = requests.get('https://httpbin.org/image/jpeg')
print(r.headers)

with open('image.jpg', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=500):
        fd.write(chunk)
'''

'''
r = requests.get('https://httpbin.org/status/501')

try:
    r.raise_for_status()
except requests.exceptions.HTTPError:
    print('ERROR! ERROR! ERROR!')

print(r)
'''


try:
    r = requests.get('https://dsklfjdslfudsfdsj.com')
except requests.exceptions.ConnectionError:
    print('CONNECTION ERROR!')