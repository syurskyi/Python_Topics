# _____ ?
#
# conn_str _ 'mongodb://localhost:27017'
# client _ ?.M.. ?
#
# db _ ?.the_small_bookstore
#
# __ ?.b__.c.. __ 0
#     print("Inserting data")
#     # insert some data...
#     r _ ?.b__.i_o.. 'title' 'The third book' 'isbn' '73738584947384'
#     print ? ty.. ?
#     r _ ?.b__.i_o..({'title': 'The forth book', 'isbn': '181819884728473'})
#     print ?.i_i..
# ____
#     print("Books already inserted, skipping")
#
# # book = db.books.find_one({'isbn': '73738584947384'})
# # # print(book, type(book))
# # # book['favorited_by'] = []
# # book['favorited_by'].append(100)
# # db.books.update({'_id': book.get('_id')}, book)
# # book = db.books.find_one({'isbn': '73738584947384'})
# # print(book)
#
#
# ?.b__.u.. 'isbn' '181819884728473' '$addToSet' |'favorited_by' 120
# book _ ?.b__.f_o.. 'isbn' '181819884728473'
# print ?
