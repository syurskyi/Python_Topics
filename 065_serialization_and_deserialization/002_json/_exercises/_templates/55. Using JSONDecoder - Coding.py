# # Using JSONDecoder
# # Just like we can use a subclass of JSONEncoder to customize our json encodings, we can use a subclass of
# # the default JSONDecoder class to customize decoding our json strings.
# # It works quite differently from the JSONEncoder subclassing though.
# # When we subclass JSONEncoder we override the default method which then allows us to intercept encoding of specific
# # types of objects, and delegate back to the parent class what we don't want to handle specifically.
# # With the JSONDecoder class we override the decode function which passes us the entire JSON as a string and we have
# # to return whatever Python object we want. There's no delegating anything back to the parent class unless we want
# # to completely skip customizing the output.
# # Let's first see how the functions work:
#
# ______ j___
#
# j _ '''
#     {
#         "a": 100,
#         "b": [1, 2, 3],
#         "c": "python",
#         "d": {
#             "e": 4,
#             "f": 5.5
#         }
#     }
# '''
#
# c_ CustomDecoder j___.J..D..
#     ___ decode ____ ar.
#         print("decode:", ty.. ar. ar.
#         r_ "a simple string object"
#
# print j___.lo.. ? cl._C..
#
# # As you can see, whatever we return from the decode method is the result of calling loads.
# # So, we might want to intercept certain JSON strings, handling them in some custom way, and delegate back to
# # the parent class if it's not a string we want to handle ourselves - but it's all or nothing:
# # Let's see an example of how we might want to use this:
#
# print('#' * 52 + '  As you can see, whatever we return from the `decode` method is the **result** of calling `loads`.')
# print('#' * 52 + '  So, we might want to intercept certain JSON strings, handling them in some custom way, '
#                  '  and delegate back to the parent class if its not a string we want to handle ourselves -'
#                  '  but its all or nothing:')
#
# c_ Point
#     ___ __i___ ___ x y
#         ____.x _ x
#         ____.y _ y
#
#     ___ __re__ ____
#         r_ _*P.. x_|____.x y_ ____.y *
#
# j_points _ '''
# {
#     "points": [
#         [10, 20],
#         [-1, -2],
#         [0.5, 0.5]
#     ]
# }
# '''
#
# j_other _ '''
# {
#     "a": 1,
#     "b": 2
# }
# '''
#
# c_ CustomDecoder j___.J..D..
#     ___ decode ____ ar.
#         i_ 'points' i_ ar.
#             obj _ j___.lo.. ar.
#             r_ "parsing object for points"
#         e___
#             r_ su__.de.. ar.
#
# print j___.lo.. j_po.. cl._C..De..
# print j___.lo.. j_o.. cl._C..De..
# # {'a': 1, 'b': 2}
# # ######################################################################################################################
#
# print('#' * 52 + '  So, lets implement the custom decoder now, assuming that `points` will be a top level node'
#                  '  in the JSON object:')
#
#
# c_ CustomDecoder j___.J..D..
#     ___ decode ____  ar.
#         obj _ j___.lo.. ar.
#         i_ 'points' i_ obj  # top level
#             ob. 'points'| _ P... x y
#                              ___ x  y i_ ob. |'points'
#         r_ ob.
#
#
# print j___.lo.. j_po.. cl._Cu..
# # {'points': [Point(x=10, y=20), Point(x=-1, y=-2), Point(x=0.5, y=0.5)]}
# # ######################################################################################################################
#
# print j___.lo.. j_ot.. cl._Cu..
# # {'a': 1, 'b': 2}
# # ######################################################################################################################
#
# # Of course, we can be more fancy and maybe handle points by specifying the data type in the JSON object
# # (and again, this is just how we, the developer, decide to make that specification).
# # Here I am going to specify that a Point object in the JSON document should be specified using this format:
# # {"_type": "point", "x": x-coord, "y": y-coord}
# # So, when we parse the JSON string we are going to look for such a structure, and do the appropriate type conversion
# # if needed. Of course, we'll have to look recursively in the JSON for this structure. We'll follow the same approach
# # as before, first deserializing to a "generic" Python dict, then replacing any Point structure as we find them.
# # To avoid having to iterate through the deserialized JSON object when we don't have that structure there in the first
# # place, I'm going to look for "_type": "point" in the string. Technically we also need to look for "_type":"point"
# # since both, from a JSON object perspective, are the same thing. In fact any amount of whitespace surrounding the :
# # is acceptable. It would be possible but result in very unwieldy and concoluted code if we were to use an ordinary
# # string search, so I'm going to use a regular expression instead (if you need help getting started with regular
# # expressions, I highly recommend using this site:
#
#
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
#
# ______ r_
# pattern _ r'"_type"\s*:\s*"point"'
#
# # In this pattern, \s simply means a whitespace character, and the * right after it means zero or more times.
# # Also note that we prefix that string with r to tell Python not to interpret the \ as anything special -
# # otherwise Python will try to escape that, or interpet it, when conbined with another character, as an escape sequence.
# # Let's see a quick example of this first:
#
# print('word1\tword2')
# # word1	word2
# # ######################################################################################################################
#
# print(r'word1\tword2')
# # word1\tword2
# # ######################################################################################################################
#
# # Notice the difference? Since we use the \ character a lot in regular expressions, we should always use this r prefix
# # which indicates a raw string, and Python will not try to recognize escape sequences in our pattern.
# # So, now let's continue testing out our regular expression pattern. We'll compile it so we can re-use it, but you
# # dont have to.
# # Once we have it compiled, we can use the search method that will find the first occurrence of the pattern in our
# # search string, or return None if it was not found:
#
# regexp _ r_.co.. pa..
# print re__.se.. '"a": 1'
# # None
# # ######################################################################################################################
#
# print r..e...se.. '"_type": "point"'
# # <_sre.SRE_Match object; span=(0, 16), match='"_type": "point"'>
# # ######################################################################################################################
#
# print r__e__.se.. '"_type"   : "point"'
# # <_sre.SRE_Match object; span=(0, 19), match='"_type"   : "point"'>
# # ######################################################################################################################
#
# print('#' * 52 + '  Alternatively, if we dont want to compile it'
#                  ' (if we only use it once, there is no real need to do so), we can do a search this way:')
#
# print r_.se.. pa.. '"_type"  :  "point"'
# # <_sre.SRE_Match object; span=(0, 19), match='"_type"  :  "point"'>
# # ######################################################################################################################
#
# print('#' * 52 + '  OK, now that we have a working regular expression pattern we can implement our custom j___ decoder.')
#
#
# c_ CustomDecoder j___.J..D..
#     ___ decode ____ ar.
#         obj _ j___.lo.. ar.
#         pattern _ r'"_type"\s*:\s*"point"'
#         i_ r_.se.. p... ar.
#             # we have at least one `Point'
#             obj _ ____.make_pts ob.
#         r_ ob.
#
#     ___ make_pts ____ ob.
#         # recursive function to find and replace points
#         # received object could be a dictionary, a list, or a simple type
#         i_ isi.. ob. di..
#             # first see if this dictionary is a point itself
#             i_ '_type' i_ ob. an. ob. '_type'| __ 'point'
#                 # could have used: if obj.get('_type', None) == 'point'
#                 obj _ P... ob.|'x' obj|'y'
#             e___
#                 # root object is not a point
#                 # but it could contain a sub-object which itself
#                 # is or contains a Point object
#                 ___ key value i_ ob_.it..
#                     obj key| _ ____.make_pts va..
#         e___ isi.. ob. li..
#             ___ index item i_ en.. ob.
#                 ob_ in..| _ ____.make_pts it..
#         r___ ob.
#
#
# j _ '''
# {
#     "a": 100,
#     "b": 0.5,
#     "rectangle": {
#         "corners": {
#             "b_left": {"_type": "point", "x": -1, "y": -1},
#             "b_right": {"_type": "point", "x": 1, "y": -1},
#             "t_left": {"_type": "point", "x": -1, "y": 1},
#             "t_right": {"_type": "point", "x": 1, "y": 1}
#         },
#         "rotate": {"_type" : "point", "x": 0, "y": 0},
#         "interior_pts": [
#             {"_type": "point", "x": 0, "y": 0},
#             {"_type": "point", "x": 0.5, "y": 0.5}
#         ]
#     }
# }
# '''
#
# print j___.lo.. ?
# # {'a': 100,
# #  'b': 0.5,
# #  'rectangle': {'corners': {'b_left': {'_type': 'point', 'x': -1, 'y': -1},
# #    'b_right': {'_type': 'point', 'x': 1, 'y': -1},
# #    't_left': {'_type': 'point', 'x': -1, 'y': 1},
# #    't_right': {'_type': 'point', 'x': 1, 'y': 1}},
# #   'rotate': {'_type': 'point', 'x': 0, 'y': 0},
# #   'interior_pts': [{'_type': 'point', 'x': 0, 'y': 0},
# #    {'_type': 'point', 'x': 0.5, 'y': 0.5}]}}
# # ######################################################################################################################
#
# f___ pp.. _______ pp..
# pprint j___.lo.. ? cl._Cu..
# # {'a': 100,
# #  'b': 0.5,
# #  'rectangle': {'corners': {'b_left': Point(x=-1, y=-1),
# #                            'b_right': Point(x=1, y=-1),
# #                            't_left': Point(x=-1, y=1),
# #                            't_right': Point(x=1, y=1)},
# #                'interior_pts': [Point(x=0, y=0), Point(x=0.5, y=0.5)],
# #                'rotate': Point(x=0, y=0)}}
# # ######################################################################################################################
#
# print('#' * 52 + '  The `JSONDecoder` class also has arguments such as `parse_int`, '
#                  ' `parse_float`, etc we saw in the previous lecture.')
# print('#' * 52 + '  We can use those to define a custom `JSONEncoder` class if we wanted to - lets say we want to use'
#                  ' `Decimals` instead of floats - just like before,')
# print('#' * 52 + '   but instead of specifying this each and every time we calls `loads`, '
#                  ' we can bundle this up into a custom decoder instead:')
#
# f___ de... _____ D..
# CustomDecoder _ j___.J..D.. parse_float=D..
#
# d _ Cu___.de.. ?
# pprint(d)
# # {'a': 100,
# #  'b': Decimal('0.5'),
# #  'rectangle': {'corners': {'b_left': {'_type': 'point', 'x': -1, 'y': -1},
# #                            'b_right': {'_type': 'point', 'x': 1, 'y': -1},
# #                            't_left': {'_type': 'point', 'x': -1, 'y': 1},
# #                            't_right': {'_type': 'point', 'x': 1, 'y': 1}},
# #                'interior_pts': [{'_type': 'point', 'x': 0, 'y': 0},
# #                                 {'_type': 'point',
# #                                  'x': Decimal('0.5'),
# #                                  'y': Decimal('0.5')}],
# #                'rotate': {'_type': 'point', 'x': 0, 'y': 0}}}
# # ######################################################################################################################
#
# print('#' * 52 + '  Of course, we can combine this with our custom decoder too:')
#
#
# c_ CustomDecoder(j___.J..D..):
#     base_decoder _ j___.J..D.. parse_float_D...
#
#     ___ decode ____  ar.
#         obj _ ____.ba.._de...de.. ar.
#         pattern _ r'"_type"\s*:\s*"point"'
#         i_ r_.se.. pa.. ar.
#             # we have at least one `Point'
#             obj _ ____.m.._p.. ob.
#         r_ ?
#
#     ___ make_pts ____ obj
#         # recursive function to find and replace points
#         # received object could be a dictionary, a list, or a simple type
#         i_ isi.. ob. di..
#             # first see if this dictionary is a point itself
#             i_ '_type' i_ ob. an. ob.|'_type' __ 'point':
#                 obj _ P... ob.|'x' obj|'y'
#             e___
#                 # root object is not a point
#                 # but it could contain a sub-object which itself
#                 # is or contains a Point object nested at some level
#                 # maybe another dictionary, or a list
#                 ____ key value i_ ob_.it..
#                     ob. |k.. _ ____.m.._p.va..
#         e___ isi.. ob. li..
#             # received a list - need to run each item through make_pts
#             ___ index, item i_ en... ob.
#                 ob. i_...| _ ____.ma.._p.. it..
#         r_ o..
#
#
# pprint j___.lo.. ? cls_Cu__
# # {.
# #  'b': Decimal('0.5'),
# #  'rectangle': {'corners': {'b_left': Point(x=-1, y=-1),
# #    'b_right': Point(x=1, y=-1),
# #    't_left': Point(x=-1, y=1),
# #    't_right': Point(x=1, y=1)},
# #   'rotate': Point(x=0, y=0),
# #   'interior_pts': [Point(x=0, y=0), Point(x=0.5, y=0.5)]}}
# # ######################################################################################################################
#
# print('#' * 52 + '  Its not evident that our `Point(x=0.5, y=0.5)` actually contains `Decimal` objects - '
#                  '  that is really just the string representation - so lets just make sure they are indeed '
#                  ' `Decimal` objects:')
#
# result _ j___.lo.. ? cl._Cu..
# pt _ re... 'rectangle' 'interior_pts' 1
# print ty.. p_.x ty.. p_.y
# # <class 'decimal.Decimal'> <class 'decimal.Decimal'>
# # ######################################################################################################################
#
# # As you can see, decoding JSON into custom objects is not exactly easy - the basic reason being that JSON does not
# # support anything other than simple data types such as integers, floats, strings, booleans, constants and objects and lists.
# # The rest is up to us.
# # This is one of the reasons there are quite a few 3rd party libraries that allow us to serialize and deserialize
# # JSON objects that follow a certain schema.
# # I'll discuss some of those in upcoming lectures.
