# # -*- coding: utf-8 -*-
# ____ pp.. ______ pp..
# ______ _3
#
#
# data _ [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
#         ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
#         ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
#         ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]
#
#
# ___ create_connection db_name
#     '''
#     Функция создает соединение с БД db_name
#     и возвращает его
#     '''
#     connection _ _3.c.. db_name
#     r_ ?
#
#
# ___ write_data_to_db connection query data
#     '''
#     Функция ожидает аргументы:
#      * connection - соединение с БД
#      * query - запрос, который нужно выполнить
#      * data - данные, которые надо передать в виде списка кортежей
#
#     Функция пытается записать все данные из списка data.
#     Если данные удалось записать успешно, изменения сохраняются в БД
#     и функция возвращает True.
#     Если в процессе записи возникла ошибка, транзакция откатывается
#     и функция возвращает False.
#     '''
#     ___
#         w___ c..
#             ?.e_m.. q.. d..
#     ______ _3.I.. __ e
#         print('Error occured: ' ?
#         r_ F..
#     _____
#         print('Запись данных прошла успешно')
#         r_ T..
#
#
# ___ get_all_from_db connection query
#     '''
#     Функция ожидает аргументы:
#      * connection - соединение с БД
#      * query - запрос, который нужно выполнить
#
#     Функция возвращает данные полученные из БД.
#     '''
#     result _ row ___ ? __ c___.e.. q..
#     r_ ?
#
#
# __ _____ __ ______
#     con _ c_c.. *sw_inventory3.db
#
#     print('Создание таблицы...')
#     schema _ c.. t.. sw...
#                 (mac t.. p.. k.., hostname t.., model t.., location t..
#     ?.e.. ?
#
#     query_insert _ I.. i.. sw.. v..  @ @ @ @
#     query_get_all _ S.. _ f.. sw..
#
#     print('Запись данных в БД:')
#     pprint d..
#     w_d_t_d. c.. q_i.. d..
#     print('\nПроверка содержимого БД')
#     pprint(g... c.. q_g_a..
#
#     ?.c..
