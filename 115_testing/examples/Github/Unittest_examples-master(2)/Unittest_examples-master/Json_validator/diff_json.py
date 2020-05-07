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
import json
import os

TYPE = 'TYPE'
PATH = 'PATH'
VALUE = 'VALUE'
ETHALON_JSON = os.path.abspath('json_ethalon.json')
TEST_JSON = os.path.abspath('json_test.json')


class JsonDiffHandler(object):
    """
        Данный класс включает в себя следующие методы:
            1)  def check(self, first_json, second_json, path='', with_values=False) -
                данный метод производит сравнение этальнного и тестового json-файлов;
            2) save_difference(self, diff_message, type_) - данный метод производит сохрание
                результата сравнения
    """
    def __init__(self, first_json, second_json, with_values=False):
        self.difference = []
        self.seen = []
        self.check(first_json, second_json, with_values=with_values)

    def check(self, first_json, second_json, path='', with_values=False):
        """Метод, сравнивающий секции этальнного и тестового json-файлов"""
        # Определение типа нового значения
        if with_values and second_json is not None:
            if not isinstance(first_json, type(second_json)):
                message = '%s --> OLD TYPE: %s ==> NEW TYPE: %s' % \
                          (path, type(first_json).__name__, type(second_json).__name__)
                self.save_difference(message, TYPE)

        # Если проверяемая секция эталонного json словарь
        if isinstance(first_json, dict):
            for key in first_json:
                # Формирование вложенности секции через точку
                if len(path) == 0:
                    new_path = key
                else:
                    new_path = "%s.%s" % (path, key)
                # Если проверяемая секция тестового json словарь
                if isinstance(second_json, dict):
                    if key in second_json:
                        sec = second_json[key]
                    else:
                        #  В тестовом json отсутствует секция
                        self.save_difference(new_path, PATH)
                        sec = None
                    # Рекурсивный вызов
                    if sec is not None:
                        self.check(first_json[key], sec, path=new_path, with_values=with_values)
                else:
                    # Если проверяемая секция тестового json НЕ словарь,
                    # то вся секция эталонного json записывается в результат
                    self.save_difference(new_path, PATH)
                    self.check(first_json[key], second_json, path=new_path, with_values=with_values)

        # Если проверяемая секция эталонного json список
        elif isinstance(first_json, list):
            for (index, item) in enumerate(first_json):
                new_path = "%s[%s]" % (path, index)
                sec = None
                if second_json is not None:
                    try:
                        sec = second_json[index]
                    except (IndexError, KeyError):
                        # Если ОШИБКА, значит секция-список эталонного json,
                        # отличается от секции-список тестового json, записываем в результат
                        self.save_difference('%s - %s' % (new_path, type(item).__name__), TYPE)

                # Рекурсивный вызов
                self.check(first_json[index], sec, path=new_path, with_values=with_values)
        # Если разница между тестируемым и эталонным json только в значениях определенных секции
        else:
            if with_values and second_json is not None:
                if first_json != second_json:
                    self.save_difference('%s --> OLD VALUE: %s ==> NEW VALUE: %s ' %
                                         (path, first_json, second_json), VALUE)
            return

    def save_difference(self, diff_message, type_):
        """Метод, сохраняющий результ сравнения (ТИП сообщения, СОДЕРЖИМОЕ сообщения)"""
        if diff_message not in self.difference:
            self.seen.append(diff_message)
            self.difference.append((type_, diff_message))


def assert_json(test_json, ethalon_json):
    """ Функция проверки на разность этальнного и тестового json-файлов"""
    test_json = json.loads(test_json)
    ethalon_json = json.loads(ethalon_json)
    diff1 = JsonDiffHandler(test_json, ethalon_json, True).difference
    diff2 = JsonDiffHandler(ethalon_json, test_json, False).difference
    diffs = []
    # Обработка типов сообщений и их содержимого, формирование результата
    for type, message in diff1:
        newType = 'CHANGED_VALUE'
        if type == PATH:
            newType = 'REMOVED_SECTION'
        diffs.append({'type': newType, 'message': message})
    for type, message in diff2:
        diffs.append({'type': 'ADDED_SECTION', 'message': message})
    return diffs


if __name__ == '__main__':
    with open(ETHALON_JSON) as ethalon_json, \
            open(TEST_JSON) as test_json:
        diff_res = assert_json(ethalon_json.read(), test_json.read())
        if len(diff_res) > 0:
            print '\r\nFound differences between two ' \
                  'files:\r\n{0},\r\n{1}\r\n'.format(TEST_JSON, ETHALON_JSON)
            print "+++" * 30
        for diff in diff_res:
            print diff['type'] + ': ' + diff['message']
