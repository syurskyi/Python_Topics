# # Example #1: Language Translator
# # Our client, a French-only speaking person, wishes to have a two-way conversation in French. He expects the other person to be able to speak French.
# # Our existing class, an English-only speaking person cannot speak French.
# # Our Adapter, is in the form of a translator who translates English responses to French so that our French-only speaking client can have his two-way conversation in French.
#
# # Existing Class: a.k.a. Adaptee: Incompatible interface # 1
# c_ EnglishSpeaker
#     ___ responseToGreeting
#         r_ "Hello to you too!"
#
#     ___ responseToFarewell
#         r_ "Goodbye my friend."
#
#
# # Adapter Class, which takes functionality provided by EnglishSpeaker, morphs it into functionality expected by the FrenchSpeaker.
# c_ Translator
#     '''Accespts an english speaker, translates his responses to French.'''
#     _englishSpeaker _ N...
#     _englishToFrenchPhrases _ {
#         "Hello to you too!": "Bonjour à vous aussi",
#         "Goodbye my friend.": "Au revoir mon ami"
#     }
#
#     ___ - englishSpeaker
#         _?  ?
#
#
# # Client: Incompatible interface # 2
# c_ FrenchSpeaker
#     '''Accepts an English-To-French Speaker as argument.'''
#     _englishToFrenchTranslator _ N..
#
#     ___ - englishToFrenchTranslator
#         _?  ?
#
#     ___ exchangeGreetings
#         print("Salut!")
#         print _eTFT__._eTFP__|
#             self._eTFT...._eS__.rTG..
#
#     ___ exchangeFarewell
#         print("Au revoir!")
#         print(_eTFT...._eTFP..|
#             self._eTFT...._eS___.rTF...
#
#
# # Create an English Speaking person
# englishSpeaker _ E...
#
# # Create a translator with popular english phrases
# englishToFrenchTranslator _ T.. eS...
#
# # The French Speaking Person can now get responses in French
# frenchSpeaker _ FS.. eTFT..
#
# # Two-way conversation in French
# ?.eG...
# ?.eF..
#
# # OUTPUT
# # Salut!
# # Bonjour à vous aussi
# # Au revoir!
# # Au revoir mon ami