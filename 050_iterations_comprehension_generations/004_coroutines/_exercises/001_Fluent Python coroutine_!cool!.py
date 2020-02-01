# # -*- coding: utf-8 -*-
# # #
# # Fluent Python: coroutine
# # Сопрограммы (coroutine) на основе генератора.
# # Следующий раздел Fluent Python - сопрограммы.
# #  В книге Fluent Python используется Python 3.4. В версиях 3.5 и 3.6 были внесены изменения связанные с сопрограммами.
# # В этой заметке вся информация основывается на разделе coroutines в книге Fluent Python.
# # Сопрограмма
# # Сопрограмма - часть программы, которая взаимодействует с вызывающем ее кодом, генерируя и получая данные.
# #     Более полное определение в википедии
# # С точкизрения синтаксиса, сопрограмма выглядит как генератор. Однако, в сопрограмме, yield как правило находится
# # с правой стороны выражения: command = yield.
# # При этом генерация значения опциональна:
# #
# #     Если после yield находится выражение, генератор отдает его
# #     иначе, отдается значение None
# #
# # Сопрограмма может не только генерировать данные, но и принимать их. Для этого используется метод send.
# # Базовый пример сопрограммы. Передача данных сопрограмме
# #
# # Пример сопрограммы:
#
# ___ basic_coroutine1 start
#     print('Start value:', ?)
#     first _ ?
#     print('First received:', ?)
#     second _ ?
#     print('Second received:', ?)
#
# # Вызываем функцию, чтобы получить генератор:
#
# bc1 _ ? 100
# print(bc1)
# # Out[3]: <generator object basic_coroutine1 at 0xb598abfc>
#
# # Теперь, чтобы получить возможность отправлять данные сопрограмме, надо ее инициировать. Это делается вызовом next:
#
# n.. ?
# # Start value: 100
#
# # Сопрограмма выполнила весь код до первого yield и остановилась. Теперь у нас есть возможность отправить данные, используя метод send:
#
# ?.se.. 200
# # First received: 200
#
# # Сопрограмма получила данные, присвоила их в переменную first, вывела сообщение “First received: 200” и остановилась
# # на следующем yield.
# # Теперь можно снова отправить данные:
#
# ?.se.. 300
# # Second received: 300
# # ---------------------------------------------------------------------------
# # StopIteration                             Traceback (most recent call last)
# # <ipython-input-5-62309180db70> in <module>()
# # ----> 1 bc1.send(300)
#
# # StopIteration:
#
# # Тут аналогично: сопрограмма получила данные, присвоила их в переменную second, вывела сообщение “Second received: 300”.
# # Но, так как на этом функция-генератор закончилась, возвращается исключение StopIteration.
# #
# # Вернемся к загадочной строке next(bc1). Эта инициация необходима, чтобы отправлять данные сопрограмме.
# # Если снова вызвать функцию и сразу попытаться отправить данные, возникнет исключение:
#
# bc1 = ? 100
# ?.se.. 200
# # ------------------------------------------------------------
# # TypeError                  Traceback (most recent call last)
# # <ipython-input-9-11b40b565caa> in <module>()
# # ----> 1 bc1.send(200)
# #
# # TypeError: can't send non-None value to a just-started generator
#
# # По описанию исключения понятно, что инициировать сопрограмму можно и по-другому, отправив send(None):
#
# bc1 = ? 100
# ?.se.. N..
# # Start value: 100
#
# # Базовый пример сопрограммы. Оператор return
# # В сопрограмме можно использовать оператор return для завершения работы генератора и возврата данных.
# # Например:
#
# ___ basic_coroutine2
#     collection _
#     w___ T..
#         item _ ?
#         __ ? __ N...
#             r_ c..
#         c_.ap. ?
#
#
# # Инициация генератора и отправка данных выполняется аналогично:
#
# bc2 = ?
# ne.. ?
# ?.se.. 100
# ?.se.. 200
#
# # При отправке None, сопрограмма завершает работу. В этом случае, по-прежнему генерируется исключение StopIteration,
# # но, кроме этого, данные возвращаются как атрибут исключения:
#
# ?.se.. N..
# # ------------------------------------------------------------
# # StopIteration              Traceback (most recent call last)
# # <ipython-input-55-ef77f9d8836c> in <module>()
# # ----> 1 bc2.send(None)
#
# # StopIteration: [100, 200]
#
# # Для получения данных в переменную, надо получить значение атрибута value:
#
# bc2 = ?
# next(?)
# ?.se.. 100
# ?.se.. 200
# ?.se.. 300
# t__
#     ?.se.. N..
# ___ S___ __ e
#     result _ ?.va..
#
# result
# # [100, 200, 300]
#
# # Базовый пример сопрограммы. Получение данных с yield
# # В этом примере yield не просто приостанавливает выполнение сопрограммы, а еще и возвращает данные:
#
# ___ basic_coroutine3 items
#     collection _ i ___ ? __ ?
#     w__ T..
#         item _ y.. ?
#         ?.ap. i..
#
# # Еще одно небольшое изменение - сопрограмма создана с параметром items. Это значит, что ей можно передавать аргументы:
#
# bc3 = ? ([1,2,3])
# n.. ?
# # Out[71]: [1, 2, 3]
#
# # После инициации сопрограммы, ей можно передавать данные. Теперь после каждой передачи данных, возвращается содержимое
# # списка collection:
#
# ?.se.. 100
# # Out[72]: [1, 2, 3, 100]
#
# ?.se.. 200
# # Out[73]: [1, 2, 3, 100, 200]
#
# # Раз содержимое возвращается, его можно присвоить в переменную:
#
# result = ?.se.. 300
# result
# # Out[75]: [1, 2, 3, 100, 200, 300]
#
# # В этой сопрограмме нет условия для завершения цикла while. Это значит, что она будет принимать данные и возвращать
# # результат до тех пор, пока сопрограмма используется. Но у сопрограммы есть метод close, который позволяет в любой момент
# # завершить ее:
# bc3.cl..
#
# # Теперь, при обращении к сопрограмме, будет возвращаться исключение StopIteration:
#
# ?.se..(400)
# # ------------------------------------------------------------
# # StopIteration              Traceback (most recent call last)
# # <ipython-input-77-1d704bd03fe8> in <module>()
# # ----> 1 bc3.send(400)
# #
# # StopIteration:
#
# # Хоть я уже и не сетевой инженер, а никуда не денешься от того, что при изучении новых тем, в голове рождаются примеры
# # использования для сетей :)
# # Пример использования сопрограммы с netmiko
# # С помощью сопрограммы можно создать соединение SSH с устройством, которое ожидает команды. А, после получения команды,
# # возвращает результат.
# #
# # Первый вариант сопрограммы:
#
# # ___ send_show_command device_params
# #     print('Opening connection to IP: {}'.format(device_params['ip']))
# #     conn = netmiko.ConnectHandler(**device_params)
# #     conn.enable()
# #     result = None
# #     while True:
# #         command = yield result
# #         result = conn.send_command(command)
# #
# # # Для подключения по SSH с помощью netmiko, надо создать словарь с параметрами подключения:
# #
# # import netmiko
# #
# # r1 = {'device_type': 'cisco_ios',
# #       'ip': '192.168.100.1',
# #       'username': 'cisco',
# #       'password': 'cisco',
# #       'secret': 'cisco' }
# #
# # # Теперь можно вызывать сопрограмму и инициировать ее:
# #
# # ssh = send_show_command(r1)
# # next(ssh)
# # # Opening connection to IP: 192.168.100.1
# #
# # # При инициации сопрограммы, выполняется весь код до yield - выводится сообщение, выполняется подключение к устройству и
# # # netmiko переходит в режим enable. После этого, управление останавливается на yield.
# # # Теперь, если передать сопрограмме команду, она запишет ее в переменную command, выполнит ее с помощью метода
# # # send_command и, так как цикл пошел на следующую итерацию, вернет результат выполнения команды и остановится:
# #
# # ssh.send('sh ip arp')
# # # Out[7]: 'Protocol  Address          Age (min)  Hardware Addr   Type   Interface\nInternet  19.1.1.1                -   aabb.cc00.6520  ARPA   Ethernet0/2\nInternet  192.168.100.1           -   aabb.cc00.6500  ARPA   Ethernet0/0\nInternet  192.168.100.100        37   aabb.cc80.c900  ARPA   Ethernet0/0\nInternet  192.168.200.1           -   0203.e800.6510  ARPA   Ethernet0/1\nInternet  192.168.200.100        28   0800.27ac.1b91  ARPA   Ethernet0/1\nInternet  192.168.230.1           -   aabb.cc00.6530  ARPA   Ethernet0/3'
# #
# # # Отправка еще одной команды, но только теперь результат сохраняется в переменную:
# #
# # result = ssh.send('sh ip int br')
# # print(result)
# # # Interface                  IP-Address      OK? Method Status                Protocol
# # # Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
# # # Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
# # # Ethernet0/2                19.1.1.1        YES NVRAM  up                    up
# # # Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
# #
# # # Если сопрограмма больше не нужна, можно остановить ее, с помощью метода close:
# #
# # ssh.close()
# #
# # # Но, в данном случае, после завершения работы сопрограммы, сессия SSH остается открытой на оборудовании. Более корректно
# # # было бы завершать сессию, когда сопрограмма завершает работу.
# # # Это достаточно легко сделать, так как вызов метода close, генерирует внутри сопрограммы исключение GeneratorExit.
# # # А значит, можно перехватить его и закрыть сессию.
# # # Финальный пример сопрограммы send_show_command с закрытием сессии (файл netmiko_coroutine.py):
# #
# # import netmiko
# #
# # ___ send_show_command(device_params):
# #     print('Open connection to: '.rjust(40, '#'),
# #           device_params['ip'])
# #     conn = netmiko.ConnectHandler(**device_params)
# #     conn.enable()
# #     result = None
# #     while True:
# #         try:
# #             command = yield result
# #             result = conn.send_command(command)
# #         except GeneratorExit:
# #             conn.disconnect()
# #             print('Connection closed'.rjust(40, '#'))
# #             break
# #
# #
# # r1 = {'device_type': 'cisco_ios',
# #       'ip': '192.168.100.1',
# #       'username': 'cisco',
# #       'password': 'cisco',
# #       'secret': 'cisco' }
# #
# # commands = ['sh ip int br', 'sh ip arp']
# #
# # ssh = send_show_command(r1)
# # next(ssh)
# #
# # for c in commands:
# #     result = ssh.send(c)
# #     print(result)
# #
# # ssh.close()
#
# # Результат выполнения:
# #
# # $ python netmiko_coroutine.py
# # ####################Open connection to:  192.168.100.1
# # Interface                  IP-Address      OK? Method Status                Protocol
# # Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
# # Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
# # Ethernet0/2                19.1.1.1        YES NVRAM  up                    up
# # Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
# # Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# # Internet  19.1.1.1                -   aabb.cc00.6520  ARPA   Ethernet0/2
# # Internet  192.168.100.1           -   aabb.cc00.6500  ARPA   Ethernet0/0
# # Internet  192.168.100.100        54   aabb.cc80.c900  ARPA   Ethernet0/0
# # Internet  192.168.200.1           -   0203.e800.6510  ARPA   Ethernet0/1
# # Internet  192.168.200.100         2   0800.27ac.1b91  ARPA   Ethernet0/1
# # Internet  192.168.230.1           -   aabb.cc00.6530  ARPA   Ethernet0/3
# #######################Connection closed
#
# # yield from
# # Выражение yield from может использоваться, как и yield, в генераторе и в сопрограммах.
# # yield from в генераторе
# # При использовании в генераторе, yield from может помочь упростить использование yield в цикле for:
#
# ___ generate
#     ___ i __ ra.. 5
#         y... i
#
# li.. ?
# # Out[2]: [0, 1, 2, 3, 4]
#
# # Аналогичный вариант с yield from:
#
# ___ generate
#     y... f.. range 5
#
# li.. ?
# # Out[4]: [0, 1, 2, 3, 4]
#
# # Пример использования yield from для получения плоского списка из списка списков с разной вложенностью
# # (упрощенный вариант примера 4.14 из книги Python Cookbook:
#
# ___ flatten_list alist
#     ___ item __ ?
#         __ ty.. ? __ list
#             y... f.. ? i..
#         ___
#             y... i..
#
# example = [0, 1, [2, 3], 4, [5, 6, [7, 8]], 9]
#
# li.. ? ?
# # Out[7]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # yield from в сопрограммах
# # Основная функциональность yield from - открытие двухстороннего канала между кодом, который вызвает сопрограмму и
# # вложенным генератором, при этом значения передаются между ними напрямую.
# # Пример использования yield from:
#
# from pprint import pprint
#
# #subgenerator
# ___ power
#     print('Start subgenerator')
#     result =    # dict
#     w_ T..
#         num = y...
#         __ ? i_ N..
#             print('Finish subgenerator')
#             b___
#         print ?
#         res__|? = ?**2
#     r_ ?
#
#
# #delegating generator
# ___ del_gen results set_id
#     w___ T..
#         print('*'*40)
#         print('Start delegating generator')
#         r__ s___ _ y... f.. po..
#         print r____.ke..
#         print('Finish delegating generator')
#         print('*'*40)
#
#
# #caller
# ___ mainnum_sets
#     results _  # dict
#     ___ set_id num_set __ n___.it..
#         collect _ del_gen r____ s..
#         ne.. ?
#         ___ num __ n._s.
#             c__.se.. n..
#         c__.se.. N..
#     r_ r____
#
# all_numbers = {'set1': [1, 2, 3, 4, 5],
#                'set2': [10, 20, 30, 40, 50]}
#
# result = main ?
# pprint(result)
#
# # Функция main перебирает наборы чисел и для каждого набора вызывает сопрограмму del_gen и инициирует генератор:
#
# ___ set_id, num_set __ n__.it..
#     collect _ del_gen r... s..
#     ne.. ?
#
# # После этого, генератор останавливается на yield и вызывается вложенный генератор power. Теперь send из функции main
# # попадает напрямую во вложенный генератор power, а yield из вложенного генератора power, попадает в функцию main.
# #  Но, так как во вложеном генераторе после yield нет никакого значения, возвращается None.
# # После перебора всех чисел в наборе, функция main отправляет значение None, чтобы завершить работу вложенного генератора.
# # Как только вложенный генератор завершил своб работу, результат, который он возвращает записывается в сопрограмме del_gen в словарь results:
# #         results[set_id] = yield from power()
# # Аналогично все повторяется для следующего набора чисел.
# #
# # Результат выполнения:
#
# # $ python basic_subgenerator.py
# # ****************************************
# # Start delegating generator
# # Start subgenerator
# # 1
# # 2
# # 3
# # 4
# # 5
# # Finish subgenerator
# # dict_keys(['set1'])
# # Finish delegating generator
# # ****************************************
# # ****************************************
# # Start delegating generator
# # Start subgenerator
# # ****************************************
# # Start delegating generator
# # Start subgenerator
# # 10
# # 20
# # 30
# # 40
# # 50
# # Finish subgenerator
# # dict_keys(['set1', 'set2'])
# # Finish delegating generator
# # ****************************************
# # ****************************************
# # Start delegating generator
# # Start subgenerator
#
# # {'set1': {1: 1, 2: 4, 3: 9, 4: 16, 5: 25},
# #  'set2': {10: 100, 20: 400, 30: 900, 40: 1600, 50: 2500}}
#
# # Я пока не до конца разобралась с этими промежуточными повторными вызовами, которые появляются после нормального вызова
# # Пример использования yield from
# # Пример в целом аналогичен прошлому, но немного изменен код во вложенном генераторе send_show_command,
# # чтобы соединение устанавливалось только, когда это действительно нужно (чтобы не было было подключения
# # из-за промежуточных вызовов):
#
# # import netmiko
# # from pprint import pprint
# #
# # #subgenerator
# # ___ send_show_command3(device_params):
# #     command = y...
# #     print('Opening connection to IP: {}'.format(device_params['ip']))
# #     conn = netmiko.ConnectHandler(**device_params)
# #     conn.enable()
# #     command_result = {}
# #     while True:
# #         if command is None:
# #             conn.disconnect()
# #             print('Connection closed')
# #             break
# #         print(command)
# #         output = conn.send_command(command)
# #         command_result[command] = output
# #         command = y...
# #     return command_result
# #
# #
# # #delegating generator
# # ___ collect_output(results, device_params):
# #     while True:
# #         print('*'*40)
# #         results[device_params['ip']] = y... from send_show_command3(device_params)
# #
# #
# # #caller
# # ___ main(devices, commands):
# #     results = {}
# #     for device in devices:
# #         collect = collect_output(results, device)
# #         next(collect)
# #         for command in commands:
# #             collect.send(command)
# #         collect.send(None)
# #     return results
# #
# #
# # r1 = {'device_type': 'cisco_ios',
# #       'ip': '192.168.100.1',
# #       'username': 'cisco',
# #       'password': 'cisco',
# #       'secret': 'cisco' }
# # r2 = {'device_type': 'cisco_ios',
# #       'ip': '192.168.100.2',
# #       'username': 'cisco',
# #       'password': 'cisco',
# #       'secret': 'cisco' }
# #
# #
# # all_devices = [r1, r2]
# # commands = ['sh ip arp', 'sh ip int br']
# #
# # result = main(all_devices, commands)
# #
# # for device, command in result.items():
# #     print(' IP: {} '.format(device).center(50,'#'))
# #     for c, output in command.items():
# #         print(' Command: {} '.format(c).center(50,'#'))
# #         print(output)
#
# # Результат выполнения:
# #
# # $ python netmiko_subgenerator.py
# # ****************************************
# # Opening connection to IP: 192.168.100.1
# # sh ip arp
# # sh ip int br
# # Connection closed
# # ****************************************
# # ****************************************
# # Opening connection to IP: 192.168.100.2
# # sh ip arp
# # sh ip int br
# # Connection closed
# # ****************************************
# # ############### IP: 192.168.100.1 ################
# # ############### Command: sh ip arp ###############
# # Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# # Internet  19.1.1.1                -   aabb.cc00.6520  ARPA   Ethernet0/2
# # Internet  192.168.100.1           -   aabb.cc00.6500  ARPA   Ethernet0/0
# # Internet  192.168.100.2          71   aabb.cc00.6600  ARPA   Ethernet0/0
# # Internet  192.168.100.100        72   aabb.cc80.c900  ARPA   Ethernet0/0
# # Internet  192.168.200.1           -   0203.e800.6510  ARPA   Ethernet0/1
# # Internet  192.168.200.100        71   0800.27ac.1b91  ARPA   Ethernet0/1
# # Internet  192.168.230.1           -   aabb.cc00.6530  ARPA   Ethernet0/3
# # ############# Command: sh ip int br ##############
# # Interface                  IP-Address      OK? Method Status                Protocol
# # Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
# # Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
# # Ethernet0/2                19.1.1.1        YES NVRAM  up                    up
# # Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
# # ############### IP: 192.168.100.2 ################
# # ############### Command: sh ip arp ###############
# # Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# # Internet  192.168.100.1          72   aabb.cc00.6500  ARPA   Ethernet0/0
# # Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
# # Internet  192.168.100.100        72   aabb.cc80.c900  ARPA   Ethernet0/0
# # ############# Command: sh ip int br ##############
# # Interface                  IP-Address      OK? Method Status                Protocol
# # Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
# # Ethernet0/1                unassigned      YES NVRAM  administratively down down
# # Ethernet0/2                unassigned      YES NVRAM  administratively down down
# # Ethernet0/3                unassigned      YES NVRAM  administratively down down
