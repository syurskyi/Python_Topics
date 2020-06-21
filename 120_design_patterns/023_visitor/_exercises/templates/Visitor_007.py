# # Version 2.0
# #=======================================================================================================================
# # Code framework
# #==============================
# ____ a _______ A.. a...
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ DataNode m..
#     """Data Structure Class"""
#
#     ___ accept  visitor
#         """Accept visitors"""
#         ?.v... ?
#
# c_ Visitor m..
#     """Visitors"""
#
#     ??
#     ___ visit  data
#         """Access operations on data objects"""
#         pass
#
#
# c_ ObjectStructure:
#     """The management class of the data structure is also a container for the data object, which can traverse all the elements in the container"""
#
#     ___ -
#         __datas _    # list
#
#     ___ add  dataElement
#         __?.ap.. ?
#
#     ___ action  visitor
#         """Operations for data access"""
#         ___ data __ __?
#             ?.ac.. ?
#
#
# # Framework-based implementation
# #==============================
# c_ DesignPatternBook D..
#     """Interpreting Design Patterns ____ a Life Perspective"""
#
#     ___ getName
#         r_ "Interpreting design patterns ____ a life perspective》"
#
#
# c_ Engineer V..
#     """engineer"""
#
#     ___ visit  book
#         print("Technical dog's feeling after reading the book @: Can grasp the core idea of the model, explain it in a simple way, very insightful!"  ?.gN..
#
#
# c_ ProductManager V..
#     """Product manager"""
#
#     ___ visit  book
#         print("Product manager's feelings after reading the book @: The picture is very interesting, and the article is very layered!"  ?.gN..
#
#
# c_ OtherFriend V..
#     """Friends outside the IT circle"""
#
#     ___ visit  book
#         print("Friends outside the IT circle feel after reading the book @: the content of technology is aggressive, but the story is very exciting, like watching a novel or a story collection!"
#                ?.gN..
#
#
# # Actual combat
# # =======================================================================================================================
# c_ Animal D..
#     """Animal"""
#
#     ___ -  name isMale age weight
#         __?  ?
#         __?  ?
#         __?  ?
#         __?  ?
#
#     ___ getName
#         r_ __?
#
#     ___ isMale
#         r_ __?
#
#     ___ getAge
#         r_ __?
#
#     ___ getWeight
#         r_ __?
#
# c_ Cat A..
#     """Cat"""
#
#     ___ - name isMale age weight
#         s___ . - ?  ?  ?  ?
#
#     ___ speak
#         print("miao")
#
#
# c_ Dog A..
#     """dog"""
#
#     ___  -    name isMale age weight
#         s___ . - ?  ?  ?  ?
#
#     ___ speak
#         print("wang")
#
#
# c_ GenderCounter V..
#     """Sex statistics"""
#
#     ___  -
#         __maleCat _ 0
#         __femaleCat _ 0
#         __maleDog _ 0
#         __femalDog _ 0
#
#     ___ visit  data
#         __ isi.. ? C..
#             __ ?.i..(
#                 __m... +_ 1
#             ____
#                 __f.. +_ 1
#         ____ isi.. ? D..
#             __ ?.i...(
#                 __mD.. +_ 1
#             ____
#                 __f... +_ 1
#         ____
#             print("Not support this type")
#
#     ___ getInfo
#         print("@ males, @ females, @ males, @ females."
#                (__m.. __f.. __m.. __f..
#
#
# c_ WeightCounter V..
#     """Statistics of weight"""
#
#     ___  - ?
#         __catNum _ 0
#         __catWeight _ 0
#         __dogNum _ 0
#         __dogWeight  _ 0
#
#     ___ visit  data
#         __ isi.. ? C..
#             __cN.. +_1
#             __cW.. +_ ?.gW..
#         ____ isi.. ? D..
#             __dN.. +_ 1
#             __dW.. +_ ?.gW..
#         ____
#             print("Not support this type")
#
#     ___ getInfo ?
#         print("The average weight of cats is: 0.2fkg, the average weight of dogs is: 0.2fkg "
#               ||__cW.. / __cN..| |__dW.. / __dN..
#
#
# c_ AgeCounter V..
#     """Age statistics"""
#
#     ___  - ?
#         __catMaxAge _ 0
#         __dogMaxAge _ 0
#
#     ___ visit  data
#         __ isi.. ? C..
#             __ __cMA.. < ?.gA..|
#                 __cMA.. _ ?.gA..
#         ____ isi.. ? D..
#             __ __dM.. < ?.gA..|
#                 __dMA.. _ ?.gA..
#         ____
#             print("Not support this type")
#
#     ___ getInfo
#         print("The maximum age of a cat is: @, and the maximum age of a dog is: @"  (__c.. __d..
#
# # Test
# #=======================================================================================================================
#
# ___ tBook(
#     book _ DPB..
#     fans _ E.. P.. O...
#     ___ fan __ ?
#         ?.r.. ?
#
# ___ VisitBook(
#     book _ DPB..
#     objMgr _ O..
#     ?.a.. ?
#     ?.ac.. E..
#     ?.ac.. P..
#     ?.ac.. O..
#
#
# ___ Animal|
#     animals _ O..
#     ?.a.. C.. *_1 T.. 1 5
#     ?.a.. C.. *_2 F.. 0.5 3
#     ?.a.. C.. *_3 F.. 1.2 4.2
#     ?.a.. D.. *_1 T.. 0.5 8
#     ?.a.. D.. *_2 T.. 3 52
#     ?.a.. D.. *_3 F.. 1 21
#     ?.a.. D.. *_4 F.. 2 25
#     genderCounter _ GC..
#     a__.ac.. ?
#     ?.gI..
#     print()
#
#     weightCounter _ W...
#     a___.ac.. ?
#     ?.gI..
#     print()
#
#     ageCounter _ AC..
#     a___.a.. ?
#     ?.gI..
#
#
# # testBook()
# # testVisitBook()
# testAnimal()