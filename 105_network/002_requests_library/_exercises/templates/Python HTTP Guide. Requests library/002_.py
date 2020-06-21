# # Кстати, urllib.request это надстройка над "низкоуровневой" библиотекой httplib о которой я писал выше.
#
# ______ r__
# response = ?.g.. 'https://httpbin.org/get'
# print ?.c..
# # b'{\n  "args": {}, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n
# # "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.9.1"\n  }, \n  "origin": "95.56.82.136", \n
# # "url": "https://httpbin.org/get"\n}\n'
# ?.j..
# # {'headers': {'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'python-requests/2.9.1', 'Host': 'httpbin.org',
# # 'Accept': '*/*'}, 'args': {}, 'origin': '95.56.82.136', 'url': 'https://httpbin.org/get'}
# ?.h..
# # {'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Server': 'nginx',
# # 'Access-Control-Allow-Credentials': 'true', 'Access-Control-Allow-Origin': '*', 'Content-Length': '237',
# # 'Date': 'Wed, 23 Dec 2015 17:56:46 GMT'}
# ?.h...g.. 'Server'
# # 'nginx'