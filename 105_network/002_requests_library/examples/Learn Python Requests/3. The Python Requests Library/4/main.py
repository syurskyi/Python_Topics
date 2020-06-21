import requests

#r = requests.get('https://requestb.in/wpo4xjwp')

r = requests.get('https://reqres.in/api/users/2')
print(r.text)
json_data = r.json()
print(json_data['data']['first_name'])