# ____ _______ _______ _______
#
# client _ _______
#
#
# ___ insert dbname, collection, data
# 	___
# 		db _ ? ?
# 		collection _ ? ?
# 		?.i.. ?
# 	______
# 		r_ *c.. 2 *m.. *Insert failed
#
# 	r_ *c.. 1 *m.. *Successfully inserted
#
#
# ___ find dbname collection query
# 	___
# 		db _ ? ?
# 		collection _ ? ?
# 		result _ ?.f.. ?
# 	______
# 		r_ *c.. 2 *m.. *Find error
#
# 	r_ *c.. 1 *m.. li.. ?
#
#
# ___ getDbs
# 	___
# 		result _ ?.d_n..
# 	______
# 		r_ *c.. 2, *m.. *Find error
#
# 	r_ *c.. 1, *m.. ?
#
#
# ___ getCollections dbname
# 	___
# 		db _ ? ?
# 		result _ ?.c_n..
# 	______
# 		r_ *c.. 2, *m.. *Find error
#
# 	r_ *c.. 1, *m.. result
#
#
# ___ delete dbname, collection, query)
# 	___
# 		db _ ?
# 		collection _ ?
# 		collection.r.. ?
# 	______
# 		r_ *c.. 2, *m.. *Delete error
#
# 	r_ *c.. 1, *m.. *Successfully Deleted
#
#
# ___ login user password
# 	___
# 		db _ ? _co..
# 		collection _ ? _us..
# 		__ le. li.. ?.f.. __ 0
# 			__ u.. __ *r.. an. p.. __ *r..
# 				r_ *c.. 1, *m.. |*u.. *r.. *p.. *r..
# 		result _ ?.f.. *u.. u.. *p.. p..
# 	______
# 		r_ *c.. 2 *m.. *Login error
#
# 	r_ *c.. 1, *m.. li.. ?
#
#
# ___ signup user password
# 	___
# 		db _ ? _c..
# 		collection _ ? '_u..
# 		?.i.. *u.. u.. *p.. p..
# 	______
# 		r_ *c.. 2 *m.. *Signup error
#
# 	r_ *c.. 1, *m.. *Signed up sucessfully
