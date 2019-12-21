# Регулярные выражения – это небольшой язык, который вы можете использовать внутри Python и многих других языках
# программирования. Зачастую регулярные выражения упоминаются как “regex”, “regexp” или просто “RE”, от reuglar
# expressions. Такие языки как Perl и Ruby фактически поддерживают синтаксис регулярных выражений прямо в собственном
# языке. Python же поддерживает благодаря библиотеки, которую вам нужно импортировать. Основное использование регулярных
# выражений – это сопоставление строк. Вы создаете правила сопоставления строк, используя регулярные выражения,
# после чего вы применяете их в строке, чтобы увидеть, присутствуют ли какие-либо сопоставления. «Язык» регулярных
# выражений на самом деле весьма короткий, так что вы вряд ли сможете использовать для всех своих нужд при сопоставлении
# строк. Кроме того, работая с задачами, в которых вы используете регулярные выражения, вы можете заметно усложнить
# процесс, а лечение багов в таком случае очень трудоемкое. В таких случаях вам нужно просто использовать Python.
# Обратите внимание на то, что Python – идеальный язык для парсинга текстов согласно его правам, и его можно
# использовать во всем, что вы делаете с регулярными выражениями. Однако, на это может потребоваться много кода,
# который будет работать медленнее, чем это делают регулярные выражения, так как они скомпилированы и выполнены в С.
# Согласуемые символы
#
# Когда вам нужно найти символ в строке, в большей части случаев вы можете просто использовать этот символ или строку.
# Так что, когда нам нужно проверить наличие слова «dog», то мы будем использовать буквы в dog. Конечно, существуют
# определенные символы, которые заняты регулярными выражениями. Они так же известны как метасимволы. Внизу изложен
# полный список метасимволов, которые поддерживают регулярные выражения Python:
# Давайте взглянем как они работают. Основная связка метасимволов, с которой вы будете сталкиваться, это квадратные
# скобки: [ и ]. Они используются для создания «класса символов», который является набором символов, которые вы можете
# сопоставить. Вы можете отсортировать символы индивидуально, например, так: [xyz]. Это сопоставит любой внесенный в
# скобки символ. Вы также можете использовать тире для выражения ряда символов, соответственно: [a-g]. В этом примере
# мы сопоставим одну из букв в ряде между a и g. Фактически для выполнения поиска нам нужно добавить начальный искомый
# символ и конечный. Чтобы упростить это, мы можем использовать звездочку. Вместо сопоставления *, данный символ
# указывает регулярному выражению, что предыдущий символ может быть сопоставлен 0 или более раз. Давайте посмотрим на
# пример, чтобы лучше понять о чем речь:

# ‘a[b-f]*f

# Этот шаблон регулярного выражения показывает, что мы ищем букву а, ноль или несколько букв из нашего класса, [b-f]
# и поиск должен закончиться на f. Давайте используем это выражение в Python:

import re
text = 'abcdfghijk'

parser = re.search('a[b-f]*f')
print(parser.group()) # 'abcdf'

# В общем, это выражение просмотрит всю переданную ей строку, в данном случае это abcdfghijk.
# Выражение найдет нашу букву «а» в начале поиска. Затем, в связи с тем, что она имеет класс символа со звездочкой
# в конце, выражение прочитает остальную часть строки, что бы посмотреть, сопоставима ли она. Если нет, то выражение
# будет пропускать по одному символу, пытаясь найти совпадения. Вся магия начинается, когда мы вызываем поисковую
# функцию модуля re. Если мы не найдем совпадение, тогда мы получим None. В противном случае, мы получим объект Match.
# Чтобы увидеть, как выглядит совпадение, вам нужно вызывать метод group. Существует еще один повторяемый метасимвол,
# аналогичный *. Этот символ +, который будет сопоставлять один или более раз. Разница с *, который сопоставляет от
# нуля до более раз незначительна, на первый взгляд.
# Символу + необходимо как минимум одно вхождение искомого символа. Последние два повторяемых метасимвола работают
# несколько иначе. Рассмотрим знак вопроса «?», применение которого выгладит так: “co-?op”. Он будет сопоставлять и
# “coop” и “co-op”. Последний повторяемый метасимвол это {a,b}, где а и b являются десятичными целыми числами.
# Это значит, что должно быть не менее «а» повторений, но и не более «b». Вы можете попробовать что-то на подобии этого:

# xb{1,4}z

# Это очень примитивный пример, но в нем говорится, что мы сопоставим следующие комбинации: xbz, xbbz, xbbbz и xbbbbz,
# но не xz, так как он не содержит «b».
#
# Следующий метасимвол это ^. Этот символ позволяет нам сопоставить символы которые не находятся в списке нашего класса.
# Другими словами, он будет дополнять наш класс. Это сработает только в том случае, если мы разместим ^ внутри нашего
# класса. Если этот символ находится вне класса, тогда мы попытаемся найти совпадения с данным символом. Наглядным
# примером будет следующий: [ˆa]. Так, выражения будет искать совпадения с любой буквой, кроме «а». Символ ^ также
# используется как анкор, который обычно используется для совпадений в начале строки.
#
# Существует соответствующий якорь для конце строки – «$». Мы потратим много времени на введение в различные концепты
# применения регулярных выражений. В следующих параграфах мы углубимся в более подробные примеры кодов.

# Поиск сопоставлений шаблонов
#
# Давайте уделим немного времени тому, чтобы научиться основам сопоставлений шаблонов. Используя Python для поиска
# шаблона в строке, вы можете использовать функцию поиска также, как мы делали это в предыдущем разделе этой статьи.
# Вот пример:

import re

text = "The ants go marching one by one"

strings = ['the', 'one']

for string in strings:
    match = re.search(string, text)
    if match:
        print('Found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))


# В этом примере мы импортируем модуль re и создаем простую строку. Когда мы создаем список из двух строк, которые мы
# будем искать в главной строке. Далее мы делаем цикл над строками, которые хотим найти и запускаем для них поиск.
# Если есть совпадения, мы выводим их. В противном случае, мы говорим пользователю, что искомая строка не была найдена

# Существует несколько других функций, которые нужно прояснить в данном примере. Обратите внимание на то, что мы
# вызываем span. Это дает нам начальную и конечную позицию совпавшей строки. Если вы выведите text_pos, которому мы
# назначили span, вы получите кортеж на подобие следующего: (21, 24). В качестве альтернативы вы можете просто вызвать
# методы сопоставления, что мы и сделаем далее. Мы используем начало и конец для того, чтобы взять начальную и конечную
# позицию сопоставления, это должны быть два числа, которые мы получаем из span.
# Коды поиска
#
# Существует несколько специальных выражений, которые вы можете искать, используя Python. Вот короткий список с кратким
# пояснением каждого кода:
#
#     \d соответствует цифре
#     \D соответствует не цифре
#     \s соответствует пустому полю (пробел)
#     \S соответствует заполненному полю
#     \w соответствует алфавитно-цифровому значению
#     \W соответствует не алфавитно-цифровому значению
#
# Вы можете использовать эти коды внутри класса символа вот так: [\d]. Таким образом, это позволит нам найти любую
# цифру, находящейся в пределе от 0 до 9. Я настаиваю на том, чтобы вы попробовали остальные коды выхода лично.

# Компилирование
#
# Модуль re позволяет вам «компилировать» выражение, которое вы ищите чаще всего. Это также позволит вам превратить
# выражение в объект SRE_Pattern. Вы можете использовать этот объект в вашей функции поиска в будущем. Давайте
# используем код из предыдущего примера и изменим его, чтобы использовать компилирование:

import re

text = "The ants go marching one by one"

strings = ['the', 'one']

for string in strings:
    regex = re.compile(string)
    match = re.search(regex, text)
    if match:
        print('Found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))

# Обратите внимание на то, что здесь мы создаем объект паттерна, вызывая compile в каждой строке нашего списка, и
# назначаем результат переменной – регулярному выражению. Далее мы передаем это выражение нашей поисковой функции.
# Остальная часть кода остается неизменной. Основная причина, по которой используют компилирование это сохранить
# выражение для повторного использования в вашем коде в будущем. В любом случае, компилирование также принимает флаги,
# которые могут быть использованы для активации различных специальных функций. Мы рассмотрим это далее.
# Обратите внимание: когда вы компилируете паттерны, они автоматически кэшируются, так что если вы не особо используете
# регулярные выражения в своем коде, тогда вам не обязательно сохранять компилированный объект как переменную.
# Флаги компиляции
#
# Существует 7 флагов компиляции, которые содержатся в Python 3. Эти флаги могут изменить поведение вашего паттерна.
# Давайте пройдемся по каждому из них, затем рассмотрим, как их использовать.
# re.A / re.ASCII
#
# Флаг ASCII указывает Python сопоставлять против ASCII, вместо использования полного Юникода для сопоставления,
# в сочетании со следующими кодами: w, W, b, B, d, D, s и S. Также существует флаг re.U / re.UNICODE, который
# используется в целях обратной совместимости. В любом случае, эти флаги являются излишеством, так как Python выполняет
# сопоставления в Юникоде в автоматическом режиме.
# re.DEBUG
#
# Данный флаг показывает информацию о дебаге вашего скомпилированного выражения.
# re.I / re.IGNORECASE
#
# Если вам нужно выполнить сравнение без учета регистра, тогда этот флаг – то, что вам нужно. Если ваше выражение было
# [a-z] и вы скомпилировали его при помощи этого флага, то ваш паттерн сопоставит заглавные буквы в том числе.
# Это также работает для Юникода и не влияет на текущую локаль.
# re.L / re.LOCALE
#
# Данный флаг делает коды: w, W, b, B, d, D, s и S зависимыми от нынешней локали. Однако, в документации говорится,
# что вы не должны зависеть от данного флага, так как механизм локали сам по себе очень ненадежный. Вместо этого, лучше
# используйте сопоставление Юникода. Далее в документации говорится, что данный флаг имеет смысл использовать только
# в битовых паттернах.

# re.M / re.MULTILINE
#
# Когда вы используете данный флаг, вы говорите Python, чтобы он использовал символ паттерна ^ для начала строки, и
# начало каждой линии. Он также указывает Python, что $ должен сопоставить конец каждой строки и конец каждой линии,
# что не сильно отличается от их значений по умолчанию. Вы можете обратиться к документации для дополнительной
# информации.
# re.S / re.DOTALL
#
# Этот забавный флаг указывает метасимволу «.» (период) сопоставить любой символ. Без этого флага, данный метасимвол
# будет сопоставлять все, что угодно, но не новую строку.
# re.X / re.VERBOSE
#
# Если вы считаете, что ваши регулярные выражения не слишком читабельные, тогда данный флаг – это то, что вам нужно.
# Он позволяет визуально разделять логические секции ваших регулярных выражений, и даже добавлять комментарии!
# Пустое пространство внутри паттерна будет игнорироваться, кроме того случая, если классу символа или пробелу
# предшествует обратная косая черта.
# Использование флага компиляции
#
# Давайте уделим немного времени, и посмотрим на простой пример, в котором используется флаг компиляции VERBOSE.
# Неплохой пример – взять обычную электронную почту и использовать поиск регулярных выражений,
# таких как r’[w.-]+@[w.-]+’ и добавить комментарии, используя флаг VERBOSE. Давайте посмотрим:

re.compile('''
           [\w\.-]+
           @
           [\w\.-]+'
           ''',
           re.VERBOSE)

# Давайте пройдем дальше и научимся находить множественные совпадения.
# Находим множественные совпадения
#
# До этого момента мы научились только находить первое совпадение в строке. Но что если у вас строка, в которой
# содержится множество совпадений? Давайте посмотрим, как найти одно:

import re

silly_string = "the cat in the hat"
pattern = "the"

match = re.search(pattern, text)
print(match.group()) # 'the'

# Теперь, как вы видите, у нас есть два экземпляра слова the, но нашли мы только одно. Существует два метода,
# чтобы найти все совпадения. Первый, который мы рассмотрим, это использование функции findall:

import re

silly_string = "the cat in the hat"
pattern = "the"

a = re.findall(pattern, silly_string)
print(a) # ['the', 'the']

# Функция findall будет искать по всей переданной ей строке, и впишет каждое совпадение в список. По окончанию поиска
# вышей строки, она выдаст список совпадений. Второй способ найти несколько совпадений, это использовать функцию
# finditer:

import re

silly_string = "the cat in the hat"
pattern = "the"

for match in re.finditer(pattern, silly_string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=match.group(), begin=match.start(),
        end=match.end())

    print(s)

# Как вы могли догадаться, метод finditer возвращает итератор экземпляров Match, вместо строк, которые мы получаем
# от findall. Так что нам нужно немного подформатировать результаты перед их выводом. Попробуйте запустить данный код
# и посмотрите, как он работает.
# Сложности с обратными косыми
#
# Обратные косые немного усложняют жизнь в мире регулярных выражений Python. Это связанно с тем, что регулярные
# выражения используют обратные косые для определения специальных форм, или для того, чтобы искать определенный символ,
# вместо того, чтобы вызывать его. Как если бы мы искали символ доллара $. Если мы не используем обратную косую для
# этого, нам нужно просто создать анкор. Проблема возникает по той причине, что Python использует символ обратной
# косой по той же причине в литеральных строках.
#
# Давайте представим, что вам нужно найти строку на подобии этой: «python». Для её поиска в регулярном выражении,
# вам нужно будет использовать обратную косую, но, так как Python также использует обратную косую, так что на выходе
# вы получите следующий поисковый паттерн: «\\python» (без скобок). К счастью, Python поддерживает сырые строки,
# путем подстановки буквы r перед строкой. Так что мы можем сделать выдачу более читабельной, введя следующее:
# r”\python”. Так что если вам нужно найти что-то с обратной косой в названии, убедитесь, что используете сырые строки
# для этой цели, иначе можете получить совсем не то, что ищете.
# Подведем итоги
#
# В данной статье мы коснулись только вершины айсберга, под названием регулярные выражения. Существуют целые книги,
# посвященные регулярным выражениям, однако эта статья, по крайней мере, дает вам базовое представление для начала.
# Теперь вы можете искать углубленные примеры и обратиться к документации, скорее всего не один и не два раза, пока вы
# учитесь. Но помните о том, что регулярные выражения – очень удобный и полезный инструмент.