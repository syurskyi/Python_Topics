# from collections ____ n_t_
#
# # Other Ways to Specify Field Names
# # There are a number of ways we can specify the field names for the named tuple:
# #     we can provide a sequence of strings containing each property name
# #     we can provide a single string with property names separated by whitespace or a comma
#
# Circle _ n_t_('Circle' 'center_x' 'center_y' 'radius'
# circle_1 _  C_ 0 0 10
# circle_2 _ C_ c._x_10 c._y_20 r.._100
# print c_1
# # Circle(center_x=0, center_y=0, radius=10)
#
# print c.._2
# # Circle(center_x=10, center_y=20, radius=100)
#
# # Or we can do it this way:
#
# City _ n_t_ 'City' 'name country population'
# new_york _ C__ 'New York' 'USA' 8_500_000
# print(n._y.
# # City(name='New York', country='USA', population=8500000)
#
# # This would work equally well:
#
# Stock _ n_t_ 'Stock' 'symbol, year, month, day, open, high, low, close'
# djia _ S.. 'DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393
# print d...
# # Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)
#
# # In fact, since whitespace can be used we can even use a multi-line string!
#
# Stock _ n_t_ 'Stock', '''symbol
#                                year month day
#                                open high low close'''
# djia _ S__ 'DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393
# print d..
# # Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)
#
# # Accessing Items in a Named Tuple
# # The major advantage of named tuples are that, as the name suggests, we can access the properties (fields)
# # of the tuple by name:
#
# # pt1   # ERROR NameError: name 'pt1' is not defined
# # pt1.x
# # 10
#
# print c.._1
# # Circle(center_x=0, center_y=0, radius=10)
#
# print c.._1.r..
# # 10
#
