# f___ collections ______ d..d..
#
# # Let's take a look at another example of where a defaultdict can be useful.
# # Suppose we have a dictionary structure that has people's names as keys, and a dictionary for the value that contains
# # the person's eye color. We want to create a dictionary of eye colors, with a list of the people's names that have
# # that eye color:
#
# persons _
#     'john': {'age': 20, 'eye_color': 'blue'},
#     'jack': {'age': 25, 'eye_color': 'brown'},
#     'jill': {'age': 22, 'eye_color': 'blue'},
#     'eric': {'age': 35},
#     'michael': {'age': 27}
#
#
# # What we want is a dictionary with the eye colors (and unknown as the key i_ the eye color was not specified),
# # and the names of the people with that eye color.
# # Let's first do this without a defaultdict, and also not using .get:
#
# eye_colors _
# ___ person, details i_ pe__.it__(
#     i_ 'eye_color' i_ details:
#         color _ de... 'eye_color'
#     e___
#         color _ 'unknown'
#     i_ color i_ e.._c..
#         e.._c.. color .ap.. pe..
#     e___:
#         e.._co.. co.. _ [pe..
#
# print(eye_colors)
# # {'blue': ['john', 'jill'], 'brown': ['jack'], 'unknown': ['eric', 'michael']}
#
# # Now let's simplify this by leveraging the .get method:
#
# eye_colors _
# ___ person, details i_ persons.it__
#     color _ det__.ge. 'eye_color' 'Unknown'
#     person_list _ e___c__.ge. co.. ||
#     pe.._l__.ap.. pe__
#     e.._co.. co.. _ person_list
#
# print e.._c..
# # {'blue': ['john', 'jill'], 'brown': ['jack'], 'Unknown': ['eric', 'michael']}
#
# # And finally let's use a defaultdict:
#
# eye_colors _ d..d.. li__
#
# ___ person, details i_ pe___.it__
#     color _ de__.ge. 'eye_color' 'Unknown'
#     e.._co.. co__ .ap.. pe..
#
# print e.._c..
# # defaultdict(list,
# #             {'blue': ['john', 'jill'],
# #              'brown': ['jack'],
# #              'Unknown': ['eric', 'michael']})
#
# # When we create a defaultdict we have to specify the factory method as the first argument, but thereafter we can
# # specify key/value pairs just like we would with the dict constructor (they are basically just passed along to the underlying dict):
#
# d _ d..d.. bo.. k1_T.. k2_F.. k3_'python'
# d
# # defaultdict(bool, {'k1': True, 'k2': False, 'k3': 'python'})
#
# # So, using this, i_ we had used a defaultdict ___ the Person values, we could simplify our previous example a bit more:
#
# persons _ {
#     'john': d..d..(l____: 'unknown',
#                         age_20, eye_color_'blue'),
#     'jack': d..d..(l____: 'unknown',
#                         age_20, eye_color_'brown'),
#     'jill': d..d..(l____: 'unknown',
#                         age_22, eye_color_'blue'),
#     'eric': d..d..(l____: 'unknown', age_35),
#     'michael': d..d..(l____: 'unknown', age_27)
# }
#
# eye_colors _ d..d.. li__
#
# ___ person, details i_ persons.it__
#     e.._co.. de.. 'eye_color' .ap.. pe..
#
# print e.._c..
#
# # defaultdict(list,
# #             {'blue': ['john', 'jill'],
# #              'brown': ['jack'],
# #              'unknown': ['eric', 'michael']})
#
# # It was a little tedious defining that defaultdict ___ every instance in our persons dictionary.
# # This is a good example of where a partial function would be really useful. (I cover partial functions in Part
# # 1 of this series, or you can review the documentation here:
# # https://docs.python.org/3.7/library/functools.html#functools.partial
# # (You can also just use a lambda function as well)
#
# f___ fu.. ______ par..
# eyedict _ par.. d..d.., l____ 'unknown'
#
# # Alternatively we could also just define it this way:
#
# eyedict _ l____ 0a.. 00k..; d..d.. l____ 'unknown' 0a.. 00k..
#
# persons _ {
#     'john': eyedict(age_20, eye_color_'blue'),
#     'jack': eyedict(age_20, eye_color_'brown'),
#     'jill': eyedict(age_22, eye_color_'blue'),
#     'eric': eyedict(age_35),
#     'michael': eyedict(age_27)
# }
#
# print(persons)
#
# # {'john': defaultdict(<function __main__.<l____>.<locals>.<l____>()>,
# #              {'age': 20, 'eye_color': 'blue'}),
# #  'jack': defaultdict(<function __main__.<l____>.<locals>.<l____>()>,
# #              {'age': 20, 'eye_color': 'brown'}),
# #  'jill': defaultdict(<function __main__.<l____>.<locals>.<l____>()>,
# #              {'age': 22, 'eye_color': 'blue'}),
# #  'eric': defaultdict(<function __main__.<l____>.<locals>.<l____>()>,
# #              {'age': 35}),
# #  'michael': defaultdict(<function __main__.<l____>.<locals>.<l____>()>,
# #              {'age': 27})}
#
# # And we can use our previous code just as before:
#
# eye_colors _ d..d.. li__
# ___ person, details i_ persons.it__
#     e.._co.. de.. 'eye_color' .ap.. pe..
#
# print ey..
#
# # defaultdict(list,
# #             {'blue': ['john', 'jill'],
# #              'brown': ['jack'],
# #              'unknown': ['eric', 'michael']})
#
# # Let's look at another example where we use a non-deterministic factory. We could make a database call, an API call,
# # and so on. To keep this simple I'm going to use the current time as my default.
# #
# # i_ this example we want to keep track of how many times certain functions are being called, as well as
# # when they were first called. To do this I want to be able to decorate the functions I want to keep track of,
# # and I want to be able to specify the dictionary that should be used so I can keep a reference
# # to it so I can examine the results.
#
# f___ c.. ______ d..d.., n..t..
# f___ dat.. ______ dat..
# f___ fun.. ______ wr..
#
#
# ___ function_stats
#     d _ d..d.. l____  "count": 0 "first_called": dat__.utcnow
#     Stats _ n..t.. 'Stats' 'decorator data'
#
#     ___ decorator fn
#         0wr.. fn
#         ___ wrapper 0a.. 00k..
#             d[fn.__n__ 'count' +_ 1
#             r_ fn 0a.. 00k..
#
#         r_ w..
#
#     r_ Stats d... d
#
# stats _ f.._s..
# di.. st__.da..
# # {}
#
# 0st__.d..
# ___ func_1
#     p..
#
# 0s__.d..
# ___ func_2 x y
#     p..
# di.. s__.da..
# # {}
#
# func_1
# di.. st__.da..
# # {'func_1': {'count': 1,
# #   'first_called': datetime.datetime(2018, 12, 29, 22, 43, 48, 828143)}}
#
# func_1
# di.. st__.da..
# # {'func_1': {'count': 2,
# #   'first_called': datetime.datetime(2018, 12, 29, 22, 43, 48, 828143)}}
#
# func_2 10 20
# di.. st__.da..
# # {'func_1': {'count': 2,
# #   'first_called': datetime.datetime(2018, 12, 29, 22, 43, 48, 828143)},
# #  'func_2': {'count': 1,
# #   'first_called': datetime.datetime(2018, 12, 29, 22, 43, 49, 714090)}}
#
