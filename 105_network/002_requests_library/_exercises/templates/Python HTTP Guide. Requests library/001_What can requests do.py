# Для начала хочется показать как выглядит код работы с http, используя модули из стандартной библиотеки
# Python и код при работе с requests. В качестве мишени для стрельбы http запросами будет использоваться
# очень удобный сервис httpbin.org

import urllib.request
response = urllib.request.urlopen('https://httpbin.org/get')
print(response.read())
# b'{\n  "args": {}, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Host": "httpbin.org",
# \n    "User-Agent": "Python-urllib/3.5"\n  }, \n  "origin": "95.56.82.136", \n  "url": "https://httpbin.org/get"\n}\n'
print(response.getheader('Server'))
# nginx
print(response.getcode())
# 200