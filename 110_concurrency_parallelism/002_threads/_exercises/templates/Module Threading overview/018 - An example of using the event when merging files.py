_____ _, q__, pathlib


___ writer(wr_file  # ПИСАТЕЛЬ
    w__ True:
        # ожидаем получение данных
        __ data_queue.e..
            # !!!!! проверяем: живы ли потоки читателей `reader()` !!!!!
            __ event_reader.is_set(
                # если очередь пуста и все
                # читатели завершили работу ТО:
                print('Все файлы объединены.')
                # конец работы - завершаем цикл
                break
        else:
            # как только поступили данные
            # извлекаем их и записываем
            r_file, data = data_queue.g..)
            # пишем данные
            print(f'Пишем файл {r_file.name}')
            with open(wr_file, 'a+') as fw:
                # дописываем в начало файла его имя
                fw.write(f'\n\nИмя файла {r_file}\n\n')
                # пишем сами данные
                fw.write(data)


___ reader(i  # ЧИТАТЕЛЬ
    # здесь читаем и обрабатываем данные файлов
    w__ True:
        # Проверяем, есть ли файлы в очереди
        __ files_queue.e..
            print(f'Поток {i} завершен.')
            # выходим из цикла
            break
        # Получаем имя файла из очереди
        r_file = files_queue.g..)
        print(f'Th{i}: Читаем  файл {r_file.name}')
        with open(r_file, 'r') as fr:
            # читаем построчно
            data = []
            ___ line __ fr:
                # обрабатываем данные построчно
                line = line.replace('у', '0').lower()
                # складываем обработанные строки в список
                data.append(line)
            # объединяем данные в текст
            data_all = ''.join(data)
            # Ставим в очередь кортеж (имя_файла, данные)
            data_queue.p..((r_file, data_all))

        # !!!!! включаем управление событиями !!!!!


event_reader = _.Event()
# очередь с названием файлов
files_queue = q__.?
# очередь с обработанными данными
data_queue = q__.?

path = pathlib.Path('.')
# каталог с файлами
test_dir = 'test_dir'
path_dir = path.joinpath(test_dir)
# список файлов
list_files = path_dir.glob('*.txt')

# создаем и заполняем очередь именами файлов
___ file __ list_files:
    files_queue.p..(file)

# общий файл c обработанными данными
write_file = 'multi-thead-file.txt'

__ files_queue.e..
    print('НЕТ файлов для обработки.')
else:
    # пишем в 1 поток. Если данные писать в несколько потоков,
    # то нужно еще использовать блокировщик threading.Lock()
    # или данные в итоговом файле будут перемешаны.
    tw = _.?(t.. writer, a.. (write_file,))
    tw.start()

    # читаем и обрабатываем в 2 потока
    threads = []
    ___ i __ r..(2
        tr = _.?(t.. reader, a.. (i + 1,))
        threads.append(tr)
        tr.start()

    # ждем, когда все файлы прочитаются
    [thread.join() ___ thread __ threads]
    # как все потоки reader() завершены
    # !!!!! скажем об этом writer() !!!!!
    event_reader.set()