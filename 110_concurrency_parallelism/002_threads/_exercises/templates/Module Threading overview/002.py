# -*- coding: utf-8 -*-

#prepare-data.py

_____ pathlib, r__

path = pathlib.Path('.')
# название тестовой директории
test_dir = 'test_dir'
# Путь к тестовой директории
path_dir = path.joinpath(test_dir)
# создаем тестовый директорий
path_dir.mkdir(exist_ok=True)
# количество создаваемых файлов
n_files = 50

# скобочки {} - это шаблон для метода строки
# str.format() туда вставим имя файла
line = "{} - We will write this line to a file "


__ path_dir.is_dir(
    ___ n __ r..(n_files
        # название файла
        f_name = f'file-{n}.txt'
        # путь к файлу
        path_file = path_dir.joinpath(f_name)
        # Генерируем разное количество строк,
        # которые будут писаться в файл
        data = [line.format(f_name) ___ _ __ r..(r__.randint(5000,15000))]
        # пишем данные в файл
        path_file.write_text('\n'.join(data))