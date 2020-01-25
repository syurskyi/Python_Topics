# # -*- coding: utf-8 -*-
#
# # Кроме того, можно указать привязку только к началу или только к концу строки
# _______ __                     # Подключаем модуль
# p _ __.c.. _ 0-9 1? 2?  __.3?)          # 1.One or more occurrences | 2.Ends with | 3.Makes a period (dot) match any character, including a newline.
# __ ?.s..("Строка245"):
#     print("Есть число в конце строки")
# ____
#     print("Нет числа в конце строки")
# # Выведет: Есть число в конце строки
# p _ __.c.. _ 1? 0-9 2?  __.3?          # 1.Starts with | 2.One or more occurrences | 3.Makes a period (dot) match any character, including a newline.
# __ ?.s..("Строка245"):
#     print("Есть число в начале строки")
# ____
#     print("Нет числа в начале строки")
# # Выведет: Нет числа в начале строки
# input()
#
# # Поддерживаются также два метасимвола, позволяющие указать привязку к началу или концу слова:
# # t \Ь - привязка к началу слова (началом слова считается пробел или любой символ, не
# # являющийся буквой, цифрой или знаком подчеркивания);
# # t \В- привязка к позиции, не являющейся началом слова.
#
#
# p _ __.c.. _ 1? python 1?")                           # 1.привязка к началу слова
# print("Найдено" __ ?.s..("python") ____ "Нет")
# # Найдено
# print("Найдено" __ ?.s..("pythonware") ____ "Нет")
# # Нет
# p _ __.c.. _ 1? th 1?")                              # 1.привязка к позиции, не являющейся началом слова.
# print("Найдено" __ ?.s..("python") ____ "Нет")
# # Найдено
# print("Найдено" __ ?.s..("this") ____ "Нет")
# # Нет
#
# # В квадратных скобках [] можно указать символы, которые могут встречаться на этом месте
# # в строке. Можно перечислить символы подряд или указать диапазон через дефис:
# # t [09) - соответствует числу О или 9;
# # t [О-9] - соответствует любому числу от О до 9;
# # t r абв: - соответствует буквам «а». «б» и «в»;
# # t (а-гJ - соответствует буквам «а». «б». «в» и «г»;
# # t [а-яёj - соответствует любой букве от «а» до «я»;
# # t [АБВ] - соответствует буквам «А». «Б» и «В»;
# # t [Ji.-ЯЁJ - соответствует любой букве от «А» до <<Я»;
# # t [а-яА-ЯёЁj - соответствует любой русской букве в любом регистре;
# # t [ О-9а-. .:..::.-яеtа-=.::.-::::: - любая цифра и любая буква независимо от регистра и языка.
# # ВНИМАНИЕ/
# # Буква «ё» не входит в диапазон [а-я:J, а буква «Е» - в диапазон [А-Я].
# # Значение в скобках инвертируется. ес.1и после первой скобки вставить символ ,, . Таким образом можно указать сн,1во.1ы. которых не должно быть на этом месте в строке:
# # t [ · :?: - не uифра О и.1и 9:
# # • [ · c,-sJ - не цифра от О .10 9:
# # t [ · а-�-=-.-.s:ё::::�-=..:..-:: - не буква.
#
# # Как вы уже знаете, точка теряет свое спеuиальное значение. если ее заключить в квадратные скобки. Кроме того, внутри квадратных скобок могут встретиться символы, которые
# # имеют специальное значение (например, ·, и -). Символ · теряет свое спешшльное значение,
# # если он не расположен сразу после открывающей квадратной скобки. Чтобы отменить специальное значение символа -, его необходимо указать после перечисления всех символов,
# # перед закрывающей квадратной скобкой или сразу после открывающей квадратной скобки.
# # Все специальные символы можно сделать обычными, если перед ними указать символ\.
# # Метасимвол I позволяет сделать выбор между альтернативными значениями. Выражение
# # n lm соответствует одному из символов: n или m.
#
#
# p _ __.c.. _ красн( ая 1? ое )")                      # 1.позволяет сделать выбор между альтернативными значениями.
# print("Найдено" __ ?.s..("красная") ____ "Нет")
# # Найдено
# print("Найдено" __ ?.s..("красное") ____ "Нет")
# # Найдено
# print("Найдено" __ ?.s..("красный") ____ "Нет")
# # Нет

 # Вместо перечисления символов можно использовать стандартные классы:
# # • \d- соответствует любой цифре. При указании флага А (AScrr) эквивалентно [О-9];
# # t \w - соответствует любой букве, uифре или символу подчеркивания. При указании флага A(ASCII) эквивалентно
# # [a-zA-Z0-9_];
# # • \s - тобой пробельный символ. При указании флага А (AScrr) эквивалентно
# # [\t\n\r\f\v];
# # t \D- не цифра. При указании флага А (AScrr) эквивалентно [ ЛО-9];
# # • \W - не буква, не цифра и не символ подчеркивания. При указании флага А (ASCII) эквивалентно [
# # л a-zA-Z0-9_];
# # • \S - не пробельный символ. При указании флага А (AScrr) эквивалентно ["\t\n\r\f\v).
# # ПРИМЕЧАНИЕ
# # В Python 3 поддержка Unicode в регулярных выражениях установлена по умолчанию. При
# # этом все классы трактуются гораздо шире. Так, класс \d соответствует не только десятичным цифрам, но и другим цифрам
# # из кодировки Unicode, - например, дробям, класс \w
# # включает не только латинские буквы, но и любые другие, а класс \s охватывает также неразрывные пробелы.
# # Поэтому на практике лучше явно указывать символы внутри квадратных скобок, а не использовать классы.
# # Количество вхождений символа в строку задается с помощью квантификаторов:
# # t { n} - n вхождений символа в строку. Например, шаблон r""' [ 0-9 J { 2 } $" соответствует
# # двум вхождениям любой цифры;
# # t {n,} - n или более вхождений символа в строку. Например, шаблон r"" [О-9) {2, }$"
# # соответствует двум и более вхождениям любой цифры;
# # t {n,m} - не менее n и не более m вхождений символа в строку. Числа указываются через
# # запятую без пробела. Например, шаблон r""' [О-9] {2, 4 }$" соответствует от двух до
# # четырех вхождений любой цифры;
# # t * - ноль или большее число вхождений символа в строку. Эквивалентно комбинации
# # {о' } ;
#
# # + - одно или большее число вхождений символа в строку. Эквивалентно комбинации
# # { 1, } ;
# # • ? - ни одного или одно вхождение символа в строку. Эквивалентно комбинации {о, 1}.
# # Все квантификаторы являются «жадными». При поиске соответствия ищется самая длинная
# # подстрокa соответствующая шаблону, и не учитываются более короткие соответствия. Рассмотрим это на примере и получим
# # содержимое всех тегов <Ь>, вместе с тегами:
#
# s _ "<b>Text1</b>Text2<b>Text3</b>"
# p _ __.c.. _ <b>. 1? </b> __.2?    # 1.Zero or more occurrences | 2.Makes a period (dot) match any character, including a newline.
# ?.f.. ?
# # ['<b>Text1</b>Text2<b>Text3</b>']
