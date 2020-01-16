# # Custom JSON Serialization
# # As we saw in the previous video, certain data types cannot be serialized to JSON using Python's defaults.
# # Here's a simple example of this:
# 
# f... d..t.. ______ d..t..
# 
# current _ d..t_.u..n..
# 
# print ?
# # datetime.datetime(2018, 12, 29, 22, 26, 35, 671836)
# 
# print('#' * 52 + '  As we can see, this is a `datetime` object.')
# 
# ______ j___
# 
# # json.dumps(current)  #  TypeError: Object of type 'datetime' is not JSON serializable
# # TypeError: Object of type 'datetime' is not JSON serializable
# # As we can see Python raises a TypeError exception, stating that datetime objects are not JSON serializable.
# # So, we'll need to come up with our own serialization format.
# # For datetimes, the most common format is the ISO 8601 format - you can read up more about it here
# # (https://en.wikipedia.org/wiki/ISO_8601), but basically the format is:
# # YYYY-MM-DD T HH:MM:SS
# # There are some variations for encoding timezones, but to keep things simple I am going to use timezone naive
# # timestamps, and just use UTC everywhere.
# # We could use Python's string representation for datetimes:
# 
# print()
# print('#' * 52 + '  We could use Pythons string representation for datetimes:')
# print st. ?
# # '2018-12-29 22:26:35.671836'
# # ######################################################################################################################
# 
# print('#' * 52 + '  but this is not quite ISO-8601. We could write a custom formatter ourselves:')
# 
# ___ format_iso dt
#     r_ ?.st..ti.. %Y-%m-%dT%H:%M:%S
# 
# # (If you want more info and options on date and time formatting/parsing using strftime and strptime,
# # which essentially pass through to their C counterparts, you can see the Python docs here:
# # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
# 
# print f.. ?
# # '2018-12-29T22:26:35'
# # ######################################################################################################################
# 
# print('#' * 52 + '  But Python actually provides us a function to do the same:')
# 
# print c__.i..f..
# # 2018-12-29T22:26:35.671836'
# # ######################################################################################################################
# 
# # This is almost identical to our custom representation, but also includes fractional seconds.
# # If you don't want fractional seconds in your representation, then you'll have to write some custom code like the one
# # above. I'm just going to use Python's ISO-8601 representation. And now let's serialize our datetime object to JSON:
# print('#' * 52 + '  This is'
#                  '  almost identical to our custom representation, but also includes fractional seconds.')
# print('#' * 52 + '  If you dont want fractional seconds in your representation, '
#                  '  then you will have to write some custom code like the one above.')
# print()
# 
# log_record _ 'time' d..t_.u_n__.i..f.. 'message' 'testing'
# print j___.d___ ?
# # '{"time": "2018-12-29T22:26:42.083020", "message": "testing"}'
# # ######################################################################################################################
# 
# print('#' * 52 + '  OK, this works, but this is far from ideal.')
# print('#' * 52 + '  Normally, our dictionary will contain the `datetime` object, not its string representation.')
# 
# log_record _ 'time': d..t_.u..n.. 'message': 'testing'
# # The problem is that log_record is now not JSON serializable!
# # What we have to do is write custom code to replace non-JSON serializable objects in our dictionary with custom
# # representations. This can quickly become tedious and unmanageable if we deal with many dictionaries,
# # and arbitrary structures.
# # Fortunately, Python's dump and dumps functions have some ways for us to define general serializations for
# # non-standard JSON objects.
# # The simplest way is to specify a function that dump/dumps will call when it encounters something it cannot serialize
# 
# ___ format_iso dt
#     r_ ?.i.f.
# 
# print j___.d___ ? de.._f..
# # '{"time": "2018-12-29T22:26:42.532485", "message": "testing"}'
# # ######################################################################################################################
# 
# print('#' * 52 + '  This will work even if we have more than one date in our dictionary:')
# 
# log_record _
#     'time1' d..t_.u..n..
#     'time2' d..t_.u..n..
#     'message' 'Testing...'
# 
# 
# print j___.d___ ? d.._f...
# # '{"time1": "2018-12-29T22:26:43.296170", "time2": "2018-12-29T22:26:43.296171", "message": "Testing..."}'
# # ######################################################################################################################
# 
# print('#' * 52 + '  So this works, but what happens if we introduce another non-serializable object:')
# 
# log_record _
#     'time': d..t_.u..n..(
#     'message': 'Testing...'
#     'other': {'a', 'b', 'c'}
# 
# 
# # json.dumps(log_record, default=format_iso) # AttributeError: 'set' object has no attribute 'i.f.'
# # AttributeError: 'set' object has no attribute 'i.f.'
# # As you can see, Python encountered that set, and therefore called the default callable - but that callable was not
# # designed to handle sets, and so we end up with an exception in the format_iso callable instead
# # We can remedy this by essentially adding code to our function to make it handle various data types.
# # Essentially creating a dispatcher - this should remind you of the single-dispatch generic function decorator
# # available in the functools module which we discussed in an earlier part of this series. You can also view more
# # info about it here: https://docs.python.org/3/library/functools.html#functools.singledispatch
# # Let's first write it without the decorator to make sure we have our code correct:
# 
# print('#' * 52 + '  Lets first write it without the decorator to make sure we have our code correct:')
# 
# ___ custom_json_formatter arg
#     __ isi.. ? d_t_
#         r_ ?.i.f.
#     ____ isi.. ? se.
#         r_ l__ ?
# 
# print j___.d___ l._r. d.._?
# # '{"time": "2018-12-29T22:26:43.760863", "message": "Testing...", "other": ["c", "a", "b"]}'
# # ######################################################################################################################
# 
# print('#' * 52 + '  To make things a little more interesting, lets throw in a custom object as well:')
# 
# c_ Person:
#     ___ -i name age
#         ____.?  ?
#         ____.?  ?
#         ____.create_dt = d..t_.u..n..
# 
#     ___ -r
#         r_ _*P.. |n.._|____.n.. a.._|____.a..
# 
#     ___ toJSON ____
#         r_
#             'name': ____.?
#             'age': ____.?
#             'create_dt': ____.?.i.f.
# 
# 
# 
# p = ? John 82
# print ?
# print ?.__J..
# # Person(name=John, age=82)
# # {'name': 'John', 'age': 82, 'create_dt': '2018-12-29T22:26:45.066252'}
# # ######################################################################################################################
# 
# print('#' * 52 + '  And we modify our custom JSON formatter as follows:')
# 
# 
# ___ custom_json_formatter arg
#     __ isi..(? d..t_
#         r_ ?.i.f.
#     ____ isi.. ? s..
#         r_ l.. ?
#     ____ isi.. ? P..
#         r_ ?.__J..
# 
# 
# log_record _ di.. ti.._d..t_.u..n..
#                   message_'Created new person record',
#                   person_p
# 
# print j___.d___ lo._r_ de.._c..
# # '{"time": "2018-12-29T22:26:45.769929", "message": "Created new person record", "person": {"name": "John", "age": 82, "create_dt": "2018-12-29T22:26:45.066252"}}'
# # ######################################################################################################################
# 
# print j___.d___ l... de.._cu....., in.._2
# # {
# #   "time": "2018-12-29T22:26:45.769929",
# #   "message": "Created new person record",
# #   "person": {
# #     "name": "John",
# #     "age": 82,
# #     "create_dt": "2018-12-29T22:26:45.066252"
# #   }
# # }
# # ######################################################################################################################
# 
# print('#' * 52 + '  One thing to note here is that for the `Person` class'
#                  '  we returned a formatted string for the `created_dt` attribute.')
# print('#' * 52 + '  We dont actually need to do this - we can simply r_ a `datetime` object and'
#                  '  let `custom_json_formatter` handle serializing the `datetime` object:')
# 
# c_ Person
#     ___ - name age
#         ____.? _ ?
#         ____.? _ ?
#         ____.create_dt _ d..t_.u..n..
# 
#     ___ -r
#         r_ _*P... n.._|____.n.. a.._ ____.a..
# 
#     ___ toJSON ____
#         r_
#             'name': ____.?
#             'age': ____.?
#             'create_dt': ____.?
# 
# 
# 
# p _ ? Monty 100
# 
# log_record _ di.. time_d..t_.u..n..
#                   message_'Created new person record',
#                   person_p
# 
# print j___.d___ l.. de.._cu..., in.._2
# # {
# #   "time": "2018-12-29T22:26:47.029102",
# #   "message": "Created new person record",
# #   "person": {
# #     "name": "Monty",
# #     "age": 100,
# #     "create_dt": "2018-12-29T22:26:46.749022"
# #   }
# # }
# # ######################################################################################################################
# 
# print('#' * 52 + '  In fact, we could simplify our class further by simply returning a dict of the attributes, '
#                  '  since in this case we want to serialize everything as is.')
# print('#' * 52 + '  But using the `toJSON` callable means we can customize exactly '
#                  '  how we want out objects to be serialized.')
# print('#' * 52 + '  So, if we were +not particular about the serialization we could do this:')
# 
# 
# c_ Person
#     ___ - name age
#         ____.?  ?
#         ____.?  ?
#         ____.create_dt _ d..t_.u..n..
# 
#     ___ -r
#         r_ _*P.. n.._|____.n.. a.._|____.a..
# 
#     ___ toJSON ____
#         r_ va.. ____
# 
# p _ ? Python 27
# 
# print p.__J..
# # {'name': 'Python',
# #  'age': 27,
# #  'create_dt': datetime.datetime(2018, 12, 29, 22, 26, 47, 973930)}
# # ######################################################################################################################
# 
# print()
# print()
# print()
# print('#' * 52 + '  ')
# 
# log_record['person'] _ p
# print ?
# # {'time': datetime.datetime(2018, 12, 29, 22, 26, 47, 29102), 'message': 'Created new person record', 'person': Person(name=Python, age=27)}
# # ######################################################################################################################
# 
# print j___.d___ lo.., de.._cu..., in.._2
# # {
# #   "time": "2018-12-29T22:26:47.029102",
# #   "message": "Created new person record",
# #   "person": {
# #     "name": "Python",
# #     "age": 27,
# #     "create_dt": "2018-12-29T22:26:47.973930"
# #   }
# # }
# # ######################################################################################################################
# 
# print('#' * 52 + '  In fact, we could use this approach in our custom formatter - '
#                  '  if an object does not have a `toJSON` callable,')
# print('#' * 52 + '  we will just use a dictionary of the attributes - it it has any, '
#                  '  it might not (like a complex number or a set as examples), '
#                  '  so we need to watch out for that as well.')
# 
# print 'toJSON' i_ va.. P..
# # True
# # ######################################################################################################################
# 
# ___ custom_json_formatter arg
#     __ isi.. ? d..t_
#         r_ ?.i.f.
#     ____ isi.. ? se.
#         r_ li.. ?
#     ____
#         t__
#             r_ ?__J..
#         ____ A..
#             ...
#                 r_ v.. ?
#             .... T.
#                 r_ st. a..
# 
# 
# print('#' * 52 + '  Lets create another custom class that does not have a `toJSON` method:')
# 
# c_ Point
#     ___ - x y
#         ____.?  ?
#         ____.?  ?
# 
#     ___ -r
#         r_ _*P.. x_|____.x y_|____.y
# 
# 
# pt1 _ P.. 10 10
# 
# print(vars(pt1))
# # {'x': 10, 'y': 10}
# # ######################################################################################################################
# 
# log_record _ di.. time_d..t_.u..n..
#                   message_'Created new point',
#                   point_pt1
#                   created_by_p
# 
# print ?
# # {'time': datetime.datetime(2018, 12, 29, 22, 26, 50, 955039),
# #  'message': 'Created new point',
# #  'point': Point(x=10, y=10),
# #  'created_by': Person(name=Python, age=27)}
# # ######################################################################################################################
# 
# print('#' * 52 + '  And we can now serialize it to JSON:')
# 
# print j___.d___ lo.. de..... in.._2
# # {
# #   "time": "2018-12-29T22:26:50.955039",
# #   "message": "Created new point",
# #   "point": {
# #     "x": 10,
# #     "y": 10
# #   },
# #   "created_by": {
# #     "name": "Python",
# #     "age": 27,
# #     "create_dt": "2018-12-29T22:26:47.973930"
# #   }
# # }
# # ######################################################################################################################
# 
# print('#' * 52 + '  So now, lets re-write our custom json formatter using the generic single dispatch decorator'
#                  '  I mentioned earlier:')
# 
# f... fun____ ______ s..d..
# 
# # Our default approach is going to first try to use toJSON, if not it will try to use vars, and it that still fails
# # we'll use the string representation, whatever that happens to be:
#
# ??
# ___ json_format arg
#     print ?
#     ___
#         print('\ttrying to use toJSON...')
#         r_ ?.__J..
#     ____ A..
#         print('\tfailed - trying to use vars...')
#         t__
#             r_ va.. ?
#         ____ T..
#             print('\tfailed - using string representation...')
#             r_ st. ?
# 
# # And now we 'register' other data types:
# 
# 0j._f..reg.. d..t_
# ___ _ arg
#     r_ a__.i.f.
# 
# 
# 0j._f..reg.. se.
# ___ _ arg
#     r_ li.. a..
# 
# print j___.d___ lo.. de.._j.._fo.. in.._2
# # Point(x=10, y=10)
# # 	trying to use toJSON...
# # 	failed - trying to use vars...
# # Person(name=Python, age=27)
# # 	trying to use toJSON...
# # {
# #   "time": "2018-12-29T22:26:50.955039",
# #   "message": "Created new point",
# #   "point": {
# #     "x": 10,
# #     "y": 10
# #   },
# #   "created_by": {
# #     "name": "Python",
# #     "age": 27,
# #     "create_dt": "2018-12-29T22:26:47.973930"
# #   }
# # }
# # ######################################################################################################################
# 
# print('#' * 52 + '  Lets change our Person class to emit some custom JSON instead of just using `vars`:')
# 
# c_ Person:
#     ___ - name age
#         ____.?  ?
#         ____.?  ?
#         ____.create_dt _ d..t_.u..n..
# 
#     ___ -r
#         r_ _*P.. n.._|____.n.. a.. |____.a..
# 
#     ___ toJSON ____
#         r_ di.. n.._ ____.n..
# 
# p _ P.. Python 27
# l.._r.. 'created_by' _ ?
# print j___.d___ l._r., de.._j.._f.. in.._2
# # Point(x=10, y=10)
# # 	trying to use toJSON...
# # 	failed - trying to use vars...
# # Person(name=Python, age=27)
# # 	trying to use toJSON...
# # {
# #   "time": "2018-12-29T22:26:50.955039",
# #   "message": "Created new point",
# #   "point": {
# #     "x": 10,
# #     "y": 10
# #   },
# #   "created_by": {
# #     "name": "Python"
# #   }
# # }
# # ######################################################################################################################
# 
# print('#' * 52 + '  The way we wrote our default formatter,'
#                  '  means that we can now also represent other unexpected data types, '
#                  '  but using each objects string representation.')
# print('#' * 52 + '  If that is not acceptable, we can either not do this and let a `TypeError` exception get generated,'
#                  '  or register more custom formatters:')
# 
# f... dec.. ______ D..
# f... fr.. ______ F..
# 
# print(j___.d___(dict(a=1 + 1j,
#                       b_D..('0.5'),
#                       c_F..(1, 3),
#                       p_P..('Python', 27),
#                       pt_P..(0, 0),
#                       time_d..t_.u..n..()
#                       ),
#                  default _ js.._f..
# # (1+1j)
# # 	trying to use toJSON...
# # 	failed - trying to use vars...
# # 	failed - using string representation...
# # 0.5
# # 	trying to use toJSON...
# # 	failed - trying to use vars...
# # 	failed - using string representation...
# # 1/3
# # 	trying to use toJSON...
# # 	failed - trying to use vars...
# # 	failed - using string representation...
# # Person(name=Python, age=27)
# # 	trying to use toJSON...
# # Point(x=0, y=0)
# # 	trying to use toJSON...
# # 	failed - trying to use vars...
# # '{"a": "(1+1j)", "b": "0.5", "c": "1/3", "p": {"name": "Python"}, "pt": {"x": 0, "y": 0}, "time": "2018-12-29T22:26:54.860340"}'
# # ######################################################################################################################
# 
# print('#' * 52 + '  Now, suppose we dont want that default representation for `Decimals` -'
#                  '  we want to serialize it in this form: `Decimal(0.5)`.')
# print('#' * 52 + '  All we need to do is to register a new function to serialize `Decimal` types:')
# 
# 
# 0j.._fo__.re.. D...
# ___ _ arg
#     r_ _*D.. |st. ?
# 
# 
# print j___.d___ d... a_1 + 1j,
#                       b_D... 0.5
#                       c_F... 1, 3
#                       p_P... Python 27
#                       pt_Po.. (0 0
#                       time_d..t_.u..n..
#                       ),
#                  default_j.._f..
# # (1+1j)
# # 	trying to use toJSON...
# # 	failed - trying to use vars...
# # 	failed - using string representation...
# # 1/3
# # 	trying to use toJSON...
# # 	failed - trying to use vars...
# # 	failed - using string representation...
# # Person(name=Python, age=27)
# # 	trying to use toJSON...
# # Point(x=0, y=0)
# # 	trying to use toJSON...
# # 	failed - trying to use vars...
# # '{"a": "(1+1j)", "b": "Decimal(0.5)", "c": "1/3", "p": {"name": "Python"}, "pt": {"x": 0, "y": 0}, "time": "2018-12-29T22:26:55.491606"}'
# # ######################################################################################################################
# 
# print(
#     '#' * 52 + '  One last example that clearly shows the `json_format` function gets called recursively when needed:')
# 
# print(j___.d___ d.. pt _ Po.. P.. Python 27 2+2j
#           de.._j.._f.. in.._2
# # Point(x=Person(name=Python, age=27), y=(2+2j))
# # 	trying to use toJSON...
# # 	failed - trying to use vars...
# # Person(name=Python, age=27)
# # 	trying to use toJSON...
# # (2+2j)
# # 	trying to use toJSON...
# # 	failed - trying to use vars...
# # 	failed - using string representation...
# # {
# #   "pt": {
# #     "x": {
# #       "name": "Python"
# #     },
# #     "y": "(2+2j)"
# #   }
# # }
# # ######################################################################################################################
