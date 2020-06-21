class WaitingList:
	
	def __init__(self, clients=None):
                if clients == None:
                        self.clients = []
                else:
                        self.clients = clients
		
	def add_client(self, client):
		self.clients.append(client)
		
	def __add__(self, other):
		return WaitingList(self.clients + other.clients)
