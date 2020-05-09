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
______ json
______ os

TYPE _ 'TYPE'
PATH _ 'PATH'
VALUE _ 'VALUE'
ETHALON_JSON _ os.path.abspath('json_ethalon.json')
TEST_JSON _ os.path.abspath('json_test.json')


c_ JsonDiffHandler(object
    """
        Данный класс включает в себя следующие методы:
            1)  def check(self, first_json, second_json, path='', with_values=False) -
                данный метод производит сравнение этальнного и тестового json-файлов;
            2) save_difference(self, diff_message, type_) - данный метод производит сохрание
                результата сравнения
    """
    ___  -   first_json, second_json, with_values_False
        difference _ []
        seen _ []
        check(first_json, second_json, with_values_with_values)

    ___ check  first_json, second_json, path_'', with_values_False
        """Метод, сравнивающий секции этальнного и тестового json-файлов"""
        # Определение типа нового значения
        if with_values and second_json is not None:
            if not isinstance(first_json, type(second_json)):
                message _ '%s --> OLD TYPE: %s ==> NEW TYPE: %s' % \
                          (path, type(first_json).__name__, type(second_json).__name__)
                save_difference(message, TYPE)

        # Если проверяемая секция эталонного json словарь
        if isinstance(first_json, dict
            for key in first_json:
                # Формирование вложенности секции через точку
                if len(path) == 0:
                    new_path _ key
                else:
                    new_path _ "%s.%s" % (path, key)
                # Если проверяемая секция тестового json словарь
                if isinstance(second_json, dict
                    if key in second_json:
                        sec _ second_json[key]
                    else:
                        #  В тестовом json отсутствует секция
                        save_difference(new_path, PATH)
                        sec _ None
                    # Рекурсивный вызов
                    if sec is not None:
                        check(first_json[key], sec, path_new_path, with_values_with_values)
                else:
                    # Если проверяемая секция тестового json НЕ словарь,
                    # то вся секция эталонного json записывается в результат
                    save_difference(new_path, PATH)
                    check(first_json[key], second_json, path_new_path, with_values_with_values)

        # Если проверяемая секция эталонного json список
        elif isinstance(first_json, list
            for (index, item) in enumerate(first_json
                new_path _ "%s[%s]" % (path, index)
                sec _ None
                if second_json is not None:
                    try:
                        sec _ second_json[index]
                    except (IndexError, KeyError
                        # Если ОШИБКА, значит секция-список эталонного json,
                        # отличается от секции-список тестового json, записываем в результат
                        save_difference('%s - %s' % (new_path, type(item).__name__), TYPE)

                # Рекурсивный вызов
                check(first_json[index], sec, path_new_path, with_values_with_values)
        # Если разница между тестируемым и эталонным json только в значениях определенных секции
        else:
            if with_values and second_json is not None:
                if first_json !_ second_json:
                    save_difference('%s --> OLD VALUE: %s ==> NEW VALUE: %s ' %
                                         (path, first_json, second_json), VALUE)
            r_

    ___ save_difference  diff_message, type_
        """Метод, сохраняющий результ сравнения (ТИП сообщения, СОДЕРЖИМОЕ сообщения)"""
        if diff_message not in difference:
            seen.append(diff_message)
            difference.append((type_, diff_message))


___ assert_json(test_json, ethalon_json
    """ Функция проверки на разность этальнного и тестового json-файлов"""
    test_json _ json.loads(test_json)
    ethalon_json _ json.loads(ethalon_json)
    diff1 _ JsonDiffHandler(test_json, ethalon_json, True).difference
    diff2 _ JsonDiffHandler(ethalon_json, test_json, False).difference
    diffs _ []
    # Обработка типов сообщений и их содержимого, формирование результата
    for type, message in diff1:
        newType _ 'CHANGED_VALUE'
        if type == PATH:
            newType _ 'REMOVED_SECTION'
        diffs.append({'type': newType, 'message': message})
    for type, message in diff2:
        diffs.append({'type': 'ADDED_SECTION', 'message': message})
    r_ diffs


if __name__ == '__main__':
    with open(ETHALON_JSON) as ethalon_json, \
            open(TEST_JSON) as test_json:
        diff_res _ assert_json(ethalon_json.read(), test_json.read())
        if len(diff_res) > 0:
            print '\r\nFound differences between two ' \
                  'files:\r\n{0},\r\n{1}\r\n'.f..(TEST_JSON, ETHALON_JSON)
            print "+++" * 30
        for diff in diff_res:
            print diff['type'] + ': ' + diff['message']
