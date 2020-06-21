# _______ common
# _______ sys
# _______ backend
# ____ ?.?G.. _______ _
# ____ ?.?W.. _______ _
# _______ json
# ____ bs__.j_u.. _______ d..
# ____ F.. _______ F..
#
# c_ Data ?D..
# 	___  - ? p.._N..
# 		s__ ?D. ?. - ?
#
# 		grid _ ?GL..
# 		sL.. ?
#
# 		r.. 400, 400
# 		m.. 300, 300
# 		sWT.. 'Mongo Admin - Data'
#
# 		collectionDropdown _ ?CB..
# 		databaseDropdown _ ?CB..
# 		dbs _ b__.gD.. *m..
# 		dD__.cIC...c.. lC..
# 		___ db __ dbs
# 			dD__.aI.. ?
#
# 		queryLineEdit _ ?LE..
# 		?.sPT.. 'query'
#
# 		resultsArea _ ?TE..
#
# 		deleteBtn _ ?PB.. *Delete
# 		?.c__.c.. oDDD..
# 		findBtn _ ?PB.. *Find
# 		?.c__.c.. oFDD..
# 		addBtn _ ?PB.. *Add
# 		?.c__.c.. oADD..
#
# 		g__.aW.. dD__, 1, 1
# 		g__.aW.. cD.. 1, 2
# 		# g__.addWidget(self.queryLineEdit, 2, 1)
# 		g__.aW.. fB.. 2, 1
# 		g__.aW.. dB.. 2, 2
# 		g__.aW.. aB.. 2, 3
# 		g__.aW.. rA.. 3, 1, 2, 3
#
# 	___ loadCollections
# 		cD__.c..
# 		db _ d..|dD__.cI..
# 		collections _ b__.gC.. ?|*m..
# 		print ?
# 		___ collection __ ?
# 			cD__.aI.. ?
#
# 	___ findData query_||
# 		db _ st. d..|dD__.cI..
# 		collection _ st. cD__.cT..
# 		result _ b__.f.. d. c.. q..
# 		formattedResult _ ''
# 		___ item __ r..|*m..
# 			formattedResult +_ du.. i.. .r.. '{', '{\n').r..('}', '}\n').r..(',', ',\n')
# 			formattedResult +_ '\n\n\n'
#
# 		rA__.sT.. ?
#
# 	___ addData , data
# 		db _ st. d..|dD__.cI..
# 		collection _ st. cD__.cT..
# 		result _ b__.i.. d. c.. d..
# 		fD..
#
# 	___ openAddDataDialog
# 		form _ F..  aD..
# 		?.e..
#
# 	___ openDeleteDataDialog
# 		form _ F.. dD..
# 		?.e..
#
# 	___ openFindDataDialog
# 		form _ F..  fD..
# 		?.e..
#
# 	___ deleteData  query
# 		db _ st. d..|dD__.cI..
# 		collection _ st. cD__.cT..
# 		result _ b__.d.. d. c.. q..
# 		fD..
