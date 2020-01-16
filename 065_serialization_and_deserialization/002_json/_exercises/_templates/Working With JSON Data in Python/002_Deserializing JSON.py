# # -*- coding: utf-8 -*-
#
# # Deserializing JSON
# # Great, looks like you’ve captured yourself some wild JSON! Now it’s time to whip it into shape. In the json library,
# # you’ll find load() and loads() for turning JSON encoded data into Python objects.
# # Just like serialization, there is a simple conversion table for deserialization, though you can probably guess what it
# # looks like already.
# #
# # JSON	Python
# # object	dict
# # array	list
# # string	str
# # number (int)	int
# # number (real)	float
# # true	True
# # false	False
# # null	None
#
# # Technically, this conversion isn’t a perfect inverse to the serialization table. That basically means that if you
# # encode an object now and then decode it again later, you may not get exactly the same object back. I imagine it’s
# # a bit like teleportation: break my molecules down over here and put them back together over there. Am I still
# # the same person?
# # In reality, it’s probably more like getting one friend to translate something into Japanese and another friend to
# # translate it back into English. Regardless, the simplest example would be encoding a tuple and getting back a list
# # after decoding, like so:
# #
# ____ ____
# blackjack_hand = (8, "Q")
# encoded_hand = ____.d.. ?
# decoded_hand = ____.l.. ?
#
# print(b.. __ d..
# # False
# print(ty.. b..
# # <class 'tuple'>
# print(ty.. d..
# # <class 'list'>
# print(b.. __ tu.. d..
# # True
#
# # A Simple Deserialization Example
# # This time, imagine you’ve got some data stored on disk that you’d like to manipulate in memory. You’ll still use
# # the context manager, but this time you’ll open up the existing data_file.json in read mode.
# #
# w___ o.. data_file.json _ __ read_file
#     data _ ____.l.. ?
# # Things are pretty straightforward here, but keep in mind that the result of this method could return any of
# # the allowed data types from the conversion table. This is only important if you’re loading in data you haven’t
# # seen before. In most cases, the root object will be a dict or a list.
# # If you’ve pulled JSON data in from another program or have otherwise obtained a string of JSON formatted data
# # in Python, you can easily deserialize that with loads(), which naturally loads from a string:
#
# json_string = """
# {
#     "researcher": {
#         "name": "Ford Prefect",
#         "species": "Betelgeusian",
#         "relatives": [
#             {
#                 "name": "Zaphod Beeblebrox",
#                 "species": "Betelgeusian"
#             }
#         ]
#     }
# }
# """
# data _ ____.l.. ?
# # Voilà! You’ve tamed the wild JSON, and now it’s under your control. But what you do with that power is up to you.
# # You could feed it, nurture it, and even teach it tricks. It’s not that I don’t trust you…but keep it on a leash, okay?
