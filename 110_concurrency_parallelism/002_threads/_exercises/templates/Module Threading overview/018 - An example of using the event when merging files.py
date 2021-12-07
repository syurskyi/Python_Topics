import threading, queue, pathlib


def writer(wr_file):  # ПИСАТЕЛЬ
    while True:
        # ожидаем получение данных
        if data_queue.empty():
            # !!!!! проверяем: живы ли потоки читателей `reader()` !!!!!
            if event_reader.is_set():
                # если очередь пуста и все
                # читатели завершили работу ТО:
                print('Все файлы объединены.')
                # конец работы - завершаем цикл
                break
        else:
            # как только поступили данные
            # извлекаем их и записываем
            r_file, data = data_queue.get()
            # пишем данные
            print(f'Пишем файл {r_file.name}')
            with open(wr_file, 'a+') as fw:
                # дописываем в начало файла его имя
                fw.write(f'\n\nИмя файла {r_file}\n\n')
                # пишем сами данные
                fw.write(data)


def reader(i):  # ЧИТАТЕЛЬ
    # здесь читаем и обрабатываем данные файлов
    while True:
        # Проверяем, есть ли файлы в очереди
        if files_queue.empty():
            print(f'Поток {i} завершен.')
            # выходим из цикла
            break
        # Получаем имя файла из очереди
        r_file = files_queue.get()
        print(f'Th{i}: Читаем  файл {r_file.name}')
        with open(r_file, 'r') as fr:
            # читаем построчно
            data = []
            for line in fr:
                # обрабатываем данные построчно
                line = line.replace('у', '0').lower()
                # складываем обработанные строки в список
                data.append(line)
            # объединяем данные в текст
            data_all = ''.join(data)
            # Ставим в очередь кортеж (имя_файла, данные)
            data_queue.put((r_file, data_all))

        # !!!!! включаем управление событиями !!!!!


event_reader = threading.Event()
# очередь с названием файлов
files_queue = queue.Queue()
# очередь с обработанными данными
data_queue = queue.Queue()

path = pathlib.Path('.')
# каталог с файлами
test_dir = 'test_dir'
path_dir = path.joinpath(test_dir)
# список файлов
list_files = path_dir.glob('*.txt')

# создаем и заполняем очередь именами файлов
for file in list_files:
    files_queue.put(file)

# общий файл c обработанными данными
write_file = 'multi-thead-file.txt'

if files_queue.empty():
    print('НЕТ файлов для обработки.')
else:
    # пишем в 1 поток. Если данные писать в несколько потоков,
    # то нужно еще использовать блокировщик threading.Lock()
    # или данные в итоговом файле будут перемешаны.
    tw = threading.Thread(target=writer, args=(write_file,))
    tw.start()

    # читаем и обрабатываем в 2 потока
    threads = []
    for i in range(2):
        tr = threading.Thread(target=reader, args=(i + 1,))
        threads.append(tr)
        tr.start()

    # ждем, когда все файлы прочитаются
    [thread.join() for thread in threads]
    # как все потоки reader() завершены
    # !!!!! скажем об этом writer() !!!!!
    event_reader.set()