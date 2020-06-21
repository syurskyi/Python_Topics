# #
# # Custom JSON Encoding using JSONEncoder
# # In the previous video, we saw how we were able to provide custom encodings using the default argument of
# # the dump/dumps function.
# # But how does Python know how to encode the "standard" types, such as str, int, float, list, dict, etc?
# # It uses a special class - JSONEncoder.
# # This class supports the following encodings (see Python docs:
# # https://docs.python.org/3/library/json.html#json.JSONEncoder)
# # Python	JSON
# # dict	object {...}
# # list, tuple	array [...]
# # str	string "..."
# # int, float	number
# # int or float Enums	number
# # bool	true or false
# # None	null
# # Anything beyond those Python types and we end up with a TypeError exception.
# # We can see how this class encodes objects by calling an instance of it directly:
#
# ______ j___
#
# default_encoder _ j___.J..E..
# print ?.en.. 1, 2, 3
# # '[1, 2, 3]'
# # ######################################################################################################################
#
# print('#' * 52 + '  And for non-supported objects:')
#
# # default_encoder.encode(1+1j) #  TypeError: Object of type 'complex' is not JSON serializable
# # TypeError: Object of type 'complex' is not JSON serializable
# # We can actually extend this JSONEncoder class and override the default method. We can then add in support for
# # whatever type we want to use, and pass any other types to the parent class to handle
# # (either serialize the data or raise a TypeError exception).
#
# print('#' * 52 + '  We can actually extend this `JSONEncoder` class and override the `default` method')
# print('#' * 52 + '  We can then add in support for whatever type we want to use, '
#                  '  and pass any other types to the parent class to handle '
#                  '  (either serialize the data or raise a `TypeError` exception). ')
#
# ______ j___
# f... d. ______ d..t__
#
#
# c_ CustomJSONEncoder j___.J..E..
#     ___ default ____ arg
#         __ isi.. ? d..t__
#             r_ ?.i..f..
#         ___
#             su__.de.. ?
#
#
# custom_encoder _ C..
# print(cu.... en.. T..
# print cu.... en.. d..t__.u..n..
# # true
# # '"2018-12-29T22:27:19.863377"'
# # ######################################################################################################################
#
# print('#' * 52 + '  And we can now use this custom encoder by specifying it when we use `dump`/`dumps`:')
#
# print j___.du.. di.. name_'test' ti.._d..t__.u.n. cl._Cu..
# # '{"name": "test", "time": "2018-12-29T22:27:20.135841"}'
# # ######################################################################################################################
#
# print('#' * 52 + '  One thing to note is that for both the `default` approach, '
#                  '  and the `cls` approach, our method / encoder will only be used for types that Python'
#                  '  cannot already serialize on its own (strings, integers, lists, etc).')
#
#
# ___ custom_encoder arg
#     print('Custom encoder called...')
#     __ isi.. ? str
#         r_ _*some string: ?
#
# # Here we want to "override" dumps default encoding behavior for strings:
# print j___.du.. 'name' 'Python' de.._cu...
# # '{"name": "Python"}'
# # ######################################################################################################################
#
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
#
# # As you can see, we cannot do that - because the argument is a "recognized" type (str), Python does not even call
# # our custom_encoder function.
# # And the same happens when we override the default method in our custom JSONEncoder class.
# # Let's look at the signature for dumps:
#
# # help(json.dumps)
# # ######################################################################################################################
#
# print('#' * 52 + '  ')
# print('#' * 52 + '  And lets see the signature for `JSONEncoder`:')
# print('#' * 52 + '  ')
#
# # help(json.JSONEncoder)
# # ######################################################################################################################
#
# # You'll notice that there are quite a few arguments for both, most of which are common to both. With the `dump`/`dumps`
# # method, there are quite a few things we can configure that control the json encoding - if we want to use those tweaks
# # in a consistent manner throughout our app, we need to remember to use them consistently every time we call the
# # `dump`/`dumps` function. Consider this example:
#
# d _
#     'a': float('inf'),
#     'b': [1, 2, 3]
#
#
# print ?
# # {'a': inf, 'b': [1, 2, 3]}
# # ######################################################################################################################
#
# print ty.. ? 'a'
# # float
# # ######################################################################################################################
#
# print('#' * 52 + '  As you can see, that float is a special type of float - it represents + infinity.')
#
# print j___.du.. ?
# # '{"a": Infinity, "b": [1, 2, 3]}'
# # ######################################################################################################################
#
# print('#' * 52 + '  Yes, it does - but notice the output, `Infinity`. ')
# print('#' * 52 + '  Technically this is not JSON...')
# print('#' * 52 + '  So, if we want to be strict about this, and ensure we are not trying to serialize'
#                  '  a value such as infinity, we would do this instead:')
#
# # json.dumps(d, allow_nan=False) #  ValueError: Out of range float values are not JSON compliant
# # ValueError: Out of range float values are not JSON compliant
# # And we get the desired result.
# # What about trying to encode an invalid key (f... JSON's perspective)::
#
# print('#' * 52 + '  What about trying to encode an invalid key (f... JSONs perspective)::')
#
# d = {10: "int", 10.5: "float", 1+1j: "complex"}
# print(d)
# # {10: 'int', 10.5: 'float', (1+1j): 'complex'}
# # ######################################################################################################################
#
# print('#' * 52 + '  These are all valid Python dictionary keys, but what happens with JSON encoding?')
# # json.dumps(d) # TypeError: keys must be a string
# # ######################################################################################################################
#
# # TypeError: keys must be a string
# # As you can see we get an exception. We may want to simply ignore that exception and not include
# # the offending key/value pair in our serialization:
#
# print('#' * 52 + '  As you can see we get an exception.')
# print('#' * 52 + '  We may want to simply ignore that exception and not include the offending'
#                  '  key/value pair in our serialization:')
#
# print j___.du.. ? sk..k.._T..
#
# print('#' * 52 + '  And now we no longer get an exception, and the complex key was simply skipped.')
# print('#' * 52 + '  We can even change how the serialization is rendered '
#                  '  (which of course means we may no longer have actual JSON):')
#
# d _
#     'name': 'Python',
#     'age': 27,
#     'created_by': 'Guido van Rossum',
#     'list': [1, 2, 3]
#
#
# print j___.du.. ?
# # '{"name": "Python", "age": 27, "created_by": "Guido van Rossum", "list": [1, 2, 3]}'
# # ######################################################################################################################
#
# print print j___.du.. ? in.._'---' se.._'' ' = '
# # {
# # ---"name" = "Python"
# # ---"age" = 27
# # ---"created_by" = "Guido van Rossum"
# # ---"list" = [
# # ------1
# # ------2
# # ------3
# # ---]
# # }
# # ######################################################################################################################
#
# print('#' * 52 + '  We can use this by the way, to create more compact JSON strings (uses less bytes):')
# print j___.du.. ?
# # {"name": "Python", "age": 27, "created_by": "Guido van Rossum", "list": [1, 2, 3]}
# # ######################################################################################################################
#
# print('#' * 52 + '  vs')
# print j___.du.. ? se.._',' ':'
# # {"name":"Python","age":27,"created_by":"Guido van Rossum","list":[1,2,3]}
# # ######################################################################################################################
#
# # As you can see, all the whitespace is eliminated. For transmitting large JSON objects, that can make
# # a (relatively small) difference in making the JSON more compact.
# # So, if we want to consistently use the same values for all those tweaks, we have to consistently remember to set
# # the arguments correctly in the dump/dumps functions.
# # Instead, we could create a custom JSONEncoder class that pre-sets all these things, and just use that encoder
# # - simpler than remembering all those arguments and their correct values:
# print('#' * 52 + '  So, if we want to consistently use the same values for all those tweaks, '
#                  '  we have to consistently remember to set the arguments correctly in the `dump`/`dumps` functions.')
# print('#' * 52 + '  Instead, we could create a custom JSONEncoder class that pre-sets all these things, '
#                  '  and just use that encoder - simpler than remembering all those arguments and their correct values:')
#
#
# c_ CustomEncoder j___.J..E..
#     ___ - $ $$
#         su__.- sk..k.._T..
#                          allow_nan_F..
#                          in.._'---'
#                          se..._ '', ' = '
#
#
#     ___ default ____ arg
#         __ isi.. ? d..t__
#             r_ ?.i..f..
#         ____
#             r_ su__ .de.. ?
#
# d =
#     'time': d..t__.u..n.
#     1+1j: "complex",
#     'name': 'Python'
#
#
# print j___.du.. ? cl._C...
# # {
# # ---"time" = "2018-12-29T22:27:26.689488"
# # ---"name" = "Python"
# # }
# # ######################################################################################################################
#
# print('#' * 52 + '  Another thing I want to point out is that with both these methods'
#                  '  we are not limited in what we emit as our JSON serialization.')
# print('#' * 52 + '  For example, for a `d..t__` object, we may want to emit not only the ISO formatted date,'
#                  '  but maybe some additional fields, all nested within a JSON object:')
#
#
# c_ CustomEncoder j___.J..E..
#     ___ default ____ a..
#         __ isi.. ? d..t__
#             obj _ di..
#                 datatype_"d..t__"
#                 is._?.i..f..
#                 da.._?.da.. .i..f..
#                 ti.._?.ti.. .i..f..
#                 y.._?.y...
#                 m.._?.m...
#                 d.._?.d..
#                 h.._?.h..
#                 mi.._?.m...
#                 se.._?.s..
#             )
#             r_ ?
#         ____
#             r_ su__ .de.. a_
# d _ {
#     'time': d..t__.u..n..
#     'message': 'Testing...'
# }
#
# print j___.du.. ? cl._Cu... in.._2
# # {
# #   "time": {
# #     "datatype": "d..t__",
# #     "iso": "2018-12-29T22:27:27.668208",
# #     "date": "2018-12-29",
# #     "time": "22:27:27.668208",
# #     "year": 2018,
# #     "month": 12,
# #     "day": 29,
# #     "hour": 22,
# #     "minutes": 27,
# #     "seconds": 27
# #   },
# #   "message": "Testing..."
# # }
# # ######################################################################################################################
