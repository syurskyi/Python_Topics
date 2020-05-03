c_ phone(object
	___  -
		model _ ''
		color _ 'red'
	
	___ call
		print('Call')
		
c_ phone2(phone
	___  -
		# phone.__init__(self)
		s__(phone2, self). - 
	
	___ sendMail
		pass
	
	___ call
		__ T..:
			pass
		____
			s__(phone2, self).call

p _ phone2
