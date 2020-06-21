# # В простых методах запросов значительных отличий у них не имеется. Но давайте взглянем на работы с Basic Auth:
#
# ______ u__.r__
# password_mgr _ ?.r__.H_PMWDR..
# top_level_url _ 'https://httpbin.org/basic-auth/user/passwd'
# password_mgr.a_p.. N.. ? 'user', 'passwd'
# handler _ ?.r__.H_BAH.. ?
# opener _ ?.r__.b_o.. ?
# response _ ?.o..  t_..
# print(?.g_c..
# # 200
# print ?.r..
# # b'{\n  "authenticated": true, \n  "user": "user"\n}\n'
#
#
# ______ r__
# response _ ?.g.. 'https://httpbin.org/basic-auth/user/passwd' a.._('user', 'passwd'
# print ?.c..
# # b'{\n  "authenticated": true, \n  "user": "user"\n}\n'
# print ?.j..
# # {'user': 'user', 'authenticated': True}
#
# # А теперь чувствуется разница между pythonic и non-pythonic? Я думаю разница на лицо.
# # И несмотря на тот факт, что requests ничто иное как обёртка над urllib3,
# # а последняя является надстройкой над стандартными средствами Python,
# # удобство написания кода в большинстве случаев является приоритетом номер один.
# #
# # В requests имеется:
# #
# #     Множество методов http аутентификации
# #     Сессии с куками
# #     Полноценная поддержка SSL
# #     Различные методы-плюшки вроде .json(), которые вернут данные в нужном формате
# #     Проксирование
# #     Грамотная и логичная работа с исключениями
