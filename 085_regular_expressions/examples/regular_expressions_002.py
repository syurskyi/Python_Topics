# Регулярное выражение — это строка, задающая шаблон поиска подстрок в тексте. Одному шаблону может соответствовать
# много разных строчек. Термин «Регулярные выражения» является переводом английского словосочетания «Regular
# expressions». Перевод не очень точно отражает смысл, правильнее было бы «шаблонные выражения». Регулярное выражение,
# или коротко «регулярка», состоит из обычных символов и специальных командных последовательностей. Например,
# \d задаёт любую цифру, а \d+ — задает любую последовательность из одной или более цифр. Работа с регулярками
# реализована во всех современных языках программирования. Однако существует несколько «диалектов», поэтому функционал
# регулярных выражений может различаться от языка к языку. В некоторых языках программирования регулярками пользоваться
# очень удобно (например, в питоне), в некоторых — не слишком (например, в C++).


# simple text    В точности текст «simple text»

# \d{5}     Последовательности из 5 цифр \d означает любую цифру {5} — ровно 5 раз

# \d\d/\d\d/\d{4}    	Даты в формате ДД/ММ/ГГГГ (и прочие куски, на них похожие, например, 98/76/5432)

# \b\w{3}\b     	Слова в точности из трёх букв \b означает границу слова (с одной стороны буква, а с другой — нет)
#                   \w — любая буква,{3} — ровно три раза

# [-+]?\d+          Целое число, например, 7, +17, -42, 0013 (возможны ведущие нули)
#                   [-+]? — либо -, либо +, либо пусто
#                   \d+ — последовательность из 1 или более цифр

# [-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?   Действительное число, возможно в экспоненциальной записи
#                                                 Например, 0.2, +5.45, -.4, 6e23, -3.17E-14.
#                                                 См. ниже картинку.