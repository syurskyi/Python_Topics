#
# # The problem is that if you inserted a date object in the database,
# # most of the time you are expecting a date object when you retrieve it, not a string object.
# # This problem can be solved passing PARSE_DECLTYPES and PARSE_COLNAMES to the connect method:
#
# _____ ?
# from d_t_ _____ date, d_t_
#
# db _ ?.c.. ':memory:', detect_types_?.P_DE__ _ ?.P_CO..
# c _ ?.c..
# c.e.. '''C.. T.. example(id IN.. P.. K.., created_at DATE)'''
# # Insert a date object into the database
# today _ da__.to..
# c.e.. '''I.. I.. example(created_at) V..(?)''' ?
# ?.c..
#
# # Retrieve the inserted object
# c.e.. '''S.. created_at F.. example'''
# row _ c.f_o..
# print('The date is @ and the datatype is @'.f.. ? 0 ty.. ? 0
# # The date is 2013-04-14 and the datatype is <class 'datetime.date'>
#
# # Changing the connect method, the database now is returning a date object.
# # The ? module uses the column's type to return the correct type of object.
# # So, if we need to work with a datetime object, we must declare the column in the table as a timestamp type:
#
# ?.c..
