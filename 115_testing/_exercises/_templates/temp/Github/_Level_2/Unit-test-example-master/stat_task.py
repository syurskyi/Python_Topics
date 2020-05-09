#!/usr/bin/env python3
#-*-coding: utf-8-*-

______ argparse
____ math ______ ceil, floor


c_ Parser(
    """
    Производит подготовку данных для дальнейшей обработки статистическими
    функциями
    """

    ___ data_extr  fileobj, index
        """
        Извлекает данные, производит проверку на количество полезных строк.
        :param fileobj: файловый объект
        :param index: номер столбца (отсчет с 0), в котором должны быть
        "непустые" объекты; по нему отфильтровывается мусор
        мусор
        :return: список со списками данных по каждой строке
        """

        SOURCE _ []
        qty _ 0
        allines _ 0

        for line in fileobj:
            allines +_ 1
            try:
                L _ list(line.split('\t'))
                L[index] == True
            except IndexError:
                pass
            else:
                L[-1] _ L[-1].rstrip()
                SOURCE.append(L)
                qty +_ 1

        print('Извлечено ' + st.(qty) + ' строк из ' + st.(allines))
        r_ SOURCE

    ___ check_pos  source, *heads
        """
        Производит поиск индексов в source[0] для имен heads.
        :param source: список/кортеж со вложенными списками/кортежами
        :param heads: str - имена заголовков столбцов
        :return: [int, int...] - список с позиционными номерами данных
        в списках/кортежах, соответствующих заголовкам столбцов
        """
        number _ []

        for head in heads:
            __ head in source[0]:
                number.append(source[0].index(head))

        r_ number

    ___ int_converter  listobj, *index
        """
        Для каждого из списков с данными преобразует list[index] в integer либо
        выдает исключение с информацией о позиции с неверным типом данных.
        :param listobj: список со вложенными списками данных
        :param index: integer - позиционный номер для списков с данными
        :return: None
        """
        linecount _ 0
        for elem in listobj:
            linecount +_ 1
            for num in index:
                try:
                    elem[num] _ int(elem[num])
                except (TypeError, ValueError
                    print('Неверный формат в ' + st.(num+1) + ' столбце, в ' +\
                          st.(linecount) + ' строке данных.')
                    raise

    ___ key_names  source, index
        """

        :param source: список/кортеж со вложенными списками/кортежами данных
        :param index: integer - позиционный номер для списка/кортежа
        с именами ключей
        :return: list - список неповторяющихся значений для каждого объекта
        списка/кортежа под номером index
        """
        keyname _ []

        for elem in source:
            __ elem[index] in keyname:
                pass
            else:
                keyname.append(elem[index])

        r_ keyname

    ___ fin_prep  fileobj, index, *heads
        """

        :param fileobj: файловый объект
        :param index: номер столбца (отсчет с 0), в котором должны быть
        "непустые" объекты
        :param heads: str - имена заголовков столбцов
        :return: {key: [(),()...]} - словарь, в котором ключи -
        неповторяющиеся bмена в первом объекте head, значения - списки
        с кортежами данных
        """

        SOURCE _ data_extr(fileobj, index)
        head_list _ [head for head in heads]
        data_pos _ check_pos(SOURCE, *head_list)

        SOURCE _ SOURCE[1:]
        int_converter(SOURCE, *data_pos[1:])
        keyname _ key_names(SOURCE, data_pos[0])

        DATAS _ {name: [] for name in keyname}

        for name in keyname:
            for num in data_pos[1:]:
                DATAS[name].append( \
                    tuple( \
                        sorted([x[num] for x in SOURCE __ x[data_pos[0]] == name])))

        r_ DATAS


c_ Statistics:

    ___  -   data
        """
        Сортирует итерируемый объект и преобразует в tuple
        :param data: list/tuple с данными
        """
        data _ tuple(sorted(data))

    ___ minimal
        """
        :return: минимальное значение из self.data
        """
        r_ data[0]

    ___ median
        """
        Если число элементов четное, то вычисляется полусумма значений двух
        средних индексов и округляется вверх до ближайшего целого значения.
        Если число элементов нечетное, то возвращается значение среднего
        индекса.
        :return: статистические 50% (медиану) данных в self.data
        """

        lendata _ len(data)

        __ lendata % 2 == 0:
            r_ ceil((data[lendata//2 - 1] + data[lendata//2]) /2)
            #округление в большую сторону

        else:
            r_ (data[lendata//2])

    ___ percent90
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
        lendata _ len(data)
        index_plus1 _ floor(lendata * 0.9)
        index _ index_plus1 - 1

        __ lendata % 10 == 0:
            r_ data[index]

        else:
            r_ (data[index] + ceil( \
                (data[index_plus1] - data[index]) * \
                (lendata * 0.9 - index_plus1)))

    ___ percent99
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
        lendata _ len(data)
        index_plus1 _ floor(lendata * 0.99)
        index _ index_plus1 - 1

        __ lendata % 100 == 0:
            r_ data[index]

        else:
            r_ (data[index] + ceil( \
                (data[index_plus1] - data[index]) * \
                (lendata * 0.99 - index_plus1)))

    ___ percent999
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
        lendata _ len(data)
        index_plus1 _ floor(lendata * 0.999)
        index _ index_plus1 - 1

        __ lendata % 1000 == 0:
            r_ data[index]

        else:
            r_ (data[index] + ceil( \
                (data[index_plus1] - data[index]) *\
                (lendata * 0.999 - index_plus1)))

    ___ fractions  denom_5
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
        rdata _ [(x - x% -denom) for x in data]
        lendata _ len(rdata)
        fdict _ {number: [0] for number in sorted(set(rdata))}

        for number in rdata:
                fdict[number][0] +_ 1

        for key in fdict:
            fdict[key].append(f..(fdict[key][0] / lendata * 100, '.2f'))

        rkeys _ list(reversed([x for x in fdict.keys()]))

        while rkeys:
            sum _ 0
            for key in rkeys:
                sum +_ fdict[key][0]
            fdict[rkeys[0]].append(f..(sum / lendata * 100, '.2f'))
            rkeys _ rkeys[1:]

        r_ fdict


c_ StatsResult(Statistics

    ___  -   datas
        """
          :param datas: {key: [[],[]...]} или {key: [(),()...]}
        """
        datas _ datas

    ___ run  *list_funcs
        """
        Функция предназначена для автоматизации формирования результатов
        нескольких наборов данных различными методами класса.
        :param list_funcs: str - имена функций-методов класса
        :return: {key: [(),()...]}
        """

        D _ {}

        for key in datas:
            D[key] _ []
            for data in datas[key]:
                data _ tuple(sorted(data)) # for not sorted Source_data
                D[key].append(tuple(x() for x in list_funcs))

        r_ D


__ __name__ == '__main__':

    argparser _ argparse.ArgumentParser()
    argparser.add_argument('-f', '--file')

    file_source _ o..(argparser.parse_args().file, _
    datas _ Parser().fin_prep(file_source, 4, 'EVENT', 'AVGTSMR')
    file_source.close()

    stat _ StatsResult(datas)
    list_funcs _ [stat.minimal, stat.median, stat.percent90, \
                      stat.percent99, stat.percent999, stat.fractions]
    stdata _ stat.run(*list_funcs)

    w__ o..('result_stat.txt',_ __ file:
        for key in stdata.keys(
            print(key, 'min=' + st.(stdata[key][0][0]),
                  '50%=' + st.(stdata[key][0][1]),
                  '90%=' + st.(stdata[key][0][2]),
                  '99%=' + st.(stdata[key][0][3]),
                  '99.9%=' + st.(stdata[key][0][4]),
                  '\n', sep_'\t', end_'\n', file_file)

            print('', 'ExecTime', 'TransNo', 'Weight,%', 'Percent',
                  sep_'\t', end_'\n', file_file)

            for timekey in stdata[key][0][5]:
                print('', timekey,
                      stdata[key][0][5][timekey][0],
                      stdata[key][0][5][timekey][1],
                      stdata[key][0][5][timekey][2],
                      sep_'\t', end_'\n', file_file)
