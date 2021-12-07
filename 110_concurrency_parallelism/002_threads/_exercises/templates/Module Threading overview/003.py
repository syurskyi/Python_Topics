import pathlib, threading, time, queue

def worker(que):
    while True:
        # Получаем задание (имя файла) из очереди
        job = que.get()
        # Путь к новому (обработанному) файлу
        file_write = path_dir_modified.joinpath(job.name)
        # открываем файл из очереди на чтение и
        # новый файл на запись
        with open(job, 'r') as fr, open(file_write, 'w') as fw:
            # дописываем имя файла
            fw.write(f'\n\n============> {file_write}\n\n')
            # читаем данные построчно
            for line in fr:
                # например, заменим букву у на 0
                line = line.replace('у', '0')
                # пишем измененные данные
                fw.write(line)
        # Сообщаем очереди что задача выполнена
        que.task_done()

path = pathlib.Path('.')
# тестовый каталог с файлами
test_dir = 'test_dir'
# Путь к тестовой директории
path_dir = path.joinpath(test_dir)
# получаем список файлов
list_files = path_dir.glob('*.txt')

# каталог с обработанными файлами
test_dir_modified = 'test_dir_modified'
path_dir_modified = path.joinpath(test_dir_modified)
path_dir_modified.mkdir(exist_ok=True)

# создаем и заполняем очередь именами файлов
que = queue.Queue()
for file in list_files:
    que.put(file)

if que.qsize():
    # Создаем и запускаем потоки
    n_thead = 3
    for _ in range(n_thead):
        th = threading.Thread(target=worker, args=(que,), daemon=True)
        th.start()

    # Блокируем дальнейшее выполнение
    # программы до тех пор пока потоки
    # не обслужат все элементы очереди
    que.join()
else:
    print('Файлы не найдены.')