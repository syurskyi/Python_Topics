# -*- coding: utf-8 -*-
____ pp.. ______ pp..
______ _3


data _ [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]


___ create_connection(db_name):
    '''
    Функция создает соединение с БД db_name
    и возвращает его
    '''
    connection _ _3.connect(db_name)
    return connection


___ write_data_to_db(connection, query, data):
    '''
    Функция ожидает аргументы:
     * connection - соединение с БД
     * query - запрос, который нужно выполнить
     * data - данные, которые надо передать в виде списка кортежей

    Функция пытается записать все данные из списка data.
    Если данные удалось записать успешно, изменения сохраняются в БД
    и функция возвращает True.
    Если в процессе записи возникла ошибка, транзакция откатывается
    и функция возвращает False.
    '''
    try:
        with connection:
            connection.executemany(query, data)
    except _3.IntegrityError as e:
        print('Error occured: ', e)
        return False
    else:
        print('Запись данных прошла успешно')
        return True


___ get_all_from_db(connection, query):
    '''
    Функция ожидает аргументы:
     * connection - соединение с БД
     * query - запрос, который нужно выполнить

    Функция возвращает данные полученные из БД.
    '''
    result _ [row for row in connection.execute(query)]
    return result


if __name__ == '__main__':
    con _ create_connection('sw_inventory3.db')

    print('Создание таблицы...')
    schema _ '''create table switch
                (mac text primary key, hostname text, model text, location text)'''
    con.execute(schema)

    query_insert _ 'INSERT into switch values (?, ?, ?, ?)'
    query_get_all _ 'SELECT * from switch'

    print('Запись данных в БД:')
    pprint(data)
    write_data_to_db(con, query_insert, data)
    print('\nПроверка содержимого БД')
    pprint(get_all_from_db(con, query_get_all))

    con.close()
