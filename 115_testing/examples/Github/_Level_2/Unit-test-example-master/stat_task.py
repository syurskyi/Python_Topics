#!/usr/bin/env python3
#-*-coding: utf-8-*-

import argparse
from math import ceil, floor


class Parser():
    """
    Производит подготовку данных для дальнейшей обработки статистическими
    функциями
    """

    def data_extr(self, fileobj, index):
        """
        Извлекает данные, производит проверку на количество полезных строк.
        :param fileobj: файловый объект
        :param index: номер столбца (отсчет с 0), в котором должны быть
        "непустые" объекты; по нему отфильтровывается мусор
        мусор
        :return: список со списками данных по каждой строке
        """

        SOURCE = []
        qty = 0
        allines = 0

        for line in fileobj:
            allines += 1
            try:
                L = list(line.split('\t'))
                L[index] == True
            except IndexError:
                pass
            else:
                L[-1] = L[-1].rstrip()
                SOURCE.append(L)
                qty += 1

        print('Извлечено ' + str(qty) + ' строк из ' + str(allines))
        return SOURCE

    def check_pos(self, source, *heads):
        """
        Производит поиск индексов в source[0] для имен heads.
        :param source: список/кортеж со вложенными списками/кортежами
        :param heads: str - имена заголовков столбцов
        :return: [int, int...] - список с позиционными номерами данных
        в списках/кортежах, соответствующих заголовкам столбцов
        """
        number = []

        for head in heads:
            if head in source[0]:
                number.append(source[0].index(head))

        return number

    def int_converter(self, listobj, *index):
        """
        Для каждого из списков с данными преобразует list[index] в integer либо
        выдает исключение с информацией о позиции с неверным типом данных.
        :param listobj: список со вложенными списками данных
        :param index: integer - позиционный номер для списков с данными
        :return: None
        """
        linecount = 0
        for elem in listobj:
            linecount += 1
            for num in index:
                try:
                    elem[num] = int(elem[num])
                except (TypeError, ValueError):
                    print('Неверный формат в ' + str(num+1) + ' столбце, в ' +\
                          str(linecount) + ' строке данных.')
                    raise

    def key_names(self, source, index):
        """

        :param source: список/кортеж со вложенными списками/кортежами данных
        :param index: integer - позиционный номер для списка/кортежа
        с именами ключей
        :return: list - список неповторяющихся значений для каждого объекта
        списка/кортежа под номером index
        """
        keyname = []

        for elem in source:
            if elem[index] in keyname:
                pass
            else:
                keyname.append(elem[index])

        return keyname

    def fin_prep(self, fileobj, index, *heads):
        """

        :param fileobj: файловый объект
        :param index: номер столбца (отсчет с 0), в котором должны быть
        "непустые" объекты
        :param heads: str - имена заголовков столбцов
        :return: {key: [(),()...]} - словарь, в котором ключи -
        неповторяющиеся bмена в первом объекте head, значения - списки
        с кортежами данных
        """

        SOURCE = self.data_extr(fileobj, index)
        head_list = [head for head in heads]
        data_pos = self.check_pos(SOURCE, *head_list)

        SOURCE = SOURCE[1:]
        self.int_converter(SOURCE, *data_pos[1:])
        keyname = self.key_names(SOURCE, data_pos[0])

        DATAS = {name: [] for name in keyname}

        for name in keyname:
            for num in data_pos[1:]:
                DATAS[name].append( \
                    tuple( \
                        sorted([x[num] for x in SOURCE if x[data_pos[0]] == name])))

        return DATAS


class Statistics:

    def __init__(self, data):
        """
        Сортирует итерируемый объект и преобразует в tuple
        :param data: list/tuple с данными
        """
        self.data = tuple(sorted(data))

    def minimal(self):
        """
        :return: минимальное значение из self.data
        """
        return self.data[0]

    def median(self):
        """
        Если число элементов четное, то вычисляется полусумма значений двух
        средних индексов и округляется вверх до ближайшего целого значения.
        Если число элементов нечетное, то возвращается значение среднего
        индекса.
        :return: статистические 50% (медиану) данных в self.data
        """

        lendata = len(self.data)

        if lendata % 2 == 0:
            return ceil((self.data[lendata//2 - 1] + self.data[lendata//2]) /2)
            #округление в большую сторону

        else:
            return (self.data[lendata//2])

    def percent90(self):
        """
        Если индекс, находящийся на границе 9/10 от data, представляет
        собой целое число, то функция возвращает значение объекта под этим
        индексом.
        Если индекс, находящийся на границе 9/10 от data, представляет
        собой дробное число, то функция возвращает сумму значения объекта
        под округленным вниз граничным индексом и округленного вверх до целого
        числа произведения разницы объектов под индексами,
        окружающими граничный, на остаток от разницы граничного индекса и
        граничного индекса, округленного внииз до целого числа.
        :return: статистические 90% данных в data
        """
        lendata = len(self.data)
        index_plus1 = floor(lendata * 0.9)
        index = index_plus1 - 1

        if lendata % 10 == 0:
            return self.data[index]

        else:
            return (self.data[index] + ceil( \
                (self.data[index_plus1] - self.data[index]) * \
                (lendata * 0.9 - index_plus1)))

    def percent99(self):
        """
        Если индекс, находящийся на границе 99/100 от data, представляет
        собой целое число, то функция возвращает значение объекта под этим
        индексом.
        Если индекс, находящийся на границе 99/100 от data, представляет
        собой дробное число, то функция возвращает сумму значения объекта
        под округленным вниз граничным индексом и округленного вверх до целого
        числа произведения разницы объектов под индексами,
        окружающими граничный, на остаток от разницы граничного индекса и
        граничного индекса, округленного внииз до целого числа.
        :return: статистические 99% данных в data
        """
        lendata = len(self.data)
        index_plus1 = floor(lendata * 0.99)
        index = index_plus1 - 1

        if lendata % 100 == 0:
            return self.data[index]

        else:
            return (self.data[index] + ceil( \
                (self.data[index_plus1] - self.data[index]) * \
                (lendata * 0.99 - index_plus1)))

    def percent999(self):
        """
        Если индекс, находящийся на границе 999/1000 от data, представляет
        собой целое число, то функция возвращает значение объекта под этим
        индексом.
        Если индекс, находящийся на границе 999/1000 от data, представляет
        собой дробное число, то функция возвращает сумму значения объекта
        под округленным вниз граничным индексом и округленного вверх до целого
        числа произведения разницы объектов под индексами,
        окружающими граничный, на остаток от разницы граничного индекса и
        граничного индекса, округленного внииз до целого числа.
        :return: статистические 99,9% данных в data
        """
        lendata = len(self.data)
        index_plus1 = floor(lendata * 0.999)
        index = index_plus1 - 1

        if lendata % 1000 == 0:
            return self.data[index]

        else:
            return (self.data[index] + ceil( \
                (self.data[index_plus1] - self.data[index]) *\
                (lendata * 0.999 - index_plus1)))

    def fractions(self, denom=5):
        """
        1.  Cоздает список объектов из data, округленных вверх до ближайшего
            целого значения, кратного denom.
        2.  Из результата (1) исключает повторы и формирует список ключей
            для словаря.
        3.  Для каждого ключа словаря добавляет целое число (int)в списке,
            равное количеству его вхождений в data.
        4.  Для каждого ключа списка добавляет строковое значение в список,
            равное процентному отношению числа, полученного в п.3, к общему
            количеству данных в data, с точностью до 2-го знака после запятой.
        5.  Для каждого ключа списка добавляет строкове значение в список,
            равное процентному отношению суммы чисел во всех ключах, числовое
            значение которых не больше данного, к общему количеству данных
            в data, с точностью до 2-го знака после запятой.
        :param denom: integer - число, при делении данных на которое остаток 0.
        :return: {int: [int, float, float]}
        """
        rdata = [(x - x% -denom) for x in self.data]
        lendata = len(rdata)
        fdict = {number: [0] for number in sorted(set(rdata))}

        for number in rdata:
                fdict[number][0] += 1

        for key in fdict:
            fdict[key].append(format(fdict[key][0] / lendata * 100, '.2f'))

        rkeys = list(reversed([x for x in fdict.keys()]))

        while rkeys:
            sum = 0
            for key in rkeys:
                sum += fdict[key][0]
            fdict[rkeys[0]].append(format(sum / lendata * 100, '.2f'))
            rkeys = rkeys[1:]

        return fdict


class StatsResult(Statistics):

    def __init__(self, datas):
        """
          :param datas: {key: [[],[]...]} или {key: [(),()...]}
        """
        self.datas = datas

    def run(self, *list_funcs):
        """
        Функция предназначена для автоматизации формирования результатов
        нескольких наборов данных различными методами класса.
        :param list_funcs: str - имена функций-методов класса
        :return: {key: [(),()...]}
        """

        D = {}

        for key in self.datas:
            D[key] = []
            for data in self.datas[key]:
                self.data = tuple(sorted(data)) # for not sorted Source_data
                D[key].append(tuple(x() for x in list_funcs))

        return D


if __name__ == '__main__':

    argparser = argparse.ArgumentParser()
    argparser.add_argument('-f', '--file')

    file_source = open(argparser.parse_args().file, 'r')
    datas = Parser().fin_prep(file_source, 4, 'EVENT', 'AVGTSMR')
    file_source.close()

    stat = StatsResult(datas)
    list_funcs = [stat.minimal, stat.median, stat.percent90, \
                      stat.percent99, stat.percent999, stat.fractions]
    stdata = stat.run(*list_funcs)

    with open('result_stat.txt','w') as file:
        for key in stdata.keys():
            print(key, 'min=' + str(stdata[key][0][0]),
                  '50%=' + str(stdata[key][0][1]),
                  '90%=' + str(stdata[key][0][2]),
                  '99%=' + str(stdata[key][0][3]),
                  '99.9%=' + str(stdata[key][0][4]),
                  '\n', sep='\t', end='\n', file=file)

            print('', 'ExecTime', 'TransNo', 'Weight,%', 'Percent',
                  sep='\t', end='\n', file=file)

            for timekey in stdata[key][0][5]:
                print('', timekey,
                      stdata[key][0][5][timekey][0],
                      stdata[key][0][5][timekey][1],
                      stdata[key][0][5][timekey][2],
                      sep='\t', end='\n', file=file)
