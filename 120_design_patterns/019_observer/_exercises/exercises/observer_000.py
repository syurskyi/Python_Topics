# _____ -f _____ an..
# _____ a.. _____ A.. ab..
# _____ ra.._____ r..r..
# _____ ty.. _____ L..
#
# c_ Subject A..
#     """
#     Интферфейс издателя объявляет набор методов для управлениями подпискичами.
#     """
#
#     ??
#     ___ attach observer O.. __ N..
#         """
#         Присоединяет наблюдателя к издателю.
#         """
#         p..
#
#     ??
#     ___ detach observer O.. __ N..
#         """
#         Отсоединяет наблюдателя от издателя.
#         """
#         p..
#
#     ??
#     ___ notify __ N..
#         """
#         Уведомляет всех наблюдателей о событии.
#         """
#         p..
#
# c_ ConcreteSubject S..
#     """
#     Издатель владеет некоторым важным состоянием и оповещает наблюдателей о его
#     изменениях.
#     """
#
#     _state; in. _ N..
#     """
#     Для удобства в этой переменной хранится состояние Издателя, необходимое всем
#     подписчикам.
#     """
#
#     _observers; Li.. |O..       # list
#     """
#     Список подписчиков. В реальной жизни список подписчиков может храниться в
#     более подробном виде (классифицируется по типу события и т.д.)
#     """
#
#     ___ attach observer O.. __ N..
#         print("Subject: Attached an observer.")
#         _o___.ap.. ?
#
#     ___ detach  observer O.. __ N..
#         _o__.re.. ?
#
#     """
#     Методы управления подпиской.
#     """
#
#     ___ notify  __ N..
#         """
#         Запуск обновления в каждом подписчике.
#         """
#
#         print("Subject: Notifying observers...")
#         ___ observer __ ?_o..
#             ?.up.. ?
#
#     ___ some_business_logic __ N..
#         """
#         Обычно логика подписки – только часть того, что делает Издатель.
#         Издатели часто содержат некоторую важную бизнес-логику, которая
#         запускает метод уведомления всякий раз, когда должно произойти что-то
#         важное (или после этого).
#         """
#
#         print("\nSubject: I'm doing something important.")
#         ?_s.. _ r..ra.. 0 10
#
#         print(_*Subject: My state has just changed to: |_s..")
#         ?n..
#
#
# c_ Observer A..
#     """
#     Интерфейс Наблюдателя объявляет метод уведомления, который издатели
#     используют для оповещения своих подписчиков.
#     """
#
#     ??
#     ___ update  subject S.. __ N..
#         """
#         Получить обновление от субъекта.
#         """
#         p..
#
# """
# Конкретные Наблюдатели реагируют на обновления, выпущенные Издателем, к которому
# они прикреплены.
# """
#
#
# c_ ConcreteObserverA O..
#     ___ update  subject S.. __ N..
#         __ ?._s.. < 3
#             print("ConcreteObserverA: Reacted to the event")
#
#
# c_ ConcreteObserverB O..
#     ___ update subject S.. __ N..
#         __ ?._s.. __ 0 o. ?._s.. >_ 2
#             print("ConcreteObserverB: Reacted to the event")
#
#
# __ _______ __ ______
#     # Клиентский код.
#
#     subject = C..
#
#     observer_a = C_A
#     ?.a.. ?
#
#     observer_b = C_B
#     ?.a.. ?
#
#     s__.s...
#     s__.s...
#
#     s__.de.. o_a
#
#     s__.s..