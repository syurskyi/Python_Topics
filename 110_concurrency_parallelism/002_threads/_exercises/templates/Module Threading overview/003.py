_____ p__, _, t__, q__

___ worker(que
    w__ T..:
        # Получаем задание (имя файла) из очереди
        job = que.g..)
        # Путь к новому (обработанному) файлу
        file_write = path_dir_modified.j..(job.name)
        # открываем файл из очереди на чтение и
        # новый файл на запись
        with open(job, 'r') as fr, open(file_write, 'w') as fw:
            # дописываем имя файла
            fw.write(f'\n\n============> {file_write}\n\n')
            # читаем данные построчно
            ___ line __ fr:
                # например, заменим букву у на 0
                line = line.replace('у', '0')
                # пишем измененные данные
                fw.write(line)
        # Сообщаем очереди что задача выполнена
        que.t..

path = p__.?('.')
# тестовый каталог с файлами
test_dir = 'test_dir'
# Путь к тестовой директории
path_dir = path.j..(test_dir)
# получаем список файлов
list_files = path_dir.glob('*.txt')

# каталог с обработанными файлами
test_dir_modified = 'test_dir_modified'
path_dir_modified = path.j..(test_dir_modified)
path_dir_modified.m..(exist_ok=T..)

# создаем и заполняем очередь именами файлов
que = q__.?
___ file __ list_files:
    que.p..(file)

__ que.qsize(
    # Создаем и запускаем потоки
    n_thead = 3
    ___ _ __ r..(n_thead
        th = _.?(t.. worker, a.. (que,), daemon=T..)
        th.start()

    # Блокируем дальнейшее выполнение
    # программы до тех пор пока потоки
    # не обслужат все элементы очереди
    que.join()
else:
    print('Файлы не найдены.')