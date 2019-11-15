# -*- coding: utf-8 -*-

# ___ benchmark func
#     """
#     Декоратор, выводящий время, которое заняло
#     выполнение декорируемой функции.
#     """
#     _____ ti00
#     ___ wrapper 0a__ 00k__
#         t _ ti00.cl00||
#         res _ f00 0a__ 00k__
#         print f00.__n__ ti00.c00|| - t
#         r_ r00
#
#     r_ w00
#
#
# ___ logging func
#     """
#     Декоратор, логирующий работу кода.
#     (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
#     """
#
#     ___ wrapper 0a__ 00k__
#         res = f00 0a__ 00k__
#         print f00.__n__ a__ k__
#         r_ r00
#
#     r_ w00
#
#
# ___ counter func
#     """
#     Декоратор, считающий и выводящий количество вызовов
#     декорируемой функции.
#     """
#
#     ___ wrapper 0a__ 00k__
#         w00.co00 += 1
#         res _ f00 0a__ 00k__
#         print *|0| была вызвана: |1|x*.f____|f00.__n__ w000.c00||
#         r_ r00
#
#     w00.c00 _ 0
#     r_ w00
#
#
# 0b___
# 0ll___
# 0c___
# ___ reverse_string string
#     r_ st_ rev___ string
#
#
# print r000 А роза упала на лапу Азора
# print reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, "
#                "a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash,"
#                " a jar, sore hats, a peon, a canal: Panama!")
#
# # выведет:
# # reverse_string ('А роза упала на лапу Азора',) {}
# # wrapper 0.0
# # reverse_string была вызвана: 1x
# # арозА упал ан алапу азор А
# # reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!',) {}
# # wrapper 0.0
# # reverse_string была вызвана: 2x
# # !amanaP :lanac a ,noep a ,stah eros ,raj a ,hsac ,oloR a ,tur a ,mapS ,snip ,eperc a ,)lemac a ro( niaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,inoracam ,elacrep ,epins ,spam ,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,nalp a ,nam A
#
#
#
# # Таким образом, декораторы можно применить к любой функции, расширив её функционал и не переписывая ни строчки кода!
#
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
#
#
# ____ h___.cli__ __ httplib
#
#
# 0b___
# 0l____
# 0c___
# ___ get_random_futurama_quote
#     conn _ htt__.HTTPConn00 slashdot.org:80
#     conn.req___  HEAD /index.html
#     ___ key value i_ conn.getresponse||.getheaders||
#         i_ k00.startsw00 x-b o_ k00.startsw00 x-f
#             r__ value
#     r_  Эх, нет... не могу!
#
#
# print get_random_futurama_quote
# print get_random_futurama_quote
#
# # outputs:
# # get_random_futurama_quote () {}
# # wrapper 0.02
# # get_random_futurama_quote была вызвана: 1x
# # The laws of science be a harsh mistress.
# # get_random_futurama_quote () {}
# # wrapper 0.01
# # get_random_futurama_quote была вызвана: 2x
# # Curse you, merciful Poseidon!