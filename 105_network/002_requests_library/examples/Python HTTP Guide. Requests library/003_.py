# В простых методах запросов значительных отличий у них не имеется. Но давайте взглянем на работы с Basic Auth:

import urllib.request
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = 'https://httpbin.org/basic-auth/user/passwd'
password_mgr.add_password(None, top_level_url, 'user', 'passwd')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
response = opener.open(top_level_url)
print(response.getcode())
# 200
print(response.read())
# b'{\n  "authenticated": true, \n  "user": "user"\n}\n'


import requests
response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))
print(response.content)
# b'{\n  "authenticated": true, \n  "user": "user"\n}\n'
print(response.json())
# {'user': 'user', 'authenticated': True}

# А теперь чувствуется разница между pythonic и non-pythonic? Я думаю разница на лицо.
# И несмотря на тот факт, что requests ничто иное как обёртка над urllib3,
# а последняя является надстройкой над стандартными средствами Python,
# удобство написания кода в большинстве случаев является приоритетом номер один.
#
# В requests имеется:
#
#     Множество методов http аутентификации
#     Сессии с куками
#     Полноценная поддержка SSL
#     Различные методы-плюшки вроде .json(), которые вернут данные в нужном формате
#     Проксирование
#     Грамотная и логичная работа с исключениями
