# -*- coding: utf-8 -*-

import locale

import locale
# Для кодировки windows-1251
print(locale.setlocale(locale.LC_ALL, "Russian_Russia.1251"))
# 'Russian_Russia.1251'
# Устанавливаем локаль по умолчанию
print(locale.setlocale(locale.LC_ALL, ""))
# 'Russian_Russia.1251'
# Получаем текущее значение локали для всех категорий
print(locale.getlocale())
# ('Russian_Russia', '1251')
# Получаем текущее значение категории locale.LC_COLLATE
print(locale.getlocale(locale.LC_COLLATE))
# ('Russian_Russia', '1251')


print(locale.localeconv())
# {'mon_decimal_point': ',', 'int_frac_digits': 2, 'p_sep_by_space': 0,
# 'frac_digits': 2, 'thousands_sep': '\xa0', 'n_sign_posn': 1,
# 'decimal_point': ',', 'int_curr_symbol': 'RUR', 'n_cs_precedes': 0,
# 'p_sign_posn': 1, 'mon_thousands_sep': '\xa0', 'negative_sign': '-',
# 'currency_symbol': 'р.', 'n_sep_by_space': 0, 'mon_grouping': [3, 0],
# 'p_cs_precedes': 0, 'positive_sign': '', 'grouping': [3, 0]}
