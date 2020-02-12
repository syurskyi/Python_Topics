class phone(object):
	def __init__(self):
		self.model = ''
		self.color = 'red'
	
	def call(self):
		print('Call')
		
class phone2(phone):
	def __init__(self):
		# phone.__init__(self)
		super(phone2, self).__init__()
	
	def sendMail(self):
		pass
	
	def call(self):
		if True:
			pass
		else:
			super(phone2, self).call()

p = phone2
