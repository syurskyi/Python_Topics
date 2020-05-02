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

headers = {'my-token' : '329uljsdf9f84oijrljfwe908u23orijdsk09asuioijr4ufeswijf39', 'User-Agent' : 'fake agent'}
r = requests.get('https://requestb.in/wpo4xjwp', headers=headers)