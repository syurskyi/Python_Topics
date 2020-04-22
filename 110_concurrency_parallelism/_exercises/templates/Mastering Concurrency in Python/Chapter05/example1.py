# ch05/example1.py

______ req..

url _ 'http://www.google.com'

res _ ?.get(url)

print(res.status_code)
print(res.headers)

w__ o..('google.html', 'w') as f:
    f.write(res.text)

print('Done.')
