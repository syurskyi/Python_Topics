# """
#  Liskov substitution principle says every class that inherit from a parent class, must not replicate functionality
#  already implemented in the parent class.
#
#  The violation of LSP here is that a `Prisoner` is not a suitable
#  substitution of `Person` since they "behave" differently.
#  Remember, the principle is that you should model your class according
#  to their behavior rather than porperties.
# """
#
#
# # BAD PRACTICE
#
# class Person(object):
#
#     def __init__(self, position):
#         self.position = position
#
#     def walk_North(self, dist):
#         self.position[1] += dist
#
#     def walk_East(self, dist):
#         self.position[0] += dist
#
#
# # `Prisoner` is a logicall natural extension of `Person`
# # since they fulfill the "is-a" relation: a `Prisoner` is a `Person`.
# # However, such extension violate LSP in this case.
# class Prisoner(Person):
#     PRISON_LOCATION = [3, 3]
#
#     def __init__(self):
#         super(Prisoner, self).__init__(self.PRISON_LOCATION)
#         self.is_free = False
#
#
# # The issue here is that `Prisoner` inherits `walk_North` and `walk_East` methods
# # from the `Person` which is not logically correct for the `Prisoner` class.
#
# def bad_main():
#     prisoner = Prisoner()
#     print("The prisoner trying to walk to north by 10 and east by -3.")
#
#     try:
#         prisoner.walk_North(10)
#         prisoner.walk_East(-3)
#     except:
#         pass
#
#     print("The location of the prison: {}".format(prisoner.PRISON_LOCATION))
#     print("The current position of the prisoner: {}".format(prisoner.position))
#
#
# # GOOD PRACTICE
#
# """
#  As we can see in `BAD` where a violation
#  of LSP may lead to an unexpected behaviour of sub-types. In our
#  example, "is-a" relation can not directly applied to `Person` and
#  `Prisoner`. The cause is that these two classes "behave" differently.
#  How to fix it? Maybe a better naming will do the trick
# """
#
#
# c_ FreeMan o..
#
#     ___ -  position
#         ??  ?
#
#     ___ walk_North dist
#         p.. 1 +_ ?
#
#     ___ walk_East dist
#         p.. 0 +_ ?
#
#
# # "is-a" relationship no longer holds since a `Prisoner` is not a `FreeMan`.
# c_ PrisonerGood o..
#     PRISON_LOCATION _ 3 3
#
#     ___ -
#         ?position = ty.. ____.P..
#
#
# ___ good_main
#     prisoner _ P..
#     print("The prisoner trying to walk to north by 10 and east by -3.")
#
#     ___
#         ?.wN.. 10
#         ?.wE.. -3
#     ________
#         p..
#
#     print("The location of the prison: @".f.. (?.PR..
#     print("The current position of the prisoner: @".f.. (?.p..
#
#
# __ ______ __ ______
#     print('BAD')
#     print('*' * 10)
#     bad_main()
#     print('*' * 10)
#     print('GOOD')
#     print('*' * 10)
#     good_main()
#     print('*' * 10)
