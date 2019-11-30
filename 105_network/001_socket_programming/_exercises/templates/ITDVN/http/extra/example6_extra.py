import json

import requests
from requests.adapters import HTTPAdapter

HOST = '127.0.0.1:8000'


def get_url(path):
    return 'http://{host}{path}'.format(host=HOST, path=path)


issues_url = get_url('/api/issues/')
login_url = get_url('/api/auth/login/')
logout_url = get_url('/api/auth/logout/')


def issue_url(pk):
    return get_url('/api/issues/{id}/'.format(id=pk))


# get issues (error)
response = requests.get(issues_url)
print(response.status_code)
print(response.json())

# auth and get issues
data = {'username': 'test_user', 'password': 'test_pass'}
headers = {'Content-Type': 'application/json'}
response = requests.post(login_url, data=json.dumps(data), headers=headers)
print(response.status_code)
print(response.json())

cookies = response.cookies

response = requests.get(issues_url, cookies=cookies)
print(response.status_code)
print(response.json())

# create issue (error: without data)
response = requests.post(issues_url, cookies=cookies)
print(response.status_code)
print(response.json())

issue_data = {'name': 'Buy Python Book',
              'due_date': '2009-02-11',
              'description': 'We have to buy a Python book!!!'}

# create issue (success: without data)
response = requests.post(issues_url, data=json.dumps(issue_data),
                         headers=headers, cookies=cookies)
created_issue = response.json()
print(response.status_code)
print(created_issue)

# patch issue
new_data = {'name': 'Fixed name'}
response = requests.patch(issue_url(created_issue['id']),
                          data=json.dumps(new_data), headers=headers,
                          cookies=cookies)
print(response.status_code)
print(response.json())

# delete issue
response = requests.delete(issue_url(created_issue['id']), cookies=cookies)
print(response.status_code)
# print(response.json())

# SESSION EXAMPLE

# auth and get issues
data = {'username': 'test_user', 'password': 'test_pass'}
headers = {'Content-Type': 'application/json'}
session = requests.Session()
response = session.post(login_url, data=json.dumps(data), headers=headers)
print(response.status_code)
print(response.json())

cookies = response.cookies

response = session.get(issues_url)
print(response.status_code)
print(response.json())

# create issue (error: without data)
response = session.post(issues_url)
print(response.status_code)
print(response.json())

# POOL MANAGER

adapter = HTTPAdapter(pool_maxsize=10, pool_block=True, pool_connections=10)
session = requests.Session()
session.mount('http://', adapter=adapter)
session.post(issues_url)
