# ########################################################################################################################
# ____ a.. ______ A.. a..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ Context m..
#     """Context Class for State Mode"""
#
#     ___ -
#         __states    # list
#         __curState _ N...
#         # Attributes that depend on state changes. When this variable is jointly determined by multiple variables, it can be defined separately as a class.
#         __stateInfo _ 0
#
#     ___ addState state
#         __ ? no. __ __s..
#             __s__.ap.. ?
#
#     ___ changeState state
#         __ ? __ N...
#             r_ F...
#         __ __c.. __ N...
#             print("Initialized to" ?.gN..
#         ____
#             print("by", __c__.gN.. "Becomes", ?.gN..
#         __c__ _ ?
#         aS.. ?
#         r_ T..
#
#     ___ getState
#         r_ __c__
#
#     ___ _setStateInfo stateInfo
#         __?  ?
#         ___ ? __ __s..
#             __ s___.iM.. ?
#                 cS... s..
#
#     ___ _gSI..
#         r_ __s...
#
#
# c_ State
#     """Base class for states"""
#
#     ___ - name
#         __?  ?
#
#     ___ getName
#         r_ __?
#
#     ___ isMatch stateInfo
#         "Whether the state property stateInfo is within the current state range"
#         r_ F..
#
#     ??
#     ___ behavior context
#         p..
#
#
#
# # Demo achieve
#
# c_ Water C..
#     """water(H2O)"""
#
#     ___ -
#         s___. -
#         aS.. S.. *S..
#         aS.. L.. *L..
#         aS.. G..*G..
#         sT.. 25
#
#     ___ getTemperature
#         r_ _gSI..
#
#     ___ setTemperature temperature
#         _sSI.. ?
#
#     ___ riseTemperature step
#         setTemperature gT.. + ?
#
#     ___ reduceTemperature step
#         sT.. gT.. - ?
#
#     ___ behavior
#         state _ gS..
#         __ isi.. ? S...
#             ?.b.. ?
#
#
# # Singleton decorator
# ___ singleton ___ $  $$
#     "Construct a singleton decorator"
#     instance _     # dict
#
#     ___ __singleton $ $$
#         __ ___ no. i. i..
#             i.. |___ _ ___|$ $$
#         r_ i...|
#
#     r_ __s..
#
#
# ?s..
# c_ SolidState S..
#     """Solid"""
#
#     ___ - name
#         s_. - ?
#
#     ___ isMatch  stateInfo
#         r_ sI.. < 0
#
#     ___ behavior context
#         print("I have a cold personality and my current temperature" ?._gSI..
#               "*C, I am as strong as steel, as a cold-blooded animal, please hit me with people, hehe ...")
#
#
# ?s..
# c_ LiquidState S..
#     """Liquid"""
#
#     ___ - name
#         s___. -_ ?
#
#     ___ isMatch stateInfo
#         r_ ? >_ 0 an. ? < 100
#
#     ___ behavior context
#         print("I have a gentle personality and my current temperature" ?._gSI..
#               "℃, I can moisturize all things, drinking I can make you more energetic ...")
#
# ?s..
# c_ GaseousState S..
#     """Gaseous"""
#
#     ___ - name
#         s__. - ?
#
#     ___ isMatch stateInfo
#         r_ stateInfo >_ 100
#
#     ___ behavior context
#         print("I have a warm personality and my current temperature" ?.._gSI..
#               "℃, flying to the sky is my lifelong dream, here you will not see my existence, I will reach the realm of selflessness ...")
#
#
# # Test
# ########################################################################################################################
# ___ State
#     # water _ Water(LiquidState("液态"))
#     water _ Wa..
#     ?.b..
#     ?.sT.. -4
#     ?.b..
#     ?.riseTemperature(18)
#     ?.behavior()
#     ?.riseTemperature(110)
#     ?.behavior()
#
#
# State()
#
#
# # t1 _ State("State1")
# # t2 _ State("State2")
# # t3 _ SolidState("State3")
# # t4 _ SolidState("State4")
# # print(t1.getName(), t2.getName(), t3.getName(), t4.getName())
# # print(id(t1), id(t2), id(t3), id(t4))
# # print(t1 == t2)
# # print(t3 == t4)
#
#
