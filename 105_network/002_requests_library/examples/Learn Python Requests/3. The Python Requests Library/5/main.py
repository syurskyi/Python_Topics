import requests

#r = requests.get('https://requestb.in/wpo4xjwp')

'''
r = requests.get('https://reqres.in/api/users/2')
print(r.text)
json_data = r.json()
print(json_data['data']['first_name'])
'''

#r = requests.get('https://requestb.in/wpo4xjwp?key1=value1&key2=value2')

payload = {'first' : 'one', 'second' : 'two'}
r = requests.get('https://requestb.in/wpo4xjwp', params=payload)