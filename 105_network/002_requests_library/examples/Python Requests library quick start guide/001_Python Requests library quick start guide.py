# Импортируйте модуль Requests:

import requests

# Попробуем получить веб-страницу. В этом примере давайте рассмотрим общий тайм-лайн GitHub:

r = requests.get('https://api.github.com/events')

# Мы получили объект Response с именем r. С помощью этого объекта можно получить всю необходимую информацию.
# Простой API Requests означает, что все формы HTTP запросов- очевидны. Ниже приведен пример того,
# как вы можете сделать запрос HTTP POST:

r = requests.post('http://httpbin.org/post', data={'key': 'value'})

# Другие типы HTTP запросов такие как : PUT, DELETE, HEAD и OPTIONS так же очень легко выполнить:

r = requests.put('http://httpbin.org/put', data={'key': 'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

# Передача параметров в URL
# Часто вам может понадобится отправить какие-то данные в строке запроса URL. Если вы настраиваете URL вручную,
# эти данные будут представлены в нем в виде пар ключ/значение после знака вопроса. Например, httpbin.org/get?key=val.
# Requests позволяет передать эти аргументы в качестве словаря, используя аргумент params.
# Если вы хотите передать key1=value1 и key2=value2 ресурсу httpbin.org/get, вы должны использовать следующий код:

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

# http://httpbin.org/get?key2=value2&key1=value1

# Ключ словаря, значение которого None не будет добавлен в строке запроса URL.
# Вы можете передать список параметров в качестве значения:

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

# http://httpbin.org/get?key1=value1&key2=value2&key2=value3


# Содержимое ответа (response)
#
# Мы можем прочитать содержимое ответа сервера. Рассмотрим снова тайм-лайн GitHub:

import requests
r = requests.get('https://api.github.com/events')
r.text

# Requests будет автоматически декодировать содержимое ответа сервера.
# Большинство кодировок unicode декодируются без проблем.
# Когда вы делаете запрос, Requests делает предположение о кодировке, основанное на заголовках HTTP.
# Эта же кодировка текста, используется при обращение к r.text. Можно узнать, какую кодировку использует Requests,
# и изменить её с помощью r.encoding:

print(r.encoding)

# 'utf-8'

# Если вы измените кодировку, Requests будет использовать новое значение r.encoding всякий раз,
# когда вы будете использовать r.text. Вы можете сделать это в любой ситуации,
# где нужна более специализированная логика работы с кодировкой содержимого ответа.
# Например, в HTML и XML есть возможность задавать кодировку прямо в теле документа.
# В подобных ситуациях вы должны использовать r.content, чтобы найти кодировку, а затем установить r.encoding.
# Это позволит вам использовать r.text с правильной кодировкой.
#
# Requests может также использовать пользовательские кодировки в случае, если в них есть потребность.
# Если вы создали свою собственную кодировку и зарегистрировали ее в модуле codecs,
# используйте имя кодека в качестве значения r.encoding.

# Бинарное содержимое ответа
# Вы можете также получить доступ к телу ответа в виде байтов для не текстовых ответов:

r.content

# b'[{"repository":{"open_issues":0,"url":"https://github.com/...

# Передача со сжатием gzip и deflate автоматически декодируются для вас.
# Например, чтобы создать изображение на основе бинарных данных, возвращаемых при ответе на запрос, используйте следующий код:

from PIL import Image
from io import BytesIO
i = Image.open(BytesIO(r.content))

# Содержимое ответа в JSON
# Если вы работаете с данными в формате JSON, воспользуйтесь встроенным JSON декодером:

import requests
r = requests.get('https://api.github.com/events')
r.json()

# [{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...

# Если декодирование в JSON не удалось, r.json() вернет исключение. Например, если ответ с кодом 204 (No Content),
# или на случай если ответ содержит не валидный JSON, попытка обращения к r.json()
# будет возвращать ValueError: No JSON object could be decoded.
# Следует отметить, что успешный вызов r.json() не указывает на успешный ответ сервера.
# Некоторые серверы могут возвращать объект JSON при неудачном ответе (например, сведения об ошибке HTTP 500).
# Такой JSON будет декодирован и возвращен. Для того, чтобы проверить успешен ли запрос, используйте r.raise_
# for_status() или проверьте какой r.status_code.
# Необработанное содержимое ответа
# В тех редких случаях, когда вы хотите получить доступ к “сырому” ответу сервера на уровне сокета,
# обратитесь к r.raw. Если вы хотите сделать это, убедитесь, что вы указали stream=True в вашем первом запросе.
# После этого вы уже можете проделать следующее:

r = requests.get('https://api.github.com/events', stream=True)
r.raw

# <urllib3.response.HTTPResponse object at 0x101194810>

r.raw.read(10)

# '\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'

# Однако, можно использовать подобный код как шаблон, чтобы сохранить результат в файл:

with open(filename, 'wb') as fd:
	for chunk in r.iter_content(chunk_size=128):
		fd.write(chunk)

# Использование r.iter_content обработает многое из того, с чем бы вам пришлось иметь дело при использовании r.raw
# напрямую. Для извлечения содержимого при потоковой загрузке, используйте способ, описанный выше.
# Обратите внимание, что chunk_size можно свободно скорректировать до числа, которое лучше подходит в вашем случае.

# Пользовательские заголовки
# Если вы хотите добавить HTTP заголовки в запрос, просто передайте соответствующий dict в параметре headers.
# Например, мы не указали наш user-agent в предыдущем примере:

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

# Заголовкам дается меньший приоритет, чем более конкретным источникам информации. Например:
#
#     Заголовки авторизации, установленные с помощью headers= будут переопределены, если учетные данные указаны
#     .netrc, которые, в свою очередь переопределены параметром auth=.
#     Заголовки авторизации будут удалены при редиректе.
#     Заголовки авторизации с прокси будут переопределены учетными данными прокси-сервера, которые указаны в вашем URL.
#     Заголовки Content-Length будут переопределены, когда вы определите длину содержимого.
#
# Кроме того, запросы не меняют свое поведение вообще, основываясь на указанных пользовательских заголовках.

# Более сложные POST запросы
# Часто вы хотите послать некоторые form-encoded данные таким же образом, как это делается в HTML форме.
# Для этого просто передайте соответствующий словарь в аргументе data. Ваш словарь данных в таком случае
# будет автоматически закодирован как HTML форма, когда будет сделан запрос:

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
# {
# 	...
# 	"form": {
# 	  "key2": "value2",
# 	  "key1": "value1"
# 	},
# 	...
# }

# Аргумент data также может иметь несколько значений для каждого ключа. Это можно сделать, указав data в формате tuple,
# либо в виде словаря со списками в качестве значений. Особенно полезно, когда форма имеет несколько элементов,
# которые используют один и тот же ключ:
# Аргумент data также может иметь несколько значений для каждого ключа. Это можно сделать, указав data в формате tuple,
# либо в виде словаря со списками в качестве значений. Особенно полезно, когда форма имеет несколько элементов,
# которые используют один и тот же ключ:

payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('http://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('http://httpbin.org/post', data=payload_dict)
print(r1.text)
# {
# 	...
# 	"form": {
# 	  "key1": [
# 		"value1",
# 		"value2"
# 	  ]
# 	},
# 	...
# }
r1.text == r2.text

# True

# Бывают случаи, когда нужно отправить данные не закодированные методом form-encoded. Если вы передадите в запрос строку
# вместо словаря, эти данные отправятся в не измененном виде.
# К примеру, GitHub API v3 принимает закодированные JSON POST/PATCH данные:

import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))

# Вместо того, чтобы кодировать dict, вы можете передать его напрямую, используя параметр json
# (добавленный в версии 2.4.2), и он будет автоматически закодирован:

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)

# Обратите внимание, параметр json игнорируется, если передаются data или files.
# Использование параметра json в запросе изменит заголовок Content-Type на application/json.
# POST отправка Multipart-Encoded файла

# Запросы упрощают загрузку файлов с многостраничным кодированием (Multipart-Encoded) :

url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
r.text
# {
# 	...
# 	"files": {
# 	  "file": "<censored...binary...data>"
# 	},
# 	...
# }

# Вы можете установить имя файла, content_type и заголовки в явном виде:

url = 'http://httpbin.org/post'
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
r = requests.post(url, files=files)
r.text
# {
# 	...
# 	"files": {
# 	  "file": "<censored...binary...data>"
# 	},
# 	...
# }

# Можете отправить строки, которые будут приняты в виде файлов:

url = 'http://httpbin.org/post'
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url, files=files)
r.text
# {
# 	...
# 	"files": {
# 	  "file": "some,data,to,send\\nanother,row,to,send\\n"
# 	},
# 	...
# }

# В случае, если вы отправляете очень большой файл как запрос multipart/form-data, возможно понадобиться отправить запрос потоком. По умолчанию, requests не поддерживает этого, но есть отдельный пакет, который это делает — requests-toolbelt. Ознакомьтесь с документацией toolbelt для получения более детальной информации о том, как им пользоваться.

# Предупреждение!
# Настоятельно рекомендуется открывать файлы в бинарном режиме. Это связано с тем, что запросы могут пытаться предоставить для вас заголовок Content-Length, и если это значение будет установлено на количество байтов в файле будут возникать ошибки, при открытии файла в текстовом режиме.

# Коды состояния ответа
# Мы можем проверить код состояния ответа:

r = requests.get('http://httpbin.org/get')
r.status_code

# 200

# У requests есть встроенный объект вывода кодов состояния:

r.status_code == requests.codes.ok

# True

bad_r = requests.get('http://httpbin.org/status/404')
bad_r.status_code

# 404
bad_r.raise_for_status()

# Traceback (most recent call last):
# File "requests/models.py", line 832, in raise_for_status
# raise http_error
# requests.exceptions.HTTPError: 404 Client Error

# Но если status_code для r оказался 200, то когда мы вызываем raise_for_status() мы получаем:

r.raise_for_status()

# Заголовки ответов
# Мы можем просматривать заголовки ответа сервера, используя словарь Python:

r.headers

# {
# 	'content-encoding': 'gzip',
# 	'transfer-encoding': 'chunked',
# 	'connection': 'close',
# 	'server': 'nginx/1.0.4',
# 	'x-runtime': '148ms',
# 	'etag': '"e1ca502697e5c9317743dc078f67693f"',
# 	'content-type': 'application/json'
# }

# Это словарь особого рода, он создан специально для HTTP заголовков. Согласно с RFC 7230, имена заголовков HTTP нечувствительны к регистру:
# Теперь мы можем получить доступ к заголовкам с большми буквами или без, если захотим:

r.headers['Content-Type']

# 'application/json'
r.headers.get('content-type')

# 'application/json'

# Cookies
# Если в запросе есть cookies, вы сможете быстро получить к ним доступ:

url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']

# 'example_cookie_value'

# Чтобы отправить собственные cookies на сервер, используйте параметр cookies:

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text
# '{"cookies": {"cookies_are": "working"}}'

# Cookies возвращаются в RequestsCookieJar, который работает как dict, но также предлагает более полный интерфейс,
# подходящий для использования в нескольких доменах или путях. Cookie jars могут также передаваться в запросы:

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
r.text

'{"cookies": {"tasty_cookie": "yum"}}'

# Редиректы и история
# По умолчанию Requests будет выполнять редиректы для всех HTTP глаголов, кроме HEAD.
# Мы можем использовать свойство history объекта Response, чтобы отслеживать редиректы .
# Список Response.history содержит объекты Response, которые были созданы для того, чтобы выполнить запрос.
# Список сортируется от более ранних, до более поздних ответов.
# Например, GitHub перенаправляет все запросы HTTP на HTTPS:

r = requests.get('http://github.com')
r.url

'https://github.com/'
r.status_code

# 200
r.history

# [<Response [301]>]

# Если вы используете GET, OPTIONS, POST, PUT, PATCH или DELETE, вы можете отключить обработку редиректа
# с помощью параметра allow_redirects:

r = requests.get('http://github.com', allow_redirects=False)
r.status_code

# 301
r.history

# []

# Если вы используете HEAD, вы также можете включить редирект:

r = requests.head('http://github.com', allow_redirects=True)
r.url

# 'https://github.com/'
r.history

# [<Response [301]>]

# Тайм-ауты
# Вы можете сделать так, чтобы Requests прекратил ожидание ответа после определенного количества секунд
# с помощью параметра timeout:
# Почти весь производственный код должен использовать этот параметр почти во всех запросах.
# Несоблюдение этого требования может привести к зависанию вашей программы:

requests.get('http://github.com', timeout=0.001)

# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)