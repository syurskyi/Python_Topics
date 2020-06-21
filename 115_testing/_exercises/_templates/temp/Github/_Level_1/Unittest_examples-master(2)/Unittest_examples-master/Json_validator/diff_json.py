#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Данный скрипт производит сравнение этальнного и тестового json-файлов.
    Сравнение происходит по следующим показателям:
    1) Добавление секции в тестовом json-файле - 'ADDED_SECTION';
    2) Удаление секции в тестовом json-файле - 'REMOVED_SECTION';
    3) Проверка отличия значений каждой секции в тестовом json-файле
       от эталонного json-файла - 'CHANGED_VALUE'
       ПРИМЕР: OLD VALUE: <example1> ==> NEW VALUE: <example1>;
    4) В случае, если в секциях есть разные значения, производится
       определение нового типа значения
       ПРИМЕР: OLD TYPE: <example2> ==> NEW TYPE: <example2>;

    P.S: Для корректного функционирования программы этальнный и
         тестовый json-файлы должны располагаться в одном и том же
         катологе.
"""
______ j__
______ __

TYPE _ 'TYPE'
PATH _ 'PATH'
VALUE _ 'VALUE'
ETHALON_JSON _ __.pa__.abspath('json_ethalon.json')
TEST_JSON _ __.pa__.abspath('json_test.json')


c_ JsonDiffHandler o..
    """
        Данный класс включает в себя следующие методы:
            1)  def check(self, first_json, second_json, path='', with_values=False) -
                данный метод производит сравнение этальнного и тестового json-файлов;
            2) save_difference(self, diff_message, type_) - данный метод производит сохрание
                результата сравнения
    """
    ___  -   first_json, second_json, with_values_False
        difference _ # list
        seen _ # list
        check(first_json, second_json, with_values_with_values)

    ___ check  first_json, second_json, path_'', with_values_False
        """Метод, сравнивающий секции этальнного и тестового json-файлов"""
        # Определение типа нового значения
        __ with_values an. second_json __ no. N..:
            __ no. isi..(first_json, ty..(second_json)):
                message _ '%s --> OLD TYPE: %s ==> NEW TYPE: %s' % \
                          (pa__, ty..(first_json).__name__, ty..(second_json).__name__)
                save_difference(message, TYPE)

        # Если проверяемая секция эталонного json словарь
        __ isi..(first_json, dict
            ___ key __ first_json:
                # Формирование вложенности секции через точку
                __ le.(pa__) __ 0:
                    new_path _ key
                ____:
                    new_path _ "%s.%s" % (pa__, key)
                # Если проверяемая секция тестового json словарь
                __ isi..(second_json, dict
                    __ key __ second_json:
                        sec _ second_json[key]
                    ____:
                        #  В тестовом json отсутствует секция
                        save_difference(new_path, PATH)
                        sec _ N..
                    # Рекурсивный вызов
                    __ sec __ no. N..:
                        check(first_json[key], sec, path_new_path, with_values_with_values)
                ____:
                    # Если проверяемая секция тестового json НЕ словарь,
                    # то вся секция эталонного json записывается в результат
                    save_difference(new_path, PATH)
                    check(first_json[key], second_json, path_new_path, with_values_with_values)

        # Если проверяемая секция эталонного json список
        elif isi..(first_json, li..
            ___ (index, item) __ enumerate(first_json
                new_path _ "%s[%s]" % (pa__, index)
                sec _ N..
                __ second_json __ no. N..:
                    ___
                        sec _ second_json[index]
                    _____ (IndexError, K..
                        # Если ОШИБКА, значит секция-список эталонного json,
                        # отличается от секции-список тестового json, записываем в результат
                        save_difference('%s - %s' % (new_path, ty..(item).__name__), TYPE)

                # Рекурсивный вызов
                check(first_json[index], sec, path_new_path, with_values_with_values)
        # Если разница между тестируемым и эталонным json только в значениях определенных секции
        ____:
            __ with_values an. second_json __ no. N..:
                __ first_json !_ second_json:
                    save_difference('%s --> OLD VALUE: %s ==> NEW VALUE: %s ' %
                                         (pa__, first_json, second_json), VALUE)
            r_

    ___ save_difference  diff_message, type_
        """Метод, сохраняющий результ сравнения (ТИП сообщения, СОДЕРЖИМОЕ сообщения)"""
        __ diff_message no. __ difference:
            seen.a..(diff_message)
            difference.a..((type_, diff_message))


___ assert_json(test_json, ethalon_json
    """ Функция проверки на разность этальнного и тестового json-файлов"""
    test_json _ j__.loads(test_json)
    ethalon_json _ j__.loads(ethalon_json)
    diff1 _ JsonDiffHandler(test_json, ethalon_json, T..).difference
    diff2 _ JsonDiffHandler(ethalon_json, test_json, F..).difference
    diffs _ # list
    # Обработка типов сообщений и их содержимого, формирование результата
    ___ ty.., message __ diff1:
        newType _ 'CHANGED_VALUE'
        __ ty.. __ PATH:
            newType _ 'REMOVED_SECTION'
        diffs.a..({'type': newType, 'message': message})
    ___ ty.., message __ diff2:
        diffs.a..({'type': 'ADDED_SECTION', 'message': message})
    r_ diffs


__ _____ __ _____
    w__ o..(ETHALON_JSON) __ ethalon_json, \
            o..(TEST_JSON) __ test_json:
        diff_res _ assert_json(ethalon_json.read(), test_json.read())
        __ le.(diff_res) > 0:
            print '\r\nFound differences between two ' \
                  'files:\r\n{0},\r\n{1}\r\n'.f..(TEST_JSON, ETHALON_JSON)
            print "+++" * 30
        ___ diff __ diff_res:
            print diff['type'] + ': ' + diff['message']
