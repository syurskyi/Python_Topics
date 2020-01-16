# # Custom JSON Decoding
# # So far we have looked at how to encode (serialize) Python objects to JSON, using the standard as well as custom
# # object serializers.
# # Now we need to turn our attention to teh reverse process - deserializing (decoding) JSON data.
# # Once again, the standard simple types such as strings, numbers (ints and floats), arrays, and objects with key/value
# # pairs. JSON does not differentiate between mutable and immutable lists - so everything that is an array ([...])
# # in JSON will get decoded into a list object.
# # Let's see a quick example of how to do this:
#
# print('#' * 52 + '  Once again, the standard simple types such as strings, numbers (ints and floats), '
#                  '  arrays, and objects with key/value pairs. ')
# print('#' * 52 + '  JSON does not differentiate between mutable and immutable lists - '
#                  '  so everything that is an array ([...]) in JSON will get decoded into a list object.')
#
# j = '''
#     {
#         "name": "Python",
#         "age": 27,
#         "versions": ["2.x", "3.x"]
#     }
# '''
#
# ______ j___
# print j___.l... ?
# # {'name': 'Python', 'age': 27, 'versions': ['2.x', '3.x']}
# # ######################################################################################################################
#
# print('#' * 52 + '  But what about other data types, such as a date for example. How can we handle that?')
#
# p _ '''
#     {
#         "time": "2018-10-21T09:14:00",
#         "message": "created this json string"
#     }
# '''
# print j___.l... ?
# #
# # {'time': '2018-10-21T09:14:00', 'message': 'created this json string'}
# # ######################################################################################################################
#
# # The deserialization worked just fine, but you'll notice that the dictionary entry for time contains a string, not a date.
# # This is not a trivial problem, and many 3rd party libraries have been written to deserialize specialized JSON
# # structures into custom Python objects. It basically boils down to having a specific structure (schema) in the
# # JSON and manually loading up some custom (or standard) Python object by specifically looking for certain elements
# # and objects in the JSON object. Remember that JSON only supports a few basic types, so anything beyond that is really
# # a custom interpretation of the data in the JSON object.
# # For example, suppose we have a JSON object where any object that contains the key/value pair "objecttype": "datetime"
# # is guaranteed to contain another key called "value" containing a date time in the format %Y-%m-%dT%H:%M:%S.
# # We could easily do the following:
# print('#' * 52 + '  For example, suppose we have a JSON object where any object that contains'
#                  '  the key/value pair `"objecttype": "datetime"` is guaranteed to contain another key'
#                  '  called `"value"` containing a date time in the format %Y-%m-%dT%H:%M:%S. ')
#
# p _ '''
#     {
#         "time": {
#             "objecttype": "datetime",
#             "value": "2018-10-21T09:14:15"
#             },
#         "message": "created this json string"
#     }
# '''
#
# d _ j___.l... ?
# print(d)
# # {'time': {'objecttype': 'datetime', 'value': '2018-10-21T09:14:15'},
# #  'message': 'created this json string'}
# # ######################################################################################################################
#
# print('#' * 52 + '  We could now run through our dictionary (top level only, we will come back to that), '
#                  '  and convert any datetime structures (schema) into actual datetime objects:')
#
# f... d..t.. ______ d..t..
#
# ___ key value i_ d.it..
#     i_  isi... v.. di.. an.
#         'objecttype' i_ va.. an.
#         va.. 'objecttype'| __ 'datetime'
#         d key| _ da__ti__.st..ti. va.. |'value' %Y-%m-%dT%H:%M:%S
#
# print(d)
# # {'time': datetime.datetime(2018, 10, 21, 9, 14, 15),
# #  'message': 'created this json string'}
# # ######################################################################################################################
#
# # As you can see that worked just fine. We can do this with other "custom" JSON schemas as well.
# # Let's say we have a JSON schema that will encode fractions using a fraction type indicator and associated keys
# # numerator and denominator with integer values, such as:
# #
# # "pieSlice": {
# #     "objecttype": "fraction",
# #     "numerator": 1,
# #     "denominator": 3
# #     }
# # We can deal with this in the same way as before:
#
# print('#' * 52 + '  We can do this with other "custom" JSON schemas as well.')
# print('#' * 52 + '  Lets say we have a JSON schema that will encode fractions using a `fraction` type indicator'
#                  '  and associated keys `numerator` and `denominator` with integer values,')
#
# j _ '''
#     {
#         "cake": "yummy chocolate cake",
#         "myShare": {
#             "objecttype": "fraction",
#             "numerator": 1,
#             "denominator": 8
#         }
#     }
# '''
#
# d _ j___.l... ?
# print(d)
# # {'cake': 'yummy chocolate cake',
# #  'myShare': {'objecttype': 'fraction', 'numerator': 1, 'denominator': 8}}
# # ######################################################################################################################
#
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
#
# f... fr.. ______ F...
#
# ___ key value i_ d.it..
#     i_ (isi... va.. di.. an.
#         'objecttype' i_ va.. an.
#         va.. 'objecttype'| __ 'fraction'
#         numerator _ va.. 'numerator'|
#         denominator _ va.. 'denominator'|
#         d|key _ F..  n.. d...
#
# print(d)
# # {'cake': 'yummy chocolate cake', 'myShare': Fraction(1, 8)}
# # ######################################################################################################################
#
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
#
# # We can extend this to even custom objects as long as they follow a specific structure (schema).
# # We could put all this code into a function, even one that can handle multiple types and clean it up quite a bit. But...
# # A few things:
# # It's a real pain having to go through the dictionary after the fact and convert the objects
# # Our conversion code only considered top-level objects - what if they are nested deeper in the JSON object -
# # we would need to deal with that possibility.
# # There has to be a better way!
# # And indeed, there is - but all in all it's still relatively clunky in some respects. Let's look at the
# # `load`/`loads` functions first. They have an optional argument named `object_hook` that can reference a callable.
# # This is very similar to the `default` argument we saw in the `dump`/`dumps` functions - but works for decoding
# # instead of encoding. That callable, if specified, will be called for every value in the JSON object that is itself
# # an object (including the root object). That dictionary will then be replaced by whatever that decoder returns.
# # Let's first write a dummy decoder, just to see how and when it gets called:
#
#
# ___ custom_decoder arg
#     print 'decoding: ' a..
#     r_ a..
#
#
# j _ '''
#     {
#         "a": 1,
#         "b": 2,
#         "c": {
#             "c.1": 1,
#             "c.2": 2,
#             "c.3": {
#                 "c.3.1": 1,
#                 "c.3.2": 2
#             }
#         }
#     }
# '''
#
# d _ j___.l... ? o.._h.._cu...
# # decoding:  {'c.3.1': 1, 'c.3.2': 2}
# # decoding:  {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}
# # decoding:  {'a': 1, 'b': 2, 'c': {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}}
# # ######################################################################################################################
#
# # As you can see it called our decoder three times, the value for the key c.3, the value for the key c and the root
# # object itself.
# # Now, let's write a decoder that will handle the datetime JSON we worked with earlier:
# print('#' * 52 + '  As you can see it called our decoder three times, '
#                  '  the value for the key `c.3`, the value for the key `c` and the root object itself.')
#
# j _ '''
#     {
#         "time": {
#             "objecttype": "datetime",
#             "value": "2018-10-21T09:14:15"
#             },
#         "message": "created this json string"
#     }
# '''
#
#
# ___ custom_decoder arg
#     i_ 'objecttype' i_ ar. an. ar.|'objecttype' __ 'datetime'
#         r_ d..ti__.st..t. ar. 'value'| '%Y-%m-%dT%H:%M:%S'
#     e___
#         r___ a..  # important, otherwise we lose anything that's not a date!
#
#
# print('#' * 52 + '  Lets just see how it works as a plain function first:')
#
# print cu... di.. ob..ty.._'datetime' va.._2018-10-21T09:14:15
# # datetime.datetime(2018, 10, 21, 9, 14, 15)
# # ######################################################################################################################
#
# print cu... di.. a_1
# # {'a': 1}
# # ######################################################################################################################
#
# d _ j___.l... ? o.._h._cu.
# print(d)
# # {'time': datetime.datetime(2018, 10, 21, 9, 14, 15),
# #  'message': 'created this json string'}
# # ######################################################################################################################
#
# print('#' * 52 + '  The nice thing about this approach, is our code is simpler, and this works for nested items too:')
#
# j = '''
#     {
#         "times": {
#             "created": {
#                 "objecttype": "datetime",
#                 "value": "2018-10-21T09:14:15"
#                 },
#             "updated": {
#                 "objecttype": "datetime",
#                 "value": "2018-10-22T10:00:05"
#                 }
#             },
#         "message": "log message here..."
#     }
# '''
#
# d _ j___.l... ? o...._cu..
#
# print(d)
# # {'times': {'created': datetime.datetime(2018, 10, 21, 9, 14, 15),
# #   'updated': datetime.datetime(2018, 10, 22, 10, 0, 5)},
# #  'message': 'log message here...'}
# # ######################################################################################################################
#
# # We can also extend this custom decoder to include other structures (schemas). Let's add in our fraction decoder:
#
# print('#' * 52 + '  ')
# print()
# print()
# print('#' * 52 + '  We can also extend this custom decoder to include other structures (schemas).')
#
#
# ___ custom_decoder arg
#     ret_value _ ar.
#     i_ 'objecttype' i_ ar.
#         i_ ar. 'objecttype'| __ datetime
#             ret_value _ da..ti__.s..ti.. ar. 'value'| %Y-%m-%dT%H:%M:%S
#         e___ ar. 'objecttype'| __ 'fraction'
#             ret_value _ F... a.. 'numerator'| ar. 'denominator'|
#     r_ r..
#
#
# j _ '''
#     {
#         "cake": "yummy chocolate cake",
#         "myShare": {
#             "objecttype": "fraction",
#             "numerator": 1,
#             "denominator": 8
#         },
#         "eaten": {
#             "at": {
#                 "objecttype": "datetime",
#                 "value": "2018-10-21T21:30:00"
#                 },
#             "time_taken": "30 seconds"
#         }
#     }
# '''
#
# d _ j___.l... ? o.._h..=cu...
# print(d)
# # {'cake': 'yummy chocolate cake', 'myShare': Fraction(1, 8), 'eaten': {'at': datetime.datetime(2018, 10, 21, 21, 30), 'time_taken': '30 seconds'}}
# # ######################################################################################################################
#
# # We can't really use a generic single dispatch approach we took with the encoder though - the decoder always receives
# # a dictionary, so we can't build it that way.
# # We still have the issue of custom objects and classes - how do we handle those?
# # Well, in pretty much the same way as before - the content of the JSON has to indicate that the object is of
# # a certain "type", and we can then decode it ourselves.
# # Let's see a simple example:
#
# print('#' * 52 + '  ')
# print()
# print()
# print('#' * 52 + '  We cant really use a generic single dispatch approach we took with the encoder though -'
#                  '  the decoder always receives a dictionary, so we cant build it that way.')
# print('#' * 52 + '  We still have the issue of custom objects and classes - how do we handle those?')
# print('#' * 52 + '  Well, in pretty much the same way as before - '
#                  '  the content of the JSON has to indicate that the object is of a certain "type", '
#                  '  and we can then decode it ourselves.')
#
#
# c_ Person
#     ___ __i__ ____ name ssn
#         ____.n.. _ n..
#         ____.s.. _ s..
#
#     ___ __re__ ____
#         r_ _*P.. n.._|____.name s.._|____.ssn
#
#
# j _ '''
#     {
#         "accountHolder": {
#             "objecttype": "person",
#             "name": "Eric Idle",
#             "ssn": 100
#         },
#         "created": {
#             "objecttype": "datetime",
#             "value": "2018-10-21T03:00:00"
#         }
#     }
# '''
#
#
# ___ custom_decoder arg)
#     ret_value _ ar.
#     i_ 'objecttype' i_ arg
#         i_ ar. 'objecttype'| __ 'datetime
#             ret_value _ da..ti__.st..ti.. ar. 'value'| %Y-%m-%dT%H:%M:%S
#         e___ ar. 'objecttype'| __ 'fraction'
#             ret_value _ F... ar. |'numerator' arg|'denominator'
#         e__ ar. 'objecttype'| __ 'person'
#             ret_value _ P.. ar. 'name'| ar. 'ssn'
#     r_ r..
#
#
# d _ j___.l... ? o.._h.._cu..
# print(d)
# # {'accountHolder': Person(name=Eric Idle, ssn=100),
# #  'created': datetime.datetime(2018, 10, 21, 3, 0)}
# # ######################################################################################################################
#
# print('#' * 52 + '  We could also provide our custom JSON encoder in the person class to serialize '
#                  '  that class in the way we expect when deserializing, as we saw in an earlier video:')
#
#
# c_ Person
#     ___ __init__ ____ name ssn
#         ____.n.. _ n..
#         ____.s.. _ s..
#
#     ___ __r__ ____
#         r_ _*P.. n.._|____.n.. s.._|____.ssn
#
#     ___ toJSON ____
#         r_ di.. ob..t.._'person' n.._____.n.. s.._____.s..
#
# # We can then encode using the techniques we have seen before, and decode using the technique we learned in this video.
# # There are also a few customized hooks for integers, floats and certain special strings (-Infinity, Infinity and NaN).
# # For example, we may want to encode floats using a Decimal instead of the standard float.
# # We could do this by using the parse_float argument as follows:
#
# f... d... ______ D...
#
# ___ make_decimal arg
#     print 'Received:' ty.. ar. ar.
#     r_ D... ar.
#
#
# j = '''
#     {
#         "a": 100,
#         "b": 0.2,
#         "c": 0.5
#     }
# '''
#
# d _ j___.l... ? parse_float_ma.._d..
# # # Received: <class 'str'> 0.2
# # # Received: <class 'str'> 0.5
# # ######################################################################################################################
#
# print(d)
# # {'a': 100, 'b': Decimal('0.2'), 'c': Decimal('0.5')}
# # ######################################################################################################################
#
# # As you can see we have decimals in our dictionary, instead of floats. Note also that the argument we receive
# # is a string - it would make little sense for us to receive a float since our function is the one that wants
# # to specifically handle converting a JSON string to some particular type.
# # We can also intercept handling of integers and those constant values I mentioned.
# print('#' * 52 + '  As you can see we have decimals in our dictionary, instead of floats.')
# print('#' * 52 + '  Note also that the argument we receive is a string - it would make little sense for us to receive'
#                  '  a float since our function is the one that wants to specifically handle converting '
#                  '  a JSON string to some particular type.')
# print('#' * 52 + '  We can also intercept handling of integers and those constant values I mentioned.')
#
# j = '''
#     {
#         "a": 100,
#         "b": Infinity
#     }
# '''
#
# print j___.l... ?
# # {'a': 100, 'b': inf}
# # ######################################################################################################################
#
# ___ make_int_binary arg
#     print('Received:' ty.. ar. ar.
#     r_ bi. in. ar.
#
#
# ___ make_const_none arg
#     print('Received:' ty.. ar. ar.
#     r_ N..
#
#
# print(j___.l... j
#            parse_int_ma...
#            parse_constant_ma_no..
# # Received: <class 'str'> 100
# # Received: <class 'str'> Infinity
# # {'a': '0b1100100', 'b': None}
# # ######################################################################################################################
#
# # Again note that in all cases, the received argument is the string read f... the json string.
# # Finally we have the object_pairs_hook argument. It works similarly to the object_hook with two differences:
# # the argument is a list of 2-tuples - the first value is the key, the second is the value
# # the list is ordered in the same order as the keys in the json document.
# # Remember that the dictionary is not guaranteed to be ordered in the same order as the keys in the json document -
# # given Python 3.6+ has guaranteed dictionary order, this is likely to be true, but the documents do not mention this
# # specifically, so at this point it should be considered an implementation detail and not relied on - if you must have
# # gauranteed key order, then you will have to use the object_pairs_hook.
# # Also, you should not specify both object_hook and object_pairs_hook - if you do, then the object_pairs_hook will
# # be used and object_hook will be ignored.
#
#
# print('#' * 52 + '  Also, you should not specify both `object_hook` and `object_pairs_hook` - if you do, '
#                  '  then the `object_pairs_hook` will be used and `object_hook` will be ignored.')
#
# j _ '''
#     {
#         "a": [1, 2, 3, 4, 5],
#         "b": 100,
#         "c": 10.5,
#         "d": NaN,
#         "e": null,
#         "f": "python"
#     }
# '''
#
#
# ___ float_handler ar.
#     print('float handler' ty.. ar. ar.
#     r_ fl.. ar.
#
#
# ___ int_handler arg
#     print 'int handler' ty.. ar. ar.
#     r_ in. ar.
#
#
# ___ const_handler arg
#     print 'const handler', ty.. ar. ar.
#     r.. N..
#
#
# ___ obj_hook(arg):
#     print('obj hook' ty.. ar. ar.
#     r_ ar.
#
#
# ___ obj_pairs_hook ar.
#     print('obj pairs hook' ty.. ar. ar.
#     return arg
#
# print j___.l... ?
# # {'a': [1, 2, 3, 4, 5], 'b': 100, 'c': 10.5, 'd': nan, 'e': None, 'f': 'python'}
# # ######################################################################################################################
#
#
# print j___.l... ?
#            object_hook _ o._h..
#            parse_float _ fl.._h..
#            parse_int _ in.._ha_
#            parse_constant _ c._h..
#           ))
# # int handler <class 'str'> 1
# # int handler <class 'str'> 2
# # int handler <class 'str'> 3
# # int handler <class 'str'> 4
# # int handler <class 'str'> 5
# # int handler <class 'str'> 100
# # float handler <class 'str'> 10.5
# # const handler <class 'str'> NaN
# # obj hook <class 'dict'> {'a': [1, 2, 3, 4, 5], 'b': 100, 'c': 10.5, 'd': None, 'e': None, 'f': 'python'}
# # {'a': [1, 2, 3, 4, 5],
# #  'b': 100,
# #  'c': 10.5,
# #  'd': None,
# #  'e': None,
# #  'f': 'python'}
# # ######################################################################################################################
#
# print j___.l... ?
#            object_pairs_hook_ob._p.._h..
#            parse_float _ f.._ha..
#            parse_int _ in._ha..
#            parse_constant _ c.._ha..
#           ))
# # int handler <class 'str'> 1
# # int handler <class 'str'> 2
# # int handler <class 'str'> 3
# # int handler <class 'str'> 4
# # int handler <class 'str'> 5
# # int handler <class 'str'> 100
# # float handler <class 'str'> 10.5
# # const handler <class 'str'> NaN
# # obj pairs hook <class 'list'> [('a', [1, 2, 3, 4, 5]), ('b', 100), ('c', 10.5), ('d', None), ('e', None), ('f', 'python')]
# # [('a', [1, 2, 3, 4, 5]),
# #  ('b', 100),
# #  ('c', 10.5),
# #  ('d', None),
# #  ('e', None),
# #  ('f', 'python')]
# # ######################################################################################################################
#
# print('#' * 52 + '  And if we specify both object hooks, then `object_hook` is basically ignored:')
#
# print j___.l... j
#            object_hook _ ob._h..
#            object_pairs _ hook_o._p._h.
#            parse_float _ fl.._ha..
#            parse_int _ in._ha..
#            parse_constant _ c.._h..
#           ))
# # int handler <class 'str'> 1
# # int handler <class 'str'> 2
# # int handler <class 'str'> 3
# # int handler <class 'str'> 4
# # int handler <class 'str'> 5
# # int handler <class 'str'> 100
# # float handler <class 'str'> 10.5
# # const handler <class 'str'> NaN
# # obj pairs hook <class 'list'> [('a', [1, 2, 3, 4, 5]), ('b', 100), ('c', 10.5), ('d', None), ('e', None), ('f', 'python')]
# # [('a', [1, 2, 3, 4, 5]),
# #  ('b', 100),
# #  ('c', 10.5),
# #  ('d', None),
# #  ('e', None),
# #  ('f', 'python')]
# # ######################################################################################################################
#
# # As we saw in the decoding videos, we can also subclass the JSONDecoder class (just like we subclassed the JSONEncoder - we'll look at this next.
