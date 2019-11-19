# pip install requests

# Тем, кто для работы с пакетами Python, использует виртуальную среду Pipenv,
# необходимо использовать немного другую команду.

# pipenv install requests


# Сразу после установки requests можно полноценно использовать в приложении.
# Импорт requests производится следующим образом.

import requests

# Python библиотека Requests метод GET
#
# Такие HTTP методы, как GET и POST, определяют, какие действия будут выполнены при создании HTTP запроса.
# Помимо GET и POST для этой задачи могут быть использованы некоторые другие методы.
# Далее они также будут описаны в руководстве.
# GET является одним из самых популярных HTTP методов.
# Метод GET указывает на то, что происходит попытка извлечь данные из определенного ресурса.
# Для того, чтобы выполнить запрос GET, используется requests.get().
# Для проверки работы команды будет выполнен запрос GET в отношении Root REST API на GitHub.
# Для указанного ниже URL вызывается метод get().

requests.get('https://api.github.com')
# <Response [200]>

# Объект Response получение ответа на запрос в Python
# Response представляет собой довольно мощный объект для анализа результатов запроса.
# В качестве примера будет использован предыдущий запрос, только на этот раз результат будет представлен
# в виде переменной. Таким образом, получится лучше изучить его атрибуты и особенности использования.

response = requests.get('https://api.github.com')

# В данном примере при помощи get() захватывается определенное значение, что является частью объекта Response,
# и помещается в переменную под названием response. Теперь можно использовать переменную response для того,
# чтобы изучить данные, которые были получены в результате запроса GET.
# HTTP коды состояний
# Самыми первыми данными, которые будут получены через Response, будут коды состояния.
# Коды состояния сообщают о статусе запроса.
# Например, статус 200 OK значит, что запрос успешно выполнен. А вот статус 404 NOT FOUND говорит о том,
# что запрашиваемый ресурс не был найден. Существует множество других статусных кодов,
# которые могут сообщить важную информацию, связанную с запросом.
# Используя .status_code, можно увидеть код состояния, который возвращается с сервера.

response.status_code
# 200

# .status_code вернул значение 200. Это значит, что запрос был выполнен успешно, а сервер ответил,
# отобразив запрашиваемую информацию.
#
# В некоторых случаях необходимо использовать полученную информацию для написания программного кода.

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

# В таком случае, если с сервера будет получен код состояния 200, тогда программа выведет значение Success!.
# Однако, если от сервера поступит код 404, тогда программа выведет значение Not Found.
# requests может значительно упростить весь процесс. Если использовать Response в условных конструкциях,
# то при получении кода состояния в промежутке от 200 до 400, будет выведено значение True.
# В противном случае отобразится значение False.
# Последний пример можно упростить при помощи использования оператора if.

if response:
    print('Success!')
else:
    print('An error has occurred.')

# Стоит иметь в виду, что данный способ не проверяет, имеет ли статусный код точное значение 200.
# Причина заключается в том, что другие коды в промежутке от 200 до 400, например, 204 NO CONTENT и 304 NOT MODIFIED,
# также считаются успешными в случае, если они могут предоставить действительный ответ.
# К примеру, код состояния 204 говорит о том, что ответ успешно получен, однако в полученном объекте нет содержимого.
# Можно сказать, что для оптимально эффективного использования способа необходимо убедиться,
# что начальный запрос был успешно выполнен.
# Требуется изучить код состояния и в случае необходимости произвести необходимые поправки,
# которые будут зависеть от значения полученного кода.
# Допустим, если при использовании оператора if вы не хотите проверять код состояния,
# можно расширить диапазон исключений для неудачных результатов запроса.
# Это можно сделать при помощи использования .raise_for_status().


import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # если ответ успешен, исключения задействованы не будут
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

# В случае вызова исключений через .raise_for_status() к некоторым кодам состояния применяется HTTPError.
# Когда код состояния показывает, что запрос успешно выполнен, программа продолжает работу без применения политики
# исключений.

# Анализ способов использования кодов состояния, полученных с сервера,
# является неплохим стартом для изучения requests. Тем не менее, при создании запроса GET,
# значение кода состояния является не самой важной информацией, которую хочет получить программист.
# Обычно запрос производится для извлечения более содержательной информации. В дальнейшем будет показано,
# как добраться до актуальных данных, которые сервер высылает отправителю в ответ на запрос.

# Получить содержимое страницы в Requests
#
# Зачастую ответ на запрос GET содержит весьма ценную информацию. Она находится в теле сообщения и
# называется пейлоад (payload).
# Используя атрибуты и методы библиотеки Response, можно получить пейлоад в различных форматах.

# Для того, чтобы получить содержимое запроса в байтах, необходимо использовать .content.

response = requests.get('https://api.github.com')
response.content
# b'{"current_user_url":"https://api.github.com/user","current_user_authorizations_
# html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_
# url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,
# per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}"
# ,"emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_
# url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_
# url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}",
# "gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search
# _url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues
# _url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys",
# "notifications_url":"https://api.github.com/notifications","organization_repositories_
# url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}",
# "organization_url":"https://api.github.com/orgs/{org}","public_gists_
# url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository
# _url":"https://api.github.com/repos/{owner}/{repo}","repository_search_
# url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user
# _repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_
# url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred",
# "team_url":"https://api.github.com/teams","user_url":"https://api.github.com/users/{user}","user_organizations_
# url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,
# page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}'

# Использование .content обеспечивает доступ к чистым байтам ответного пейлоада, то есть к любым данным в теле запроса.
# Однако, зачастую требуется конвертировать полученную информацию в строку в кодировке UTF-8.
# response делает это при помощи .text.

response.text
# '{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/
# settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_
# search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https:
# //api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/
# emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":
# "https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://
# api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://
# api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}",
# "issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","notifications_url":
# "https://api.github.com/notifications","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{
# ?type,page,per_page,sort}","organization_url":"https://api.github.com/orgs/{org}","public_gists_url":"https:/
# api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api
# .github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}
# {&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_
# page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.
# github.com/gists/starred","team_url":"https://api.github.com/teams","user_url":"https://api.github.com/users/{user}
# ","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/
# {user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}
# {&page,per_page,sort,order}"}'

# $ Декодирование байтов в строку требует наличия определенной модели кодировки. По умолчанию requests попытается
# узнать текущую кодировку, ориентируясь по заголовкам HTTP. Указать необходимую кодировку можно при помощи добавления
# .encoding перед .text.

response.encoding = 'utf-8' # Optional: requests infers this internally
response.text
# '{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/
# settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations",
# "code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":
# "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/
# user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":
# "https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.
# github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https:/
# /api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}",
# "issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","notifications_url":
# "https://api.github.com/notifications","organization_repositories_url":"https://api.github.com/orgs/{org}/repos
# {?type,page,per_page,sort}","organization_url":"https://api.github.com/orgs/{org}","public_gists_url":"https://
# api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.
# github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}
# {&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,
# sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.
# com/gists/starred","team_url":"https://api.github.com/teams","user_url":"https://api.github.com/users/{user}","user_
# organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/
# repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,
# sort,order}"}'

# Если присмотреться к ответу, можно заметить, что его содержимое является сериализированным JSON контентом.
# Воспользовавшись словарем, можно взять полученные из .text строки str и провести с ними обратную сериализацию при
# помощи использования json.loads(). Есть и более простой способ, который требует применения .json().

response.json()
# {'current_user_url': 'https://api.github.com/user', 'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}', 'authorizations_url': 'https://api.github.com/authorizations', 'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}', 'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}', 'emails_url': 'https://api.github.com/user/emails', 'emojis_url': 'https://api.github.com/emojis', 'events_url': 'https://api.github.com/events', 'feeds_url': 'https://api.github.com/feeds', 'followers_url': 'https://api.github.com/user/followers', 'following_url': 'https://api.github.com/user/following{/target}', 'gists_url': 'https://api.github.com/gists{/gist_id}', 'hub_url': 'https://api.github.com/hub', 'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}', 'issues_url': 'https://api.github.com/issues', 'keys_url': 'https://api.github.com/user/keys', 'notifications_url': 'https://api.github.com/notifications', 'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}', 'organization_url': 'https://api.github.com/orgs/{org}', 'public_gists_url': 'https://api.github.com/gists/public', 'rate_limit_url': 'https://api.github.com/rate_limit', 'repository_url': 'https://api.github.com/repos/{owner}/{repo}', 'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}', 'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}', 'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}', 'starred_gists_url': 'https://api.github.com/gists/starred', 'team_url': 'https://api.github.com/teams', 'user_url': 'https://api.github.com/users/{user}', 'user_organizations_url': 'https://api.github.com/user/orgs', 'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}', 'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}

# Тип полученного значения из .json(), является словарем. Это значит, что доступ к его содержимому можно получить по ключу.
# Коды состояния и тело сообщения предоставляют огромный диапазон возможностей. Однако, для их оптимального
# использования требуется изучить метаданные и заголовки HTTP.

# HTTP заголовки в Requests
#
# HTTP заголовки ответов на запрос могут предоставить определенную полезную информацию. Это может быть тип содержимого
# ответного пейлоада, а также ограничение по времени для кеширования ответа. Для просмотра HTTP заголовков
# загляните в атрибут .headers.

response.headers
# {'Server': 'GitHub.com', 'Date': 'Mon, 10 Dec 2018 17:49:54 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Status': '200 OK', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '59', 'X-RateLimit-Reset': '1544467794', 'Cache-Control': 'public, max-age=60, s-maxage=60', 'Vary': 'Accept', 'ETag': 'W/"7dc470913f1fe9bb6c7355b50a0737bc"', 'X-GitHub-Media-Type': 'github.v3; format=json', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Content-Encoding': 'gzip', 'X-GitHub-Request-Id': 'E439:4581:CF2351:1CA3E06:5C0EA741'}

# .headers возвращает словарь, что позволяет получить доступ к значению заголовка HTTP по ключу.
# Например, для просмотра типа содержимого ответного пейлоада, требуется использовать Content-Type.

response.headers['Content-Type']
# 'application/json; charset=utf-8'

#У объектов словарей в качестве заголовков есть своим особенности.
# Специфика HTTP предполагает, что заголовки не чувствительны к регистру. Это значит, что при получении доступа к
# заголовкам можно не беспокоится о том, использованы строчным или прописные буквы.

response.headers['content-type']
# 'application/json; charset=utf-8'

# При использовании ключей 'content-type' и 'Content-Type' результат будет получен один и тот же.
# Это была основная информация, требуемая для работы с Response. Были задействованы главные атрибуты и методы,
# а также представлены примеры их использования. В дальнейшем будет показано, как изменится ответ после
# настройки запроса GET.

# Python Requests параметры запроса
#
# Наиболее простым способом настроить запрос GET является передача значений через параметры строки запроса в URL.
# При использовании метода get(), данные передаются в params. Например, для того, чтобы посмотреть на библиотеку
# requests можно использовать Search API на GitHub.

import requests

# Поиск местонахождения для запросов на GitHub
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Анализ некоторых атрибутов местонахождения запросов
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+

# Передавая словарь {'q': 'requests+language:python'} в параметр params, который является частью .get(),
# можно изменить ответ, что был получен при использовании Search API.
# Можно передать параметры в get() в форме словаря, как было показано выше. Также можно использовать список кортежей.

requests.get(
    'https://api.github.com/search/repositories',
    params=[('q', 'requests+language:python')],
)
# <Response [200]>

# Также можно передать значение в байтах.

requests.get(
    'https://api.github.com/search/repositories',
    params=b'q=requests+language:python',
)
# <Response [200]>

# Строки запроса полезны для уточнения параметров в запросах GET.
# Также можно настроить запросы при помощи добавления или изменения заголовков отправленных сообщений.

# Настройка HTTP заголовка запроса (headers)
#
# Для изменения HTTP заголовка требуется передать словарь данного HTTP заголовка в get() при помощи использования
# параметра headers. Например, можно изменить предыдущий поисковой запрос, подсветив совпадения в результате.
# Для этого в заголовке Accept медиа тип уточняется при помощи text-match.

import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# просмотр нового массива `text-matches` с предоставленными данными
# о поиске в пределах результатов
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')

# Заголовок Accept сообщает серверу о типах контента, который можно использовать в рассматриваемом приложении.
# Здесь подразумевается, что все совпадения будут подсвечены, для чего в заголовке используется значение
# application/vnd.github.v3.text-match+json. Это уникальный заголовок Accept для GitHub.
# В данном случае содержимое представлено в специальном JSON формате.
# Перед более глубоким изучением способов редактирования запросов, будет не лишним остановиться на некоторых
# других методах HTTP.
# Примеры HTTP методов в Requests
# Помимо GET, большой популярностью пользуются такие методы, как POST, PUT, DELETE, HEAD, PATCH и OPTIONS.
# Для каждого из этих методов существует своя сигнатура, которая очень похожа на метод get().


requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key':'value'})
requests.options('https://httpbin.org/get')

# Каждая функция создает запрос к httpbin сервису, используя при этом ответный HTTP метод.
# Результат каждого метода можно изучить способом, который был использован в предыдущих примерах.

response = requests.head('https://httpbin.org/get')
response.headers['Content-Type']
# 'application/json'

response = requests.delete('https://httpbin.org/delete')
json_response = response.json()
json_response['args']
# {}

# При использовании каждого из данных методов в Response могут быть возвращены заголовки, тело запроса,
# коды состояния и многие другие аспекты. Методы POST, PUT и PATCH в дальнейшем будут описаны более подробно.
# Python Requests тело сообщения
# В соответствии со спецификацией HTTP запросы POST, PUT и PATCH передают информацию через тело сообщения,
# а не через параметры строки запроса. Используя requests, можно передать данные в параметр data.
# В свою очередь data использует словарь, список кортежей, байтов или объект файла. Это особенно важно,
# так как может возникнуть необходимость адаптации отправляемых с запросом данных в соответствии с
# определенными параметрами сервера.
# К примеру, если тип содержимого запроса application/x-www-form-urlencoded, можно отправить данные формы в
# виде словаря.

requests.post('https://httpbin.org/post', data={'key':'value'})
# <Response [200]>

# Ту же самую информацию также можно отправить в виде списка кортежей.

requests.post('https://httpbin.org/post', data=[('key', 'value')])
# <Response [200]>

# В том случае, если требуется отравить данные JSON, можно использовать параметр json. При передачи данных JSON через
# json, requests произведет сериализацию данных и добавит правильный Content-Type заголовок.
# Стоит взять на заметку сайт httpbin.org. Это чрезвычайно полезный ресурс, созданный человеком,
# который внедрил использование requests – Кеннетом Рейтцом. Данный сервис предназначен для тестовых запросов.
# Здесь можно составить пробный запрос и получить ответ с требуемой информацией.
# В качестве примера рассмотрим базовый запрос с использованием POST.

response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
json_response['data']
# '{"key": "value"}'
json_response['headers']['Content-Type']
# 'application/json'

# Здесь видно, что сервер получил данные и HTTP заголовки, отправленные вместе с запросом. requests также
# предоставляет информацию в форме PreparedRequest.
# Python Requests анализ запроса
# При составлении запроса стоит иметь в виду, что перед его фактической отправкой на целевой сервер библиотека
# requests выполняет определенную подготовку. Подготовка запроса включает в себя такие вещи, как проверка заголовков
# и сериализация содержимого JSON.
# Если открыть .request, можно просмотреть PreparedRequest.

response = requests.post('https://httpbin.org/post', json={'key':'value'})
response.request.headers['Content-Type']
# 'application/json'

response.request.url
# 'https://httpbin.org/post'

response.request.body
# b'{"key": "value"}'

# Проверка PreparedRequest открывает доступ ко всей информации о выполняемом запросе. Это может быть пейлоад, URL,
# заголовки, аутентификация и многое другое.
# У всех описанных ранее типов запросов была одна общая черта – они представляли собой неаутентифицированные
# запросы к публичным API. Однако, подобающее большинство служб, с которыми может столкнуться пользователь,
# запрашивают аутентификацию.

# Python Requests аутентификация HTTP AUTH
#
# Аутентификация помогает сервису понять, кто вы. Как правило, вы предоставляете свои учетные данные на сервер,
# передавая данные через заголовок Authorization или пользовательский заголовок, определенной службы. Все функции
# запроса, которые вы видели до этого момента, предоставляют параметр с именем auth, который позволяет вам передавать
# свои учетные данные.

# Одним из примеров API, который требует аутентификации, является Authenticated User API на GitHub.
# Это конечная точка веб-сервиса, которая предоставляет информацию о профиле аутентифицированного пользователя.
# Чтобы отправить запрос API-интерфейсу аутентифицированного пользователя, вы можете передать свое имя пользователя
# и пароль на GitHub через кортеж в get().

from getpass import getpass
requests.get('https://api.github.com/user', auth=('username', getpass()))
# <Response [200]>

# Запрос выполнен успешно, если учетные данные, которые вы передали в кортеже auth, действительны.
# Если вы попытаетесь сделать этот запрос без учетных данных, вы увидите, что код состояния 401 Unauthorized.

requests.get('https://api.github.com/user')
# <Response [401]>

# Когда вы передаете имя пользователя и пароль в кортеже параметру auth, вы используете учетные данные при помощи
# базовой схемы аутентификации HTTP.
# Таким образом, вы можете создать тот же запрос, передав подробные учетные данные базовой аутентификации,
# используя HTTPBasicAuth.

from requests.auth import HTTPBasicAuth
from getpass import getpass
requests.get(
    'https://api.github.com/user',
    auth=HTTPBasicAuth('username', getpass())
)
# <Response [200]>

# Хотя вам не нужно явно указывать обычную аутентификацию, может потребоваться аутентификация с использованием другого
# метода. requests предоставляет другие методы аутентификации, например, HTTPDigestAuth и HTTPProxyAuth.
# Вы даже можете предоставить свой собственный механизм аутентификации. Для этого необходимо сначала создать
# подкласс AuthBase. Затем происходит имплементация __call__().

import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))

# Здесь пользовательский механизм TokenAuth получает специальный токен. Затем этот токен включается заголовок
# X-TokenAuth запроса.
# Плохие механизмы аутентификации могут привести к уязвимостям безопасности, поэтому, если службе по какой-то
# причине не нужен настраиваемый механизм аутентификации, вы всегда можете использовать проверенную схему
# аутентификации, такую как Basic или OAuth.
# Пока вы думаете о безопасности, давайте рассмотрим использование requests в SSL сертификатах

# Python Requests проверка SSL сертификата
# Всякий раз, когда данные, которые вы пытаетесь отправить или получить, являются конфиденциальными,
# безопасность важна. Вы общаетесь с защищенными сайтами через HTTP, устанавливая зашифрованное соединение с
# использованием SSL, что означает, что проверка SSL сертификата целевого сервера имеет решающее значение.
# Хорошей новостью является то, что requests по умолчанию все делает сам. Однако в некоторых случаях необходимо
# внести определенные поправки.
# Если требуется отключить проверку SSL-сертификата, параметру verify функции запроса можно присвоить значение False.

requests.get('https://api.github.com', verify=False)
# InsecureRequestWarning: Unverified HTTPS request is being made.
# Adding certificate verification is strongly advised.
# See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#   InsecureRequestWarning)
# <Response [200]>

#  случае небезопасного запроса requests предупреждает о возможности потери информации и просит сохранить
#  данные или отказаться от запроса.

# Примечание. Для предоставления сертификатов requests использует пакет, который вызывается certifi.
# Это дает понять requests, каким ответам можно доверять. Поэтому вам следует часто обновлять certifi,
# чтобы обеспечить максимальную безопасность ваших соединений.

# Python Requests производительность приложений
#
# При использовании requests, особенно в среде приложений, важно учитывать влияние на производительность.
# Такие функции, как контроль таймаута, сеансы и ограничения повторных попыток, могут помочь обеспечить
# бесперебойную работу приложения.
# Таймауты
#
# Когда вы отправляете встроенный запрос во внешнюю службу, вашей системе нужно будет дождаться ответа,
# прежде чем двигаться дальше. Если ваше приложение слишком долго ожидает ответа, запросы к службе могут быть сохранены,
# пользовательский интерфейс может пострадать или фоновые задания могут зависнуть.
#
# По умолчанию в requests на ответ время не ограничено, и весь процесс может занять значительный промежуток.
# По этой причине вы всегда должны указывать время ожидания, чтобы такого не происходило. Чтобы установить время
# ожидания запроса, используйте параметр timeout. timeout может быть целым числом или числом с плавающей точкой,
# представляющим количество секунд ожидания ответа до истечения времени ожидания.

requests.get('https://api.github.com', timeout=1)
# <Response [200]>
requests.get('https://api.github.com', timeout=3.05)
# <Response [200]>

# В первом примере запрос истекает через 1 секунду. Во втором примере запрос истекает через 3,05 секунды.
# Вы также можете передать кортеж. Это – таймаут соединения (время, за которое клиент может установить соединение
# с сервером), а второй – таймаут чтения (время ожидания ответа, как только ваш клиент установил соединение):

requests.get('https://api.github.com', timeout=(2, 5))
# <Response [200]>

# Если запрос устанавливает соединение в течение 2 секунд и получает данные в течение 5 секунд после установления
# соединения, то ответ будет возвращен, как это было раньше. Если время ожидания истекло,
# функция вызовет исключение Timeout.

import requests
from requests.exceptions import Timeout

try:
    response = requests.get('https://api.github.com', timeout=1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')


# Ваша программа может поймать исключение Timeout и ответить соответственно.
# Объект Session в Requests
#
# До сих пор вы имели дело с requests API высокого уровня, такими как get() и post(). Эти функции являются
# абстракцией того, что происходит, когда вы делаете свои запросы. Они скрывают детали реализации,
# такие как управление соединениями, так что вам не нужно о них беспокоиться.
#
# Под этими абстракциями находится класс под названием Session. Если вам необходимо настроить контроль над выполнением
# запросов или повысить производительность ваших запросов, вам может потребоваться использовать Session напрямую.

# Сессии используются для сохранения параметров в запросах.

# Например, если вы хотите использовать одну и ту же аутентификацию для нескольких запросов,
# вы можете использовать сеанс:

import requests
from getpass import getpass

# используя менеджер контента, можно убедиться, что ресурсы, применимые
# во время сессии будут свободны после использования
with requests.Session() as session:
    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')

# здесь можно изучить ответ
print(response.headers)
print(response.json())

# Каждый раз, когда вы делаете запрос session, после того как он был инициализирован с учетными данными аутентификации,
# учетные данные будут сохраняться.

# Первичная оптимизация производительности сеансов происходит в форме постоянных соединений.
# Когда ваше приложение устанавливает соединение с сервером с помощью Session, оно сохраняет это соединение
# в пуле соединений. Когда ваше приложение снова хочет подключиться к тому же серверу, оно будет использовать
# соединение из пула, а не устанавливать новое.

# HTTPAdapter — Максимальное количество повторов запроса в Requests
#
# В случае сбоя запроса возникает необходимость сделать повторный запрос. Однако requests не будет делать
# это самостоятельно. Для применения функции повторного запроса требуется реализовать собственный транспортный адаптер.

# Транспортные адаптеры позволяют определить набор конфигураций для каждой службы, с которой вы взаимодействуете.
# Предположим, вы хотите, чтобы все запросы к https://api.github.com были повторены три раза, прежде чем, наконец,
# появится ConnectionError. Для этого нужно построить транспортный адаптер, установить его параметр max_retries и
# подключить его к существующему объекту Session.

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# использование `github_adapter` для всех запросов, которые начинаются с указанным URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)

